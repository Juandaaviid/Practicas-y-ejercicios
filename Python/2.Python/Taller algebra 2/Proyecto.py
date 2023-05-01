import numpy as np
'''
PROYECTO FINAL DE ALGEBRA LINEAL 2 
INTEGRANTES:
Danilo Alexander Duran Mejia - 2210405
Juan David Ruiz Higuera - 2211241
'''

def punto_1():
    opcion= str(input('Seleccione el inciso al cual desea acceder "a" o "c": '))
    if opcion == 'a':
        A = np.array([[1,5,13],[2,7,17],[3,11,19]])
        print(A)
        b = np.array([0,0,0])
        x = np.linalg.solve(A,b)
        print('Solucion= ', x)

        det = np.linalg.det(A)
        print('Determinante de A= ',det)
    elif opcion =='c':
        A=np.array ([[1 ,5 ,13] ,[2 ,7 ,17] ,[3 ,11 ,19]])
        print ( A)
        b=np.array ([0 ,0 ,0])
        x=np.linalg .solve(A,b)
        print (" Solucion=" , x)

        det=np.linalg .det(A)

        print (" Determinante de A=", det)

        Q, R = np.linalg .qr(A)

        print("")
        print (" matriz Q=")
        print(Q)
        print("")
        print ("Matriz R=",R)
def punto_2():
    A = np.array([
        [2,4,6,0,4,5,6,7,6,5],
        [7,1,0,0,6,3,4,1,8,8],
        [2,7,8,7,8,1,6,0,2,9],
        [0,7,3,6,8,1,7,1,1,6],
        [4,9,7,3,0,7,9,4,3,0],
        [9,4,6,2,6,2,2,9,6,9],
        [0,1,9,6,3,3,1,4,1,9],
        [0,2,7,6,4,6,9,8,7,5],
        [1,6,8,6,0,6,3,5,3,1],
        [7,1,1,7,5,2,2,9,7,8]])
    opcion= str(input('Seleccione el inciso al cual desea acceder "a", "b" o "c": '))
    if opcion == 'a':
        determinante = np.linalg.det(A)
        print(A)
        print('El determinante de la matriz A es: ',determinante)
        rango = np.linalg.matrix_rank(A)
        print('El rango de la matriz A es: ',rango)
        if rango !=10:
            print('Los vectores columna de A no son base de R^10')
        else:
            print('Los vectores columna de A son base de R^10')
    elif opcion == 'b':
        base_ort = np.linalg.qr(A)
        print('Una base ortonormal para A es: \n',base_ort)
    elif opcion == 'c':
        S = np.array([
        [2,4,6],
        [7,1,0],
        [2,7,8],
        [0,7,3],
        [4,9,7],
        [9,4,6],
        [0,1,9],
        [0,2,7],
        [1,6,8],
        [7,1,1]
        ])

        u = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        A = np.dot(S.T, S)
        b = np.dot(S.T, u)
        sub = np.linalg.solve(A, b)
        proy_u_en_W = np.dot(S, sub)
        print('La proyeccion del vector u sobre el subespacio W es: \n',proy_u_en_W)

def punto_5():
    print('punto 5')

opcion = int(input('Ingrese el punto del proyecto al que desea acceder.\n1.\n2.\n5.\nRespuesta: '))

if opcion == 1:
    punto_1()
elif opcion == 2:
    punto_2()
elif opcion == 5:
    punto_5()
