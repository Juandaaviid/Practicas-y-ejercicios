#esctructura de un diccionario
diccionario = {"azul","rojo","negro","verde","amarillo","blanco"}
print(diccionario)
#print(type(diccionario))
#Estructura de una lista
lista = ["azul","rojo","negro","verde","amarillo","naranja"]
print(lista)
#print(type(lista))
#Estructura de una tupla
tupla = ("azul","rojo","negro","verde","amarillo","rojo")
print(tupla)
#print(type(tupla))

#Tamaño de la tupla
print(len(tupla))
#Recorrer tuplas forma 1
for item in tupla:
    print(item)
#Recorrer tuplas forma 2
for i in range(len(tupla)):
    print(tupla[i])
#Encontrar el numero de veces que existe un elemento en la tupla
print(tupla.count("rojo"))

tupla=list(tupla)
print(tupla)
print(type(tupla))

lista=tuple(lista)
print(lista)
print(type(lista))
