#CLASE 5 Quiz3
#Autor: Ivan Hidalgo

segundos=int(input("ingrese  el valor en segundos: "))
minuto = 60


if segundos>=60:
   segundos_s= segundos - minuto

if segundos_s<60:
   segundos_f = minuto - segundos_s


print ("los segundos faltantes para un minutos es " + str (segundos_f) + " segundos")

