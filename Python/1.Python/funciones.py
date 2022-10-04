# ESTA FUNCION SIRVE PARA SUMAR DOS NUMEROS
def funcionsuma(numero1, numero2):
    resultado=numero1+numero2
    print(f"El resultado de la suma es {resultado}")
    return resultado

# ESTA FUNCION SIRVE PARA RESTAR DOS NUMEROS
def funcionresta(numero1, numero2):
    resultado=numero1-numero2
    print(f"El resultado de la resta es {resultado}")
    return resultado

num1=int(input("Escriba el numero 1: "))
num2=int(input("Escriba el numero 2: "))
funcionsuma(num1,num2)
funcionresta(num1,num2)
