agenda={
    0:{"nombre":"Pedro","telefonos":[6076335022,3163672367],"correo":"pedro@gmail.com","direccion":"Carrera 27 No. 56-08","ciudad":"Bucaramanga"},
    1:{"nombre":"Juan","telefonos":[6077346344,3153564636],"correo":"juan@gmail.com","direccion":"Calle 100 No. 24-09","ciudad":"Bogota"},
    2:{"nombre":"Luis","telefonos":[6076452032,3206456545],"correo":"luis@gmail.com","direccion":"Carrera 16 No. 56-02","ciudad":"Medellín"},
    3:{"nombre":"Maria","telefonos":[6076756633,3145367707],"correo":"maria@gmail.com","direccion":"Calle 45 No. 12-08","ciudad":"Cali"}          
    }

#Recorrer los items del diccionario por su clave
for items in agenda.keys():
    print(items)
#Recorrer los items del diccionario 0 por sus claves

for items in agenda[0].keys():
    print(items)
#Recorrer los items del diccionario por sus valores
for items in agenda.values():
    print(items)
#Recorrer los items de todos los diccionarios anidados
for indice in agenda.keys():
    for items in agenda[indice].values():
        print(items)
#Imprimimos una columna especifica del diccionario, usando tambien el metodo get    
for indice in agenda.keys():
    print(agenda[indice].get("nombre","No se encuentro ningun registro"))
    agenda[indice]["nombre"]
#Recorrer todo el diccionario por filas y por columnas
for fila in agenda.keys(): # 0,1,2,3
    for columna in agenda[fila].keys(): # nombre,telefono,correo,direccion,ciudad
        print(agenda[fila][columna])
#Por ejemplo acceder al correo de Juan
print(agenda[2]["correo"])
#Por ejemplo acceder a los telefonos de Maria
for telefonos in agenda[1]["telefonos"]:
    print (f"{telefonos}")
#Usar el metodo items() para recorrer de forma simultanea claves(keys) y valores(values)
for clave,valor in agenda[0].items():
    print(f"La clave es: {clave} y el valor es: {valor}")

'''
# Metodo ZIP para trabajo con diccionarios
contactos = zip(agenda.keys(), agenda.values())
print(type(contactos))
contactos = list(contactos)
print(contactos)
'''