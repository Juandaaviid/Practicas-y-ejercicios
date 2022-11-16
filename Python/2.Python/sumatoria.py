import math
print("Sumatoria de n numeros \n")
limite = int(input("ingrese el limite de la sumatoria: "))
x=0
for i in range(1,limite+1,1):
    x += (i+3)-(((i**4)+2*i)/i)
print(x)