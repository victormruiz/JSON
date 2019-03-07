import json
with open("convenios.json") as fichero:
	datos=json.load(fichero)

print("Elige una opción: ")
print("1.- ejercicio 1: ")
print("2.- ejercicio 2: ")
print("3.- ejercicio 3: ")
print("4.- ejercicio 4: ")
print("5.- ejercicio 5: ")
print("0.- salir: ")
opcion=int(input("¿opcion?: "))

while opcion >= 0:
	if opcion == 1:
		for convenio in datos["convenios"]:
			print("el convenio con numero de expediente",convenio["numeroexpediente"],convenio["vigente"],"está vigente")
	elif opcion == 2:
		print("El número total de convenios es",len(datos["convenios"]))
	elif opcion == 3:
		fecha=input("Escribe una posible fecha de aprobacion (ej: 28/12/2010): ")
		for convenio in datos["convenios"]:
			if convenio["fechaaprobacion"] == fecha:
				print("el numero de inscripcion asociado con esa fecha es",convenio["numeroinscripcion"])
	elif opcion == 4:
		numinsc=input("Escribe un número de inscripción: ")
		print("Las entidades que corresponden a ese numero de inscripción son:")
		for convenio in datos["convenios"]:
			if convenio["numeroinscripcion"] == numinsc:
				print(convenio["entidades"][0]["entidad"])
	elif opcion == 5:
		lista=[]
		area=input("Escribe un area: ")
		print("Estos son los titulos de los convenios asociados a ese area:")
		print(" ")
		for convenio in datos["convenios"]:
			if convenio["area"] == area:
				print("- "+convenio["titulo"].lower())

	print("Elige una opción: ")
	print("1.- ejercicio 1: ")
	print("2.- ejercicio 2: ")
	print("3.- ejercicio 3: ")
	print("4.- ejercicio 4: ")
	print("5.- ejercicio 5: ")
	print("0.- salir: ")
	opcion=int(input("¿opcion?: "))
