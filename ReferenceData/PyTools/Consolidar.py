import os
from .Parameters import Parameters
from .FileHelper import FileHelper
class Consolidar:
    @staticmethod
    def UnirArchivos():
        nombreArchivos = Consolidar.__ListarArchivos()
        Consolidar.__ClearOutputPutFile()
        for nombreArchivo in nombreArchivos:
            with open(Parameters.contenidosTraducidosPath+nombreArchivo,'r',encoding="utf-8") as archivo:
                contenido = f"\n->**********************************{nombreArchivo}\n{archivo.read()}"
                Consolidar.__AppendOutputFile(contenido)
    
    @staticmethod
    def __ListarArchivos():
        listado = os.listdir(Parameters.contenidosTraducidosPath)
        listado.sort()
        return listado
    @staticmethod
    def __AppendOutputFile(contenido):
        if not os.path.exists(Parameters.contenidosUnificadosPath):
            os.makedirs(Parameters.contenidosUnificadosPath)
        with open(Parameters.getOutFileConsolidados(),"a",encoding="utf-8") as file:
            file.write(contenido)
    @staticmethod
    def __ClearOutputPutFile():
        FileHelper.CreatePath(Parameters.contenidosUnificadosPath)
        FileHelper.CreateFile(Parameters.getOutFileConsolidados())