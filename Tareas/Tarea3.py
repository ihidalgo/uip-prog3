#TAREA3
#Autor: Ivan Hidalgo
#
#Escriba un programa en Python donde el usuario introduce un numero n y el programa 
#imprime los primeros n numeros triangulares, junto con su indice. Los numeros triangulares se originan
#de la suma de los numeros naturales desde 1 hasta n.
#Ecuacion  utilizada S n i=1  i=n*(n+1)/2


numero=int(input("ingrese un numero: "))
 
resultado={}
for i in range(1,numero+1):
   resultado[i]=(i*(i+1)/2)

for i in resultado:
print (i, resultado[i])

 

