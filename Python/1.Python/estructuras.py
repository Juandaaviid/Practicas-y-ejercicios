# Declaración de tuplas (tuple)
# Arreglos de datos estáticos, no pueden modificarse
tupla = ("lunes","martes","miercoles","jueves","viernes")
tupla = tuple(tupla)
tupla = tuple(["lunes","martes","miercoles","jueves","viernes"])
print(tupla)
print(type(tupla))

# Declaración de listas (list)
# Arreglos de datos que pueden ser repetidos y cambiar dinamicamente
lista = ["verde", "azul", "amarillo", "naranja", "negro", "rojo", "amarillo"]
lista = list(lista)
lista = list(["verde", "azul", "amarillo", "naranja", "negro", "rojo", "amarillo"])
print(lista)
print(type(lista))

# Declaracion de conjuntos (set)
# Arreglos de datos cuya caracteristica principal es que no pueden repetirse y se pueden cambiar dinamicamente
conjunto = ["verde", "azul", "amarillo", "naranja", "negro", "rojo", "verde"]
conjunto = set(conjunto)
conjunto = set(["verde", "azul", "amarillo", "naranja", "negro", "rojo"])
print(conjunto)
print(type(conjunto))

# Declaracion de diccionarios (dict)
# Arreglos de datos que se identifican mediante claves y no por indices
diccionario = {"nombre":"Pedro","cedula":1055455552,"telefonos":[3205367322,3166723677]}
diccionario = dict(diccionario)
diccionario = dict([("nombre","Pedro"),("cedula",1055455552),("telefonos",[3205367322,3166723677])])
print(diccionario)
print(type(diccionario))