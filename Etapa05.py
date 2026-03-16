from TextProcessor import TextProcessor
from FileManager import FileManager
from ui import ui
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
        FileManager.ReadAllText(self.syllabusTopicsFile)
        FileManager.ReadAllText(self.referenceTopicsFile)
        ui.printStageFinish(5)