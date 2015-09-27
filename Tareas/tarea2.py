#TAREA2
#Autor: Ivan Hidalgo
#
#Instrucciones:Crear un programa en Python que resuelva el siguiente problema de fisica: 
#Una ambulancia se mueve con una velocidad de 120 km/h y necesita recorrer un tramo recto de 60km.
#Calcular el tiempo necesario, en segundos, para que la ambulancia llegue a su destino. La formula a utilizar es: velocidad = distancia / tiempo.


velocidad  =  120                   
distancia = 60

tiempo_h = distancia / velocidad    #calcula  el  tiempo en horas
tiempo_m = tiempo_h * 60            #calcula  el  tiempo en minutos
tiempo_s = tiempo_m * 60            #calcula  el  tiempo en segundos

print ("El tiempo necesario para que la ambulancia llegue a su destino es : " + str(tiempo_s) + "s") 
 

