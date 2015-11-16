#-------------------------------------------------------------------------------
# Name:  Sumar Datos de Una Lisa
#
# Author: Cristian Torres
#-------------------------------------------------------------------------------
class Lista:
   lista=[]
   suma=0
   def llenarlista(self):
       x= int (raw_input("Ingrese Tamaño De La Lista:"))
       for i in range(x):
           #llenar lista
           self.lista.append(int(raw_input("Ingrese Numero:")))
       #imprimir lista
       for i in self.lista:
           print i
 
   def sumar(self):
       for i in self.lista:
           self.suma+= i
       print "La Suma De Los Datos Es:",self.suma
 
obj = Lista()
obj.llenarlista()
obj.sumar()