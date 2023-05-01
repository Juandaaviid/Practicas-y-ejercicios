import numpy as np

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
determinante = np.linalg.det(A)
print(A)
print('El determinante de la matriz A es: ',determinante)
rango = np.linalg.matrix_rank(A)
print('El rango de la matriz A es: ',rango)
if rango !=10:
    print('Los vectores columna de A no son base de R^10')
else:
    print('Los vectores columna de A son base de R^10')