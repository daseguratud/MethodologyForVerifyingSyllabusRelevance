class Parameters:
    contenidosOriginalesPath = "./01_Contenidos/"
    contenidosTraducidosPath = "./02_ContenidosTraducidos/"
    contenidosUnificadosPath = "./03_ContenidosConsolidados/"
    contenidosLimpiosPath = "./04_ContenidosLimpios/"
    nubePalabrasPath = "./05_NubeDePalabras/"
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
    