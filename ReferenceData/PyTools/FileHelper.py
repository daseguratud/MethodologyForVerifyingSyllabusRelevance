import os
import shutil
class FileHelper:
    @staticmethod
    def CreatePath(path):
        if not os.path.exists(path):
            os.makedirs(path)
    @staticmethod
    def CreateFile(name):
        if os.path.exists(name):
            os.remove(name)
    @staticmethod
    def CopyFile(Origen,Destino):
        shutil.copy(Origen,Destino)
    @staticmethod
    def ReadAllText(Archivo):
        with open(Archivo,"r", encoding='utf-8') as file:
            contenido = file.read()
        return contenido
    @staticmethod
    def ReadAllLines(Archivo):
        with open(Archivo,"r", encoding='utf-8') as file:
            contenido = file.readlines()
        return contenido
    @staticmethod
    def WriteAllText(Archivo, Contenido):
        with open(Archivo,"w", encoding='utf-8') as file:
            file.write(Contenido)