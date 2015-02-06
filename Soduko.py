import numpy as np 

archivo = open("sodoku.txt","r")
archivo2 = open("sodoku2.txt","r")
def leeArchivo(nombre):
	for linea in nombre.readline():
		print sumaLineas(linea)

def sumaLineas(linea):
	contador = 0
	for x in linea:
		contador += x








	
"""matriz= np.array([lista1,lista2,lista3,lista4,lista5,lista6,lista7,lista8,lista9])
print(matriz)"""

leeArchivo(archivo2)
print "#####################"
leeArchivo(archivo)
