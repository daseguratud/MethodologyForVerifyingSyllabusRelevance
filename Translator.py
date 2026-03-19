from googletrans import Translator as gTranlator
from deep_translator import GoogleTranslator
from FileManager import FileManager
from TranslationCache import TranslationCache
from ui import ui
import asyncio
class Translator:
    def __init__(self):
        pass
    def Translate(self, text, destLanguage):
        cacheTranslations = self.__LoadCache()
        translation=[t for t in cacheTranslations if t.Original==text]
        existsTranslation = len(translation)>0
        if existsTranslation: 
            ui.printInternalProcess("Tranlated from cache")
            return translation[0].Translated

        ui.printInternalProcess("Getting language...")
        re=self.__GetLanguaje(text[0:100])
        fileLanguage = re.lang
        if fileLanguage == destLanguage:
            ui.printInternalProcess("No tanslate needed.")
            return text
        ui.printInternalProcess("Tranlating...")
        lineas= text.splitlines()
        nLines = len(lineas)
        nline=0
        textToTranslate = ""
        for linea in lineas:
            textToTranslate += linea + '\n'
            if len(textToTranslate) > 4000 or nline == nLines-1:            
                textoTraducido = GoogleTranslator(source='auto', target=destLanguage).translate(textToTranslate)
                if textoTraducido is not None:
                    translation +=  textoTraducido+ ' '
                textToTranslate = ""
            nline += 1
        self.__SaveCache(text,textoTraducido)
        return textoTraducido
    def __GetLanguaje(self,text):
        detected = asyncio.run(gTranlator().detect(text))
        return detected
    def __LoadCache(self):
        RS = '\x1E'  # separador de conjuntos
        US = '\x1F'  # separador de idiomas
        cacheTextsTranslatedText = FileManager.ReadAllText("CacheTranslate.txt")
        cacheTextsTranslated = cacheTextsTranslatedText.split(RS)
        cacheTextsTranslated = cacheTextsTranslated[:-1]
        cache=[TranslationCache(*ct.split(US)) for ct in cacheTextsTranslated]
        return cache
    def __SaveCache(self, Original, Translated):
        RS = '\x1E'  # separador de conjuntos
        US = '\x1F'  # separador de idiomas
        newCache = TranslationCache(Original, Translated)
        FileManager.AppendAllText("CacheTranslate.txt",f"{Original}{US}{Translated}{RS}")