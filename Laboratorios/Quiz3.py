#CLASE 5 quiz 3
#Autor: Ivan Hidalgo

for i in range (6): 
   segundos=int(input("Ingrese el valor en segundos: "))
   aux_segundos=segundos
   minuto=0
   for j in range (60):
      if aux_segundos>=60:
         aux_segundos= aux_segundos - 60 
         minuto=minuto+1
   
   print ("Los segundos faltantes para un minutos mas son " + str (60 - aux_segundos) + " segundos")
     
