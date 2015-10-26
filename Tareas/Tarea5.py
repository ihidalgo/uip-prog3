#TAREA5
#Autor: Ivan Hidalgo
#
#Elaborar un programa en Python que encueste a 10 personas y las clasifique segun el deporte que practica.
#La lista de deportes validos son: Ajedrez, Atletismo, Baloncesto, Futbol, Karate, Natacion, Volleyball, Flag y Ping Pong. 
#Puede darse el caso que no le guste ninguno de los deportes anteriores. Si es asi, entonces se puede seleccionar la opcion Otros. 
#Al final el programa debe mostrar estadisticas de la encuesta e indicar cual es el deporte con mayor preferencia de los encuestados.


lista=["Ajedrez", "Atletismo", "Baloncesto", "Futbol", "Karate", "Natacion", "Volleyball", "Flag", "PingPong", "Otros"]

for j in range(10):
   print (str(j+1)+" "+(lista[j]))
   if j==lista[9]:
      break 

for i in range (3):
   aux="nada"
   deporte_s=int(input("Seleccione el deporte de su preferencia: "))

   if deporte_s==1:
      da=0
      da=da+1

   elif deporte_s==2:
      db=0
      db=db+1

   elif deporte_s==3:
      dc=0
      dc=dc+1

   elif deporte_s==4:
      dd=0
      dd=dd+1

   elif deporte_s==5:
      de=0
      de=de+1

   elif deporte_s==6:
      df=0
      df=df+1

   elif deporte_s==7:
      dg=0
      dg=dg+1

   elif deporte_s==8:
      dh=0
      dh=dh+1

   elif deporte_s==9:
      di=0
      di=di+1

   elif deporte_s==10:
      dj=0
      dj=dj+1

   elif da>db and da>dc and  da>dd and da>de   and da>df   and da>dg   and da>dh and da>di and da>dj:  
      preferido="Ajedrez"
      
      
   elif db>da and db>dc and  db>dd and db>de   and db>df   and db>dg   and db>dh and db>di and db>dj:  
      preferido="Atletismo"
      
     
#print ("El deporte con mayor preferencia de los encuestados es "+ (preferido))   