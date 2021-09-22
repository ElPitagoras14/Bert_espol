#Contexto 
from os import getcwd


def context(archivo):
    contxt = []
    file = open("resources/" + archivo, 'r', encoding="utf-8")
    contxt = file.readlines()[1]
    file.close()
    return contxt
