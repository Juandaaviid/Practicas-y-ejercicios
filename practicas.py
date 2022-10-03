import modulos
"""
#---DECLARACION MATCH---
Es como el switch case como en c++ pero en este caso utiliza match y case
ejemplo=int(input("Ingrese un numero del 1 al 4: "))

match ejemplo:
    case 1:
        print("Hola")
    case 2:
        print("Hola"*2)
    case 3:
        print("Hola"*3)
    case 4:
        print("Hola"*4)
"""
"""
#---TUPLAS---
Es una lista ordenada o un arreglo por decirlo asi, se pueden usar cualquier tipo de variables string, int,float, boolean, etc
ejemplo:

color=("rojo","azul","verde","morado","rojo","verde","negro","azul")
print(color)

#imprime determinado elemento de la tupla
print(color[1])

#actualizar una tupla: primero se convierte a lista, luego se modifican elementos y despues se convierte a tupla nuevamente
x = list(color)
x[1] = "marron"
color = tuple(x)
print(color)

#Desempaquetar tuplas
(red,blue,green) = color
print(red)

#Metodos de tuplas count() que cuenta la cantidad de veces que aparece un elemento, index() que encuentra la primera posicion del elemento deseado
color=("rojo","azul","verde","morado","rojo","verde","negro","azul")
print(color.count("rojo"))
print(color.index("azul"))
"""
"""
#---LISTAS---
Son como las tuplas pero mas flexible a la hora de declarar datos y no hay que convertirlas como las tuplas, se declara con []

numeros = [1,2,4,1,1,2,4,5,6,5]
meses = ["enero","abril","marzo","diciembre","noviembre"]
verdad = [True,False,False,False,True]
mixtos = ["Juan",1,True,1.9,0]
#print(mixtos)
#print(len(meses))

#Acceder a elementos de una lista
#print(meses[2])
#print(meses[1:4])#Un intervalo, tambien funciona en las tuplas

#Cambiar elementos de una lista
#numeros[2] = 7
#print(numeros)

#Metodos de las listas append() que agrega un elemento al final de la lista, remove() que elimina el elemento deseado
#meses.append("Febrero")
#print(meses)
#mixtos.remove(1.9)
#print(mixtos)
"""
"""
#---DICCIONARIOS---
Son más flexibles que las tuplas y que las listas, tambien recibe todo tipo de datos y se caracterizan en tener claves y valores, se puede duplicar un vlaor pero no una clave ejemplo:

varios={1: "Cadena", 2: False, 3: 12, 4: 1.2, 5: "Cadena", 2: "David"}
#print(varios)
#Tupla y lista anidada
tupla={"color": "azul", "edad": 18, "tupl": ("David", 2, True)}
lista={"color": "azul", "edad": 18, "tupl": ["Juan", 2, True]}
#print(tupla)
#print(lista)
#print(len(tupla))

#Para acceder a elementos de un diccionario, algunos metodos son keys() para las claves, values() para los valores, items() para convertir el diccionario en tupla y lista anidada
#print(varios.keys())
#print(tupla.values())
#print(varios.items())

#Cambiar elementos con el metodo update(), tambien sirve para añadir uno nuevo
#varios[2] = True
#print(varios)

#varios.update({2: False})
#print(varios)

#varios.update({6: 1234})
#print(varios)

#Eliminar elementos con pop() que elimina un elemento por medio de las claves, popitem()que elimina el ultimo valor, del, clear() que limpia todo el diccionario
#varios.pop(2)
#print(varios)

#varios.popitem()
#print(varios)

#varios.clear()
#print(varios)

#del varios[1]
#print(varios)
"""
"""
#---MODULOS---

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))

modulos.suma(num1, num2)
"""
"""
#-------------POO----------
#---Clases y objetos---

#Declaracion de clase, nombre primera mayuscula
class Carro():
    #declarar atributos de instancia, siempre se pone self
    def __init__(self):
        print("holaaa")
    #metodos
    def mensaje(self):
        print("holaaaa otra vez")
    def mensaje2(self):
        print("adios")

mensaje = Carro()
print(type(mensaje.__init__))
#acceder a los metodos
mensaje.mensaje()
mensaje.mensaje2()

class clase2:

    def __init__(self, numero):
        self.numero=numero
    def comparar(self):
        if self.numero > 0:
            print("el numero es porsitivo")
        elif self.numero < 0:
            print("el numero es negativo")
        elif self.numero == 0:
            print("el numero es cero")
    def ciclo(self):
        while self.numero <= 10:
            print(self.numero)
            self.numero += 1

ejemplo = clase2(0)
ejemplo.comparar()
ejemplo.ciclo()
#ejemplo = clase2(int(input("Dame un numero:")))
#ejemplo.ciclo()
"""