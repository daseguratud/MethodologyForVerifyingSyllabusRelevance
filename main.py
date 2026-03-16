import os
from SyllabusRelevanceVerifier import SyllabusRelevanceVerifier
from ui import ui
try:
    os.system('cls')
    stv = SyllabusRelevanceVerifier()
    stv.Run()
except Exception as e:
    ui.printError(e)
    input()