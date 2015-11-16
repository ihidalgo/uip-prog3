import os
#PARCIAL1
#Autor: Ivan Hidalgo
#Este programa hace el calculo de la planilla de una empresa, generalmente se trabaja 104 horas por quincena y cada empleado puede tener una tarifa
#distinta por hora, se calcula pago de horas extras,impuestos, total a pagar, el empleado que mas gano, total a pagar a empleados de 55 años en adelante etc..

nombre=[]
edad=[]
valor_horas=[]
horas_trabajadas=[]
pago_bruto=[0,0,0,0,0,0,0,0,0,0]                               #Inicializando los elementos en 0. Nota: salia el error: indexerror list index out of range
horas_extras=[0,0,0,0,0,0,0,0,0,0]
phoras_extras=[0,0,0,0,0,0,0,0,0,0]
tpagar=[0,0,0,0,0,0,0,0,0,0]
impuestos=[0,0,0,0,0,0,0,0,0,0]
impuestos_horase=[0,0,0,0,0,0,0,0,0,0]
total_impuestos=[0,0,0,0,0,0,0,0,0,0]
neto=[0,0,0,0,0,0,0,0,0,0]
mayor=0
nombre1=""
total_55=0

for i in range (2):                                            #Se deja el ciclo de 2 para pruebas
   
   v_nombre= str(input("Ingrese el nombre del empleado " + str (i+1) +":")) #Se llena la lista nombre
   nombre.append(v_nombre)
   v_edad= int(input("Ingrese la edad:"))                                   #Se llena la lista edad
   edad.append (v_edad)
   v_horas=int(input("Ingrese la tarifa por horas: "))                     #Se llena la lista valor_horas
   valor_horas.append(v_horas)
   v_horast=int(input("Ingrese la cantidad de horas trabajadas: "))          #Se llena la lista horas_trabajadas
   horas_trabajadas.append(v_horast)
   
   
   
   
   if horas_trabajadas[i]>104:  #13 dias de trabajo = 104 horas
      
      pago_bruto[i] =  horas_trabajadas [i] * valor_horas [i]  #Calcula pago bruto
      horas_extras[i]  =  horas_trabajadas [i] - 104           #Calcula horas extras          
      phoras_extras[i] =  horas_extras[i]  * 1.50              #Calcula pago de horas extras
      tpagar[i] =  pago_bruto [i] + phoras_extras[i]           #Calcula el subtotal a pagar
      impuestos[i]  =  pago_bruto[i]  * 0.10                   #Calcula los impuestos
      impuestos_horase[i] =  phoras_extras[i] * 0.20           #Calcula los impuestos sobre las horas extras
      total_impuestos[i] = impuestos[i] + impuestos_horase[i]  #Calcula el total de impuestos a pagar
      neto[i] =  tpagar[i] - total_impuestos[i]                #Calcula el total a pagar (neto)
	  
   else: 
      pago_bruto[i] =  horas_trabajadas [i] * valor_horas [i]
      impuestos[i]  =  pago_bruto[i] * 0.10
      total_impuestos[i]  = total_impuestos[i] + impuestos[i] 
      neto[i] =  pago_bruto[i] - total_impuestos[i]
	  
   if i==0:                                                    #Se obtiene nombre y pago total  del empleado que mas devengo  
              
      mayor     = neto[i]
      nombre1   = nombre[i]   
           
    
   elif mayor<neto[i]:
                   
      mayor     = neto[i]
      nombre1   = nombre[i]
   
   if  edad [i]>=55:                                           #Se obtiene el pago total de los empleados con 55 años en adelante
         
      total_55+=neto[i]	  
             
   os.system('cls')                                            #Limpiar pantalla
for i in range (2):                                            #Ciclo para imprimir resultados
   
   print ("Nombre"  "|" "    "  "Edad" "|" "   "  "Tarifa por hora" "|" "   "  "Horas trabajadas" "|" "   "  " Total Impuesto" "|" "   "  "Total a Pagar")     
   print (nombre[i],"   " ,edad[i],"    ",valor_horas[i],"                ",horas_trabajadas[i],"                   ",total_impuestos[i],"          ", neto[i])  
print ("El pago total para los empleados de 55 años en adelante =", total_55, "$")
print ("El empleado que mas gano es",nombre1," ",mayor, "$")
