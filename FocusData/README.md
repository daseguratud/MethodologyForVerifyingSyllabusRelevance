# Archivos del proceso de analisis de contenidos de espacios académicos de fundamentos de sistemas digitales en los programas de la Universidad Distrital Francisco José de Caldas
En este repositorio se encuentra la evidencia del proceso realizado para el analisis del contenido de los syllabus de fundamentos de sistemas digitales realizado para el estudio de tematicas de los espacios académicos relacionados con sistemas digitales.
## Descripcion de archivos de python
* main.py:\
    Script para el procesmiento de los contenidos recolectados.

* Pytools:\
    Clases creadas poara el procesamiento de los archivos de los contenidos de los libros consultados.
    - LimpiarTexto.py:
        Este script lee el archivo consolidado, elimina los números del contenido al igual que las palabras contenidas en el archivo stopwords.csv y comvierte este contenido en minúsculas. El resultado queda en la carpeta de contenidos limpios.
    - NubePalabras.py:
        Crea la nuve de palabras basado en el archivo limpio. Depende de WordCloud (pip install wordcloud)
    - Parameters.py:
        Parametros necesarios para el experimento, como rutas y nombres de archivo.
## Descripcion de directorios
* 01_Contenidos\
    Carpeta con los archivos de los contenidos de los syllabus consultados.
