import os
import PyPDF2
class FileManager:
    def __init__(self):
        pass
    @staticmethod
    def WriteAllText(filename, text):
        with open(filename, "w", encoding="utf-8") as archivo_texto:
            archivo_texto.write(text)
    @staticmethod
    def ReadAllText(filename):
        with open(filename, "r", encoding="utf-8") as archivo_texto:
            return archivo_texto.read()
    @staticmethod
    def extract(origen, destino=None):
        with open(origen, "rb") as archivo_pdf:
            lector = PyPDF2.PdfReader(archivo_pdf)
            texto=''  
            for pagina in lector.pages:
                texto += pagina.extract_text()
            if destino!=None:
                FileManager.WriteAllText(destino, texto)
            return texto 
        
    @staticmethod
    def extractRange(origen, destino, paginaInicial, cantidadPaginas):
        with open(origen, "rb") as archivo_pdf:
            lector = PyPDF2.PdfReader(archivo_pdf)
            texto=''
            for npagina in range(paginaInicial, paginaInicial+cantidadPaginas):
                texto += lector.pages[npagina-1].extract_text()           
            FileManager.WriteAllText(destino, texto)
            return texto 
    @staticmethod
    def FileExists(filename):
        return os.path.exists(filename)

