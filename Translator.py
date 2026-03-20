from googletrans import Translator as gTranlator
from deep_translator import GoogleTranslator
from Cache import Cache
from LanguageCache import LabguageCache
from TranslationCache import TranslationCache
from ui import ui
import asyncio
class Translator:
    def __init__(self):
        self._cacheTranlation = Cache("CacheTranslate.txt",TranslationCache,"Original","Translated")
        self._cacheLanguage = Cache("CacheLanguage.txt",LabguageCache,"Text","Language")
    def Translate(self, text, destLanguage):
        translation=self._cacheTranlation.GetValue(text)
        if translation!=None: 
            ui.printInternalProcess("Tranlated from cache")
            return translation

        ui.printInternalProcess("Getting language...")
        fileLanguage=self.__GetLanguaje(text[0:100])
        if fileLanguage == destLanguage:
            ui.printInternalProcess("No tanslate needed.")
            return text
        ui.printInternalProcess("Tranlating...")
        lineas= text.splitlines()
        nLines = len(lineas)
        nline=0
        textToTranslate = ""
        fullTextTranslated=""
        for linea in lineas:
            textToTranslate += linea + '\n'
            if len(textToTranslate) > 4000 or nline == nLines-1:            
                textoTraducido = GoogleTranslator(source='auto', target=destLanguage).translate(textToTranslate)
                if textoTraducido is not None:
                    fullTextTranslated +=  textoTraducido+ ' '
                textToTranslate = ""
            nline += 1
        self._cacheTranlation.Save(text,fullTextTranslated)
        return fullTextTranslated
    def __GetLanguaje(self,text):
        langCache =self._cacheLanguage.GetValue(text)
        if langCache!= None:
            ui.printStageMessageSubProcess("Language from cache")
            return langCache
        detected = asyncio.run(gTranlator().detect(text))
        self._cacheLanguage.Save(text,detected.lang)
        return detected.lang
