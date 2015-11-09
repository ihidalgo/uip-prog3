#PARCIAL1
#Autor: Ivan Hidalgo
#Este programa hace el calculo de la planilla de una empresa, generalmente se trabaja 104 horas por quincena y cada empleado puede tener una tarifa
#distinta por hora, se calculan los impuestos, horas extras etc..

nombre=[]
edad=[]
valor_horas=[]
horas_trabajadas=[]
pago_bruto=[]
horas_extras=[]
phoras_extras=[]
tpagar=[]
impuestos=[]
impuestos_horase=[]
total_impuestos=[]
neto=[]


for i in range (3):
   
   v_nombre= str(input("Ingrese el nombre del empleado " + str (i+1) +" :")) #se llena la lista nombre
   nombre.append(v_nombre)
   v_edad= int(input("Ingrese la edad :"))                                   #se llena la lista edad
   edad.append(v_edad)
   v_horas=int(input("Ingrese el valor de las horas: "))                     #se llena la lista valor_horas
   valor_horas.append(v_horas)
   
   v_horast=int(input("Ingrese la cantidad de horas trabajadas: "))          #se llena la lista horas_trabajadas
   horas_trabajadas.append(v_horast)

"""   if horas_trabajadas[i]>104:  #13 dias de trabajo = 104 horas
      
      pago_bruto[i] = horas_trabajadas [i] * valor_horas [i]  #calcula pago bruto
      horas_extras[i]  =  horas_trabajadas [i] - 104          #calcula horas extras          
      phoras_extras[i] =  horas_extras[i]  * 1.50             #calcula pago de horas extras
      tpagar[i] =  pago_bruto [i] + phoras_extras[i]          #calcula el subtotal a pagar
      impuestos[i]  =  pago_bruto[i]  * 0.10                  #calcula los impuestos
      impuestos_horase[i] =  phoras_extras[i] * 0.20          #calcula los impuestos sobre las horas extras
      total_impuestos[i] = impuestos[i] + impuestos_horase[i] #calcula el total de impuestos a pagar
      neto[i] = tpagar[i] - total_impuestos[i]                #calcula el total a pagar (neto)
	  
   else: 
      pago_bruto[i] =  horas_trabajadas [i] * valor_horas [i]
      impuestos[i]  =  pago_bruto[i] * 0.10
      total_impuestos[i]  =  impuestos[i] 
      neto[i] = pago_bruto[i] - total_impuestos[i] """
    
   
#for i in range (3):  #para imprimir resultados
   #print (nombre[i],edad[i])   
print (nombre[0],edad[0])  
print (nombre[1],edad[1])  
print (nombre[2],edad[2])