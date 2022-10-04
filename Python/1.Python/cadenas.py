palabra= "PYTHON"

#BUSQUEDA DE CARACTERES

print(palabra[0])
print(palabra[1])
print(palabra[2])
print(palabra[3])
print(palabra[4])
print(palabra[5])
print(palabra[2:6])
print(palabra[1:])
print(palabra[:2])

#SABER SI UNA PALABRA ESTA EN MAYUSCULAS

print(palabra.isupper())

#SABER SI UNA PALABRA ESTA EN MINUSCULAS
print(palabra.islower())

#SABER SI UNA PALABRA EMPIEZA CON DETERMINADA LETRA
print(palabra.startswith('P'))

#REMPLAZAR CARACTERES
print(palabra.replace('H','T'))

#CONTAR EL NUMERO DE VECES QUE ESTA DETERMINADO CARACTER
print(palabra.count('n'))

#SABER SI UNA PALABRA TERMINA CON DETERMINADA LETRA
print(palabra.endswith('N'))

#EN QUE POSICION ESTA DETERMINADO CARACTER
print(palabra.find('N'))

#EN QUE POSICION ESTA DETERMINADO CARACTER O ALGO ASI
print(palabra.index('Y'))

#TAMAÑO DE LA PALABRA
print(len(palabra))