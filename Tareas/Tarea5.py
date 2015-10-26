#TAREA5
#Autor: Ivan Hidalgo
#
#Elaborar un programa en Python que encueste a 10 personas y las clasifique segun el deporte que practica.
#La lista de deportes validos son: Ajedrez, Atletismo, Baloncesto, Futbol, Karate, Natacion, Volleyball, Flag y Ping Pong. 
#Puede darse el caso que no le guste ninguno de los deportes anteriores. Si es asi, entonces se puede seleccionar la opcion Otros. 
#Al final el programa debe mostrar estadisticas de la encuesta e indicar cual es el deporte con mayor preferencia de los encuestados.


lista=["Ajedrez", "Atletismo", "Baloncesto", "Futbol", "Karate", "Natacion", "Volleyball", "Flag", "PingPong", "Otros"]

for j in range(10): # ciclo para imprimir los valores de la lista
   print (str(j+1)+" "+(lista[j]))
   if j==lista[9]:
      break        #finalizando ciclo
da=0 # inicializacion de variables que serviran como acumuladores
db=0 # da= deporte A, db= deporte B  y asi sucesivamente
dc=0 
dd=0 
de=0 
df=0 
dg=0 
dh=0 
di=0 
dj=0

for i in range (10):
   
   deporte_s=int(input("Seleccione el deporte de su preferencia indicando el numero: "))

   if deporte_s==1:
      
      da= da+1    #aculador

   elif deporte_s==2:
      
      db=db+1

   elif deporte_s==3:
      
      dc=dc+1

   elif deporte_s==4:
      
      dd=dd+1

   elif deporte_s==5:
      
      de=de+1

   elif deporte_s==6:
      
      df=df+1

   elif deporte_s==7:
      
      dg=dg+1

   elif deporte_s==8:
      
      dh=dh+1

   elif deporte_s==9:
      
      di=di+1

   elif deporte_s==10:
      
      dj=dj+1

   if da>db and da>dc and  da>dd and da>de   and da>df   and da>dg   and da>dh and da>di and da>dj:  
      preferido="Ajedrez"
      
   elif db>da and db>dc and  db>dd and db>de   and db>df   and db>dg   and db>dh and db>di and db>dj:  
      preferido="Atletismo"

   elif dc>da and dc>db and  dc>dd and dc>de   and dc>df   and dc>dg   and dc>dh and dc>di and dc>dj:  
      preferido="Baloncesto"
      
   
   elif dd>da and dd>db and  dd>dc and dd>de   and dd>df   and dd>dg   and dd>dh and dd>di and dd>dj:  
      preferido="Futbol"

   elif de>da and de>db and  de>dc and de>dd   and de>df   and de>dg   and de>dh and de>di and de>dj:  
      preferido="Karate"

   elif df>da and df>db and  df>dc and df>dd   and df>de   and df>dg   and df>dh and df>di and df>dj:  
      preferido="Natacion"    

   elif dg>da and dg>db and  dg>dc and dg>dd   and dg>de   and dg>df   and dg>dh and dg>di and dg>dj:  
      preferido="Volleyball"

   elif dh>da and dh>db and  dh>dc and dh>dd   and dh>de   and dh>df   and dh>dg and dh>di and dh>dj:  
      preferido="Flag"

   elif di>da and di>db and  di>dc and di>dd   and di>de   and di>df   and di>dg and di>dh and di>dj:  
      preferido="PingPong"

   elif dj>da and dj>db and  dj>dc and dj>dd   and dj>de   and dj>df   and dj>dg and dj>dh and dj>di:  
      preferido="Otros Deportes"

print ("El deporte con mayor preferencia de los encuestados es: "+ (preferido))
