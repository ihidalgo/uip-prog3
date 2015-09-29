#CLASE 3 quiz 2
#Autor: Ivan Hidalgo

monto=float(input("ingrese el valor del monto: "))


if monto>= 500:
   descuento = monto * 0.30
   monto= monto - descuento
   
elif monto>=200 and monto<500:
   descuento = monto * 0.20
   monto=monto-descuento
   
elif monto>=100  and monto<200:
   descuento = monto * 0.10
   monto=monto-descuento
   
else:
   descuento = 0



print ("El descuento es por " + str(descuento) + "$" + " total a pagar es: " + str(monto)+"$")