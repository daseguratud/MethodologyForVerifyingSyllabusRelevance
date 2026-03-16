import os
from FileManager import FileManager
from ui import ui
class Etapa02:
    def __init__(self, SyllabusPath,TextSylabusPath):
        self.file_path = SyllabusPath
        self.corpus_path = TextSylabusPath
    def Procesar(self):
        ui.printStageStart(2)
        for archivo in os.listdir(self.file_path):
            ui.printStageMessage(f"Procesando {archivo}...")
            fullfileName = os.path.join(self.file_path, archivo)
            fulltextFileName = os.path.join(self.corpus_path, archivo.replace('.pdf', '.txt'))
            FileManager.extract(fullfileName,fulltextFileName)
        ui.printStageFinish(2)
