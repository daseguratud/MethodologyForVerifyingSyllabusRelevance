import asyncio
import re
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from FileManager import FileManager
from Translator import Translator
from ui import ui
class TextProcessor:
    def __init__(self):
        self.stopWords=self.__LoadCustomStopWords()
        self.destLanguage='en'
        self.translator = Translator() 
    @staticmethod
    def __LoadCustomStopWords():
        lineas=FileManager.ReadAllText("stopwords.csv").splitlines()
        stopwords = []
        for linea in lineas: 
            stopwords.append(linea.replace("\n",""))
        return stopwords 
    def TranslateToTargetLanguage(self,text):
        return self.translator.Translate(text,self.destLanguage)
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
    def TerminologyUnification(self,text):
        normalizedText = text
        rulesText = FileManager.ReadAllText("NormalizationRules.rule")
        rules = rulesText.splitlines()
        for rule in rules:
            fields=rule.split("<-")
            lema = fields[0]
            variants = fields[1].split(';') 
            for variant in variants:
                normalizedText = re.sub(variant,lema,normalizedText,) 
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
    
    def CrossPlot(self, unifiedTerms, outputFileName, bacgroundImage,showWordCloud=False):
        x = [float(t.syllabusFrecuency) for t in unifiedTerms]
        y = [float(t.referenceFrecuency) for t in unifiedTerms]
        labels = [t.term for t in unifiedTerms]
        img = mpimg.imread(bacgroundImage)
        # plt.xscale("log")
        # plt.yscale("log")
        # plt.imshow(img,extent=[-0.05, 1.05, -0.05, 1.05], alpha=0.1)
        plt.grid(True, which="both")
        plt.scatter(x, y)
        for i in range(len(x)):
            plt.text(x[i], y[i], labels[i])
            # plt.text(x[i], y[i], "t"+str(i))
        plt.xlabel("Syllabus Frecuency Terms")
        plt.ylabel("Reference Frecuency Terms")
        
        
        plt.savefig(outputFileName, dpi=600)
        if showWordCloud:
            plt.show()