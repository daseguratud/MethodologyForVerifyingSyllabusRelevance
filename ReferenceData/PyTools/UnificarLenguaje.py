from .Parameters import Parameters
from .FileHelper import FileHelper
from googletrans import Translator
import os
class UnificarLenguaje:
    @staticmethod
    def Traducir():
        FileHelper.CreatePath(Parameters.contenidosTraducidosPath)
        archivosOriginales = os.listdir(Parameters.contenidosOriginalesPath)
        for archivo in archivosOriginales:
            origen = Parameters.contenidosOriginalesPath+archivo
            destino =Parameters.contenidosTraducidosPath+archivo.replace("es","en")            
            if(archivo.find("es")>=0):                
                traduccion = UnificarLenguaje.__TraducirContenido(origen)
                FileHelper.WriteAllText(destino,traduccion)
            else:
                FileHelper.CopyFile(origen,destino)
    @staticmethod
    def __TraducirContenido(archivo):
        try:
            Contenido = FileHelper.ReadAllText(archivo)
            lineas=Contenido.splitlines()
            traductor = Translator()
            grupos=[]
            grupo=[]
            for i in range(0,len(lineas)):
                grupo.append(lineas[i])
                if i%50==0:                    
                    grupos.append(str.join("\n",grupo))
                    grupo=[]
            if len(grupo)>0: grupos.append(str.join("\n",grupo))
            traduccion=""
            for grupo in grupos:
                traduccion += traductor.translate(grupo,src="es",dest="en").text+"\n"
            return traduccion
        except Exception as ex:            
            print(f"Error en traduccion: {ex} en {archivo}")
            return ":("