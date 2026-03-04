class Parameters:
    contenidosOriginalesPath = "./01_Contenidos/"
    contenidosUnificadosPath = "./02_ContenidosConsolidados/"
    contenidosLimpiosPath = "./03_ContenidosLimpios/"
    nubePalabrasPath = "./04_NubeDePalabras/"
    contenidosUnificadosFile = "Contenidos.txt"
    nubePalabrasFileFrec = "Frecuencies.csv"
    nubePalabrasFileImg = "Frecuencies.png"
    @staticmethod
    def getOutFileConsolidados(): 
        return f"{Parameters.contenidosUnificadosPath}{Parameters.contenidosUnificadosFile}"    
    @staticmethod
    def getOutFileTraducidos(): 
        return f"{Parameters.contenidosTraducidosPath}{Parameters.contenidosUnificadosFile}"    
    @staticmethod
    def getOutFileLimpios(): 
        return f"{Parameters.contenidosLimpiosPath}{Parameters.contenidosUnificadosFile}"
    @staticmethod
    def getOutFileNubePalabrasFrec(): 
        return f"{Parameters.nubePalabrasPath}{Parameters.nubePalabrasFileFrec}"
    @staticmethod
    def getOutFileNubePalabrasImg(): 
        return f"{Parameters.nubePalabrasPath}{Parameters.nubePalabrasFileImg}"
    