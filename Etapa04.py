from TextProcessor import TextProcessor
from FileManager import FileManager
from ui import ui
import os
class Etapa04:    
    def __init__(self,languageProcessWorkingPath,
                 syllabusTextPath,booksContentsTextPath,
                 ConsolidatedSyllabusFile, ConsolidatedReferencesFile
                 ):
        self.languageProcessWorkingPath = languageProcessWorkingPath
        self.syllabusTextPath = syllabusTextPath
        self.booksContentsTextPath = booksContentsTextPath
        self.ConsolidatedSyllabusFile = ConsolidatedSyllabusFile
        self.ConsolidatedReferencesFile = ConsolidatedReferencesFile
        self.__updateFilesList()
        self.textProcessor = TextProcessor()
    def __updateFilesList(self):
        self.__FilesList = []
        self.__syllabus=os.listdir(self.syllabusTextPath)
        self.__references=os.listdir(self.booksContentsTextPath)
        self.__FilesList.extend([os.path.join(self.syllabusTextPath, f) for f in self.__syllabus])
        self.__FilesList.extend([os.path.join(self.booksContentsTextPath, f) for f in self.__references])
    def Procesar(self):
        ui.printStageStart(4)
        self.__updateFilesList()
        for fileName in self.__FilesList:
            if os.path.isfile(fileName):
                ui.printStageMessage(f"Processing file: {os.path.basename(fileName)} ")
                content = FileManager.ReadAllText(fileName)        
                content=self.textProcessor.SolveSpetialCases(content)
                content=self.textProcessor.TranslateToTargetLanguage(content)
                content=self.textProcessor.ToLowerCase(content)
                content=self.textProcessor.TerminologyUnification(content)
                content=self.textProcessor.CleanNumbersFromText(content)
                content=self.textProcessor.CleanPunctuationFromText(content)
                content=self.textProcessor.RemoveExtraBlancks(content)
                FileManager.WriteAllText(os.path.join(self.languageProcessWorkingPath,"IntermediateFiles",os.path.basename(fileName)),content)
        self.__Consolidar()
        self.__CrerateWordCloud()
        ui.printStageFinish(4)
    def __CrerateWordCloud(self):
        ui.printStageMessageSubProcess("Creating wordcloud...")
        syllabusCorpusFile = os.path.join(self.languageProcessWorkingPath,self.ConsolidatedSyllabusFile)
        syllabusCorpus = FileManager.ReadAllText(syllabusCorpusFile)
        self.textProcessor.CreateWordCloud(syllabusCorpus,syllabusCorpusFile.replace(".txt",".csv"))
        
        referenceCorpusFile = os.path.join(self.languageProcessWorkingPath,self.ConsolidatedReferencesFile)
        referenceCorpus = FileManager.ReadAllText(referenceCorpusFile)
        self.textProcessor.CreateWordCloud(referenceCorpus,referenceCorpusFile.replace(".txt",".csv"))
        ui.printStageMessageSubProcess("Wordcloud created.")
    def __Consolidar(self):
        self.__updateFilesList()
        ui.printStageMessageSubProcess("Consolidating processed files...")
        consolidatedSyllabusContent=""
        consolidatedReferenceContent=""
        for fileName in os.listdir(os.path.join(self.languageProcessWorkingPath,"IntermediateFiles")):
            originalName=fileName
            fileContent = FileManager.ReadAllText(os.path.join(self.languageProcessWorkingPath,"IntermediateFiles",fileName))
            if originalName in self.__syllabus:
                consolidatedSyllabusContent+=fileContent+"\n"
            elif originalName in self.__references:
                consolidatedReferenceContent+=fileContent+"\n"
        
        FileManager.WriteAllText(os.path.join(self.languageProcessWorkingPath,self.ConsolidatedSyllabusFile),consolidatedSyllabusContent)
        FileManager.WriteAllText(os.path.join(self.languageProcessWorkingPath,self.ConsolidatedReferencesFile),consolidatedReferenceContent)
        ui.printStageMessageSubProcess("Consolidation completed.")

