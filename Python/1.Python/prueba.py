numero_binario = '1010110'

numero_decimal = 0 #aquí iremos sumando el resultado de cada multiplicación

for posicion, digito_string in enumerate(numero_binario[::-1]):
	numero_decimal += int(digito_string) * 2 ** posicion

print(f'El número decimal que buscamos es {numero_decimal}')