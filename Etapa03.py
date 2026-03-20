import os
from Book import Book
from FileManager import FileManager
from ui import ui
class Etapa03:
    def __init__(self, RutaLibros, Rutacorpus):
        self.RutaLibros = RutaLibros
        self.Rutacorpus = Rutacorpus
        self.Books = [
            Book("01_Flyod.pdf", 12, 4),      
            Book("02_Julian.pdf", 8, 5),     
            Book("03_Ndjountche.pdf", 4, 3), 
            # Book("04_Tocci.pdf", 1, 10), # ERROR  
            Book("05_Morris.pdf", 8, 6),    
            Book("06_Adan.pdf", 5, 2),      
            Book("07_Wakerly.pdf", 7, 7),   
            Book("08_Zurek.pdf", 7, 2),     
            Book("09_Matin.pdf", 10, 6),     
            Book("10_Maini.pdf", 9, 14),     
            Book("11_Roth.pdf", 7, 8),      
            Book("12_Groote.pdf", 9, 4),    
            Book("13_Raychaudhuri.pdf", 7, 12),
            Book("14_Urquia.pdf", 5, 16),
            Book("15_El-Sheikh.pdf", 5, 5),
            Book("16_Mazumder.pdf", 6, 6),
            Book("17_Velasquez.pdf", 1, 15),
            Book("18_Guapacha.pdf", 8, 3),
            Book("19_LaMeres.pdf", 10, 7),
            Book("20_Ghosh.pdf", 8, 2),
            Book("21_Roy.pdf", 11, 10),
            Book("22_Kani.pdf", 12, 12),
        ]
    def Procesar(self):
        ui.printStageStart(3)
        for libro in self.Books:
            ui.printStageMessage(f"Procesando {libro.FileName}...")
            fullfileName = os.path.join(self.RutaLibros, libro.FileName)
            fullcorpusFileName = os.path.join(self.Rutacorpus, libro.FileName.replace('.pdf', '.txt'))
            FileManager.extractRange(fullfileName,fullcorpusFileName,libro.FromPage,libro.nPages)
        ui.printStageFinish(3)
    def ProcesarFromDirList(self):
        ui.printStageStart(3)
        archivos = os.listdir(self.RutaLibros)
        for archivo in archivos:
            ui.printStageMessage(f"Procesando {archivo}...")
            fullfileName = os.path.join(self.RutaLibros, archivo)
            ui.printStageMessage(f"Procesando {fullfileName}...")
            fullcorpusFileName = os.path.join(self.Rutacorpus, archivo.replace('.pdf', '.txt'))
            ui.printStageMessage(f"Procesando {fullcorpusFileName}...")
            FileManager.extract(fullfileName,fullcorpusFileName)
        ui.printStageFinish(3)
