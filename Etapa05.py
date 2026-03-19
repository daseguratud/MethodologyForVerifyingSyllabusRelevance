from TextProcessor import TextProcessor
from FileManager import FileManager
from UnifiedTerm import UnifiedTerm
from ui import ui
import matplotlib.pyplot as plt
import os
class Etapa05:    
    def __init__(self,processWorkingPath,
                 syllabusTopicsFile,referenceTopicsFile
                 ):
        self.__processWorkingPath = processWorkingPath
        self.__syllabusTopicsFile = syllabusTopicsFile
        self.__referenceTopicsFile = referenceTopicsFile
        self.__unifiedTableFile=os.path.join(self.__processWorkingPath,"UnifiedTable.csv")
        self.__unifiedTablePlotFile=self.__unifiedTableFile.replace(".csv",".jpg")
        self.__unifiedTabletoMostFile=self.__unifiedTableFile.replace(".csv","TopMost.csv")
        self.__unifiedTabletoImageile=os.path.join(self.__processWorkingPath,"BackGround.png")
        self.__textProcessor = TextProcessor()
            
    def Procesar(self):
        ui.printStageStart(5)
        UnifiedTerms= self.__CreateUnifiedTable()
        UnifiedTerms= self.__TopMost(UnifiedTerms,20)
        self.__textProcessor.CrossPlot(UnifiedTerms, self.__unifiedTablePlotFile,self.__unifiedTabletoImageile,True)
        ui.printStageFinish(5)
    
    def __TopMost(self,UnifiedTerms,TopMost):
        if TopMost<=0 : return UnifiedTerms
        resultado=[]
        ordenados = sorted(UnifiedTerms, key=lambda t: t.syllabusFrecuency,reverse=True)
        top= len(ordenados) if len(ordenados)<TopMost else TopMost
        resultado=ordenados[:top]

        ordenados = sorted(UnifiedTerms, key=lambda t: t.referenceFrecuency,reverse=True)
        top= len(ordenados) if len(ordenados)<TopMost else TopMost
        ordenados=ordenados[:top]
        for termino in ordenados:
            foundedTerm =[r for r in resultado if r.term==termino]
            existTerm = len(foundedTerm)>0
            if(not existTerm):
                resultado.append(termino)    
        FileManager.WriteAllText(self.__unifiedTabletoMostFile,str.join("\n",[str(r) for r in resultado]))    
        return resultado

    def __CreateUnifiedTable(self):
        syllabusTerms = FileManager.ReadAllText(self.__syllabusTopicsFile).splitlines()
        referenceTerms = FileManager.ReadAllText(self.__referenceTopicsFile).splitlines()
        UnifiedTerms = []
        for term in syllabusTerms:
            fields = term.split(';')
            fields.append("0")
            newRow = UnifiedTerm(*fields)
            UnifiedTerms.append(newRow)
        for term in referenceTerms:
            fields = term.split(';')
            foundedTerm =[t for t in UnifiedTerms if t.term==fields[0]]
            existTerm = len(foundedTerm)>0
            if(existTerm):
                foundedTerm[0].referenceFrecuency=fields[1]
            else:
                newRow = UnifiedTerm(fields[0],"0",fields[1])
                UnifiedTerms.append(newRow)
        
        texto = str.join("\n",[str(t) for t in UnifiedTerms])
        FileManager.WriteAllText(self.__unifiedTableFile,texto)
        return UnifiedTerms
