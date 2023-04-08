from io import open
from os import path

def escribir_archivo():
    archivo = open('texto.txt', 'w') #Se crea el archivo si no esta
    archivo.write('Este tema esta interesante y toca seguir aprendiendo') #Escribe en el archivo
    archivo.close() #Cierra la función

def leer_archivo():
    if path.isfile('texto.txt'): #valida si esta el archivo
        archivo = open('texto.txt', 'r') #Sirve para leer los archivos y si hay algo escrito no se modificara
        #textos = archivo.read()
        textos = archivo.readlines() #para que aparezcan como un diccionario
        archivo.close() #para cerrar el flujo que se abrio
        print(textos)
    else:
        print('El archivo no existe')

def agregar_datos():
        if path.isfile('texto.txt'): #valida si esta el archivo
            archivo = open('texto.txt', 'a') #Sirve para actuañizar los datos
            archivo.write('\notra linea') #lo que va agregar al archivo
            archivo.close() #para cerrar el flujo que se abrio
        else:
            print('El archivo no existe')

def modificar_datos():
        if path.isfile('texto.txt'): #valida si esta el archivo
            archivo = open('texto.txt', 'r+') #Sirve para actuañizar los datos
            texto = archivo.readlines()
            print(texto)
            texto[1] = 'esto es una modificación\n'
            #archivo.write('\notra linea') #lo que va agregar al archivo
            print(texto)
            archivo.seek(0) #Es metodo sirve para trabajar con el puntero
            archivo.writelines(texto)
            archivo.close() #para cerrar el flujo que se abrio
            print(texto)
        else:
            print('El archivo no existe')

#Esto eliminario todos los datos de una archivo
def eliminar_datos():
    archivo = open('texto.txt', 'w') #Se crea el archivo si no esta
    archivo.close() #Cierra la función

modificar_datos()
#agregar_datos()
#leer_archivo()
#escribir_archivo()