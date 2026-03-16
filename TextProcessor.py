import asyncio
import re
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
from googletrans import Translator
from deep_translator import GoogleTranslator
from FileManager import FileManager
from ui import ui
class TextProcessor:
    def __init__(self):
        self.stopWords=self.__LoadCustomStopWords()
        self.destLanguage='en'
    @staticmethod
    def __LoadCustomStopWords():
        lineas=FileManager.ReadAllText("stopwords.csv").splitlines()
        stopwords = []
        for linea in lineas: 
            stopwords.append(linea.replace("\n",""))
        return stopwords 
    def GetLanguaje(self,text):
        detected = asyncio.run(Translator().detect(text))
        return detected
    def TranslateToTargetLanguage(self,text):
        re=self.GetLanguaje(text[0:100])
        fileLanguage = re.lang
        if fileLanguage == self.destLanguage:
            return text
        ui.printInternalProcess("Tranlating...")        
        traduccion=""
        lineas= text.splitlines()
        nLines = len(lineas)
        nline=0
        textToTranslate = ""
        for linea in lineas:
            textToTranslate += linea + '\n'
            if len(textToTranslate) > 4000 or nline == nLines-1:            
                textoTraducido = GoogleTranslator(source='auto', target=self.destLanguage).translate(textToTranslate)
                if textoTraducido is not None:
                    traduccion +=  textoTraducido+ '\n'
                textToTranslate = ""
            nline += 1
        return traduccion
    def CleanNumbersFromText(self,text):
        numbers = ['1','2','3','4','5','6','7','8','9','0','.']
        textResult=""
        for letra in text:
            if letra not in numbers:
                textResult += letra
        return textResult
    def CleanPunctuationFromText(self,text):
        punctuationMarks = [
            ".", ",", ";", ":", "!", "¡", "?", "¿",
            "'", '"', "(", ")", "[", "]", "{", "}",
            "-", "_", "/", "\\", "|",
            "@", "#", "$", "%", "&", "*", "+", "=",
            "<", ">", "^", "~", "`"
        ]
        textResult=text
        for mark in punctuationMarks:
            textResult=textResult.replace(mark," ")
        return textResult
    def SolveSpetialCases(self,text):
        cases = [
            ['´a','á'],
            ['´e','é'],
            ['´i','í'],
            ['´o','ó'],
            ['´u','ú'],
            ['´ a','á'],
            ['´ e','é'],
            ['´ i','í'],
            ['´ o','ó'],
            ['´ u','ú'],            
            ['´ ı','í'],            
            ['˜ n','ñ'],            
            ['“”',''],            
        ]
        textResult=text
        for c in cases:
            textResult = textResult.replace(c[0],c[1])
        return textResult
    def ToLowerCase(self,text):
        return text.lower()
    def RemoveExtraBlancks(self,text):
        lines = text.splitlines()
        resultLines = []        
        for line in lines:
            line=line.strip()
            if len(line) > 0:
                line =  re.sub(r' +', ' ', line).strip()
                resultLines.append(line)
        return '\n'.join(resultLines)
    def LemaText(self,text):
        normalizedText = text
        normalizationRules={
            "flipflops":"flipflop",
            "flip flops":"flipflop",
            "flip-flops":"flipflop",
            "flip-flop":"flipflop",
        }
        for pattern,normalText in normalizationRules.items():
            normalizedText = re.sub(pattern,normalText,normalizedText,) 
        return normalizedText
    def CreateWordCloud(self,text,fullCSVOutputFileName,showWordCloud=False):
        stopWords = STOPWORDS.union(self.stopWords)
        nube_palabras = WordCloud(
            max_words=1000,
            stopwords= stopWords,
            width=800, height=400, 
            background_color='white', 
            colormap='viridis').generate(text)
        frequencies = nube_palabras.words_
        nube_palabras.to_file(fullCSVOutputFileName.replace(".csv",".jpg"))
        if showWordCloud:
            plt.figure(figsize=(10, 5))
            plt.imshow(nube_palabras, interpolation='bilinear')
            plt.axis('off')
            plt.show()

        datFrec=[]
        for frecuency in frequencies.items():
            data=f"{frecuency[0]};{frecuency[1]}"
            datFrec.append(data)        
        FileManager.WriteAllText(fullCSVOutputFileName,str.join("\n",datFrec))
    