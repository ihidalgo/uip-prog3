#CLASE 3 quiz 1
#Autor: Ivan Hidalgo
#
#Instrucciones: Calcular el  area  y perimetro de un retangulo base  y la altura  de 5 cm  y  7 cm respespectivamente.
#Ademas  convertir area y prerimetro  a metros  y pulgadas.


base = 5
altura = 7

area = base * altura        
perimetro = base*2 + altura*2 

area_metro   =   area / 100     
area_pulgadas =  area * 0.39370

perimetro_metro   =   perimetro / 100
perimetro_pulgadas =  perimetro * 0.39370

print ("el area es " + str(area))
print ("El perimetro es " +str(perimetro))
print ("area  a metros " + str(area_metro))
print ("Area a pulgadas " +str (area_pulgadas))
print ("perimetro a metros " +str (perimetro_metro))
print ("perimetro a pulgadas " +str (perimetro_pulgadas))


