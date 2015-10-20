def menu():
	print ("Selecciona una opcion")
	print ("\t1 - Ingresar mensaje")
	print ("\t2 - Comparar mensaje")
	print ("\t3 - Guardar")
	print ("\t4 - Mostrar contador")
        #print ("\t5 - Salir")
 
while True:
        menu()
        opcionMenu=int(input("inserta un numero valor >> "))
        
        if opcionMenu=="1":
		print ("1")
		
	elif opcionMenu=="2":
		print ("2 ")
		 
	elif opcionMenu=="3":
		print ("3 ")

	elif opcionMenu=="4":
		print ("4 ")
	 
	elif opcionMenu=="5":
		break

	else:
		print ("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")
		