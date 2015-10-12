#TAREA3
#Autor: Ivan Hidalgo
#
#Dado un intervalo de tiempo en minutos, calcular los dias, horas y minutos correspondientes.


tiempo=int(input("Ingrese el tiempo en minutos: "))

if tiempo/1440>=0:   # 24 horas x 60 minutos= 1440 minutos
   dias = tiempo / 1440
   x = tiempo % 1440
   horas = x / 60
   minutos = x % 60

if tiempo==1440:
   tiempo=tiempo
   dias = 1
   horas = 24
   minutos= tiempo

print ("Tiempo Ingresado " + str(tiempo)+ " minutos")
print ("Equivalencia en dias " +str(dias))
print ("Equivalencia en horas " + str(horas))
print ("Minutos " +str (minutos))
