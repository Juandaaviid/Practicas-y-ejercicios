import math
def principal():
    print("Hallar el angulo y la magnitud de un vector conociendo sus componentes para el primer y segundo cuadrante\n")
    x = float(input("Ingrese la cordenada en x del vector: "))
    y = float(input("Ingrese la cordenada en y del vector: "))
    return x,y
def calculos(x,y):
    magnitud = math.sqrt((x**2)+(y**2))
    angulo_rad = math.atan(y/x)
    angulo_gra = angulo_rad*(180/math.pi)
    return(magnitud,angulo_rad,angulo_gra)
