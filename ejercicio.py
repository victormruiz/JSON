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
		print("El número total de convenios es",len(datos["convenios"])
	print("Elige una opción: ")
	print("1.- ejercicio 1: ")
	print("2.- ejercicio 2: ")
	print("3.- ejercicio 3: ")
	print("4.- ejercicio 4: ")
	print("5.- ejercicio 5: ")
	print("0.- salir: ")
	opcion=int(input("¿opcion?: "))
