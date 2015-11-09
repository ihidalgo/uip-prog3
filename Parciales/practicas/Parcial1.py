#PARICAL1
#Autor: Ivan Hidalgo
#

class Planilla:
   nombre=""
   pago=0
   def nombrar(self,n): 
      self.nombrar=n
	  
estructura=Planilla()

for i in range (2):

   n=str(input("ingrese el nombre: "))
   pago=int(input("ingrese el salario: "))
   
#for i in range (2):

   print (estructura.nombrar)
