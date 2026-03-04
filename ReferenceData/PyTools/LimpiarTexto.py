from .Parameters import Parameters
from .FileHelper import FileHelper
class LimpiarTexto:
    stopwords=""
    @staticmethod
    def Limpiar():
        FileHelper.CreatePath(Parameters.contenidosLimpiosPath)
        FileHelper.CreateFile(Parameters.getOutFileLimpios())
        FileHelper.CopyFile(Parameters.getOutFileConsolidados(),Parameters.getOutFileLimpios())
        LimpiarTexto.__ProcessFileLines(LimpiarTexto.__LimpiaNumeros)
        LimpiarTexto.__ProcessFileLines(LimpiarTexto.__ToLower)
        # LimpiarTexto.stopwords = LimpiarTexto.LoadCustomStopWords()
        # print("->*********** Stopwords")
        # print(LimpiarTexto.stopwords)
        # LimpiarTexto.__ProcessFileLines(LimpiarTexto.__QuitaStopWords)
    @staticmethod
    def LoadCustomStopWords():
        lineas=FileHelper.ReadAllLines("stopwords.csv")
        stopwords = []
        for linea in lineas: 
            stopwords.append(linea.replace("\n",""))
        return stopwords 
    @staticmethod
    def __ProcessFileLines(function):
        lineas=FileHelper.ReadAllLines(Parameters.getOutFileLimpios())
        with open(Parameters.getOutFileLimpios(),'w+',encoding="utf-8") as destino:
            for linea in lineas:
                if(not linea.startswith('->')):
                    linea = function(linea)
                destino.write(linea)
    @staticmethod
    def __LimpiaNumeros(cadena):
        Numeros=['0','1','2','3','4','5','6','7','8','9','.']
        cadenaFinal=""
        for letra in cadena:
            try:
                Numeros.index(letra)
            except:
                cadenaFinal+=letra
        return cadenaFinal
    def __ToLower(cadena):       
        return str.lower(cadena)
    def __QuitaStopWords(cadena):        
        cadenaFinal = cadena
        for stopword in LimpiarTexto.stopwords:
            cadenaFinal=str.replace(cadenaFinal,stopword," ")
        return cadenaFinal