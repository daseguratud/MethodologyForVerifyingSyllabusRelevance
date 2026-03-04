# Metodología de verificación de la pertinencia de los contenidos de un espacio académico para una actualización curricular, empleando técnicas de procesamiento de lenguaje natural - MethodologyForVerifyingSyllabusRelevanc
Este repositorio contiene la evidencia del proceso desarrollado empleando técnicas de procesamiento de lenguaje natural para el análisis del contenido de los libros de referencia en el área de Fundamentos de Sistemas Digitales, así como el análisis del contenido de los syllabus seleccionados correspondientes a este espacio académico en la Universidad Distrital Francisco José de Caldas, el proceso busca establecer la pertinencia temática entre los espacios académicos de Fundamentos De Sistemas Digitales y la bibliografía actualizada.
Dicho proceso fue implementado en el marco del trabajo Emulador de circuitos digitales combinacionales y secuenciales basado en dispositivos SoC” - PPNFF-2025-2144 de la Universidad Distrital Francisco José de Caldas adscrito al Grupo de Investigación LIFAE.
Este repositotio se organiza en dos carpetas, una con la evidencia del proceso de los recursos bibliográficos y la otra para la evidencia de los contenidos bajo estudio.
## Contenidos bajo estudio
## Contenidos de referencia
## Descripcion de archivos de python
* main.py:\
    Script para el procesmiento de los contenidos recolectados.
* Pytools:\
    Clases creadas poara el procesamiento de los archivos de los contenidos de los libros consultados.
    - Consolidar.py:
        Une los archivos de la carpeta de contenidos en unso solo y lo deja en la  carpeta de salida.
    - LimpiarTexto.py:
        Este script lee el archivo consolidado, elimina los números del contenido al igual que las palabras contenidas en el archivo stopwords.csv y comvierte este contenido en minúsculas. El resultado queda en la carpeta de contenidos limpios.
    - NubePalabras.py:
        Crea la nuve de palabras basado en el archivo limpio. Depende de WordCloud (pip install wordcloud)
    - Parameters.py:
        Parametros necesarios para el experimento, como rutas y nombres de archivo.
    - UnificarLenguaje.py:
        Traduce las líneas del archivo consolidado. Depende del traductor de goolge en linea (pip install googletrans==4.0.0-rc1).
## Descripcion de directorios
* 01_Contenidos\
    Carpeta con los archivos de los contenidos de los libros consultados. El nombre del archivo es puesto con el siguiente patron: <indice>_<apellido primer autor>_<idioma en|es>.txt.
* 02_ContenidosTraducidos\
    La carpeta contiene los archivos de contenidos en ingles, los archivos que originalmente estaban en español son traducidos por medio de googletrans.
* 03_ContenidosConsolidados\
    En esta carpeta se encuentra un solo archivo consolidado con el contenido en ingles de todos los libros.
* 04_ContenidosLimpios\
    En esta carpeta está el archivo resultado de procesar el archivo consolidado de todos los contenidos en ingles. Parte del proceso está convertir este contenido a minúsculas y retirar las palabras y caracteres registrados en el archivo "stopwords.csv" 
