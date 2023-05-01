import numpy as np

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