from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
from .Parameters import Parameters
from .FileHelper import FileHelper
from .LimpiarTexto import LimpiarTexto
class NubePalabras:
    @staticmethod
    def CrearNube():
        FileHelper.CreatePath(Parameters.nubePalabrasPath)
        texto = FileHelper.ReadAllText(Parameters.getOutFileLimpios())
        stopWords = STOPWORDS.union(LimpiarTexto.LoadCustomStopWords())
        nube_palabras = WordCloud(
            stopwords= stopWords,
            width=800, height=400, 
            background_color='white', 
            colormap='viridis').generate(texto)
        frequencies = nube_palabras.words_
        nube_palabras.to_file(Parameters.getOutFileNubePalabrasImg())
        # plt.figure(figsize=(10, 5))
        # plt.imshow(nube_palabras, interpolation='bilinear')
        # plt.axis('off')
        # plt.show()
        datFrec=[]
        for frecuency in frequencies.items():
            data=f"{frecuency[0]},{frecuency[1]}"
            datFrec.append(data)
        FileHelper.CreateFile(Parameters.getOutFileNubePalabrasFrec())
        FileHelper.WriteAllText(Parameters.getOutFileNubePalabrasFrec(),str.join("\n",datFrec))
