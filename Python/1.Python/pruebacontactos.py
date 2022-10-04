print("----------------")
print("Guardar contacto")
print("----------------")
nombre_1 = str(input("Digite el nombre: "))
apellido_1 = str(input("Digite el apellido: "))
telefono_1 = int(input("Digite el telefono movil: "))
telefono_2 = int(input("Digite el telefono fijo: "))
diccionario = {"nombre":nombre_1,"apellido":apellido_1,"telefonos":[telefono_1,telefono_2]}
print("----------------------")
print("Contaco guardado como:")
print("----------------------")
for claves,valores in diccionario.items():
    print(claves,valores)