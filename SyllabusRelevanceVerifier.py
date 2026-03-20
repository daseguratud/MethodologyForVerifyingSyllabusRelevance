from Etapa02 import Etapa02
from Etapa03 import Etapa03
from Etapa04 import Etapa04
from Etapa05 import Etapa05
from ui import ui
import os

class SyllabusRelevanceVerifier:
    def __init__(self): 
        SyllabusPath = "Etapa 01/"
        SyllabusTextPath = "Etapa 02/"
        booksPath = "Etapa 03/Libros"        
        booksContentsTextPath = "Etapa 03/Corpus"
        languageProcessWorkingPath = "Etapa 04/"
        ConsolidatedSyllabusFile="SyllabusCorpus.txt"
        ConsolidatedReferencesFile="ReferenceCorpus.txt"

        AnalysisProcesssWorkingPath = "Etapa 05/"
        syllabusTermsFullFileName=os.path.join(languageProcessWorkingPath,"SyllabusCorpus.csv")
        referencesTermsFullFileName=os.path.join(languageProcessWorkingPath,"ReferenceCorpus.csv")


        self.etapa02 = Etapa02(SyllabusPath,SyllabusTextPath)
        self.etapa03 = Etapa03(booksPath,booksContentsTextPath)
        self.etapa04 = Etapa04(languageProcessWorkingPath,SyllabusTextPath,booksContentsTextPath,ConsolidatedSyllabusFile,ConsolidatedReferencesFile)
        self.etapa05 = Etapa05(AnalysisProcesssWorkingPath,syllabusTermsFullFileName,referencesTermsFullFileName)
    def Run(self): 
        ui.printTest()
        ui.printMainMessage("************************  INICIA PROCESO  ************************")
        # self.etapa02.Procesar()
        # self.etapa03.Procesar()
        self.etapa04.Procesar()        
        self.etapa05.Procesar()        
        ui.printMainMessage("***********************  PROCESO TERMINADO ***********************")
