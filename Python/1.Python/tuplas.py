# Declaración de tuplas (tuple)
# Arreglos de datos estáticos, no pueden modificarse
tupla = ("lunes","martes","miercoles","jueves","viernes")
tupla = tuple(tupla)
tupla = tuple(["lunes","martes","miercoles","jueves","viernes"])
print(tupla)
print(type(tupla))
# Numero de elementos de la tupla
print(len(tupla))
# Numero de coincidencias en la tupla
print(tupla.count("miercoles"))
#Recorrer la tupla forma 1
for item in tupla:
    print(item)
#Recorrer la tupla forma 2
for i in range(len(tupla)):
    print(tupla[i])