from TextProcessor import TextProcessor
from FileManager import FileManager
from UnifiedTerm import UnifiedTerm
from ui import ui
import os
class Etapa05:    
    def __init__(self,processWorkingPath,
                 syllabusTopicsFile,referenceTopicsFile
                 ):
        self.processWorkingPath = processWorkingPath
        self.syllabusTopicsFile = syllabusTopicsFile
        self.referenceTopicsFile = referenceTopicsFile
        self.textProcessor = TextProcessor()
    def Procesar(self):
        ui.printStageStart(5)
        self.__CreateUnifiedTable()
        ui.printStageFinish(5)
    def __CreateUnifiedTable(self):
        syllabusTerms = FileManager.ReadAllText(self.syllabusTopicsFile).splitlines()
        referenceTerms = FileManager.ReadAllText(self.referenceTopicsFile).splitlines()
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
        FileManager.WriteAllText(os.path.join(self.processWorkingPath,"UnifiedTable.csv"),texto)