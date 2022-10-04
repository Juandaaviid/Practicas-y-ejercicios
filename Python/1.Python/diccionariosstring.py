#Ejemplo del uso de join
paises = ['Argentina', 'Uruguay', 'Chile', 'Paraguay', 'Brasil', 'Bolivia']
# Si deseamos convertir esta lista en una cadena de texto, utilizaremos la función join de la siguiente manera:
paisesString = ','.join(paises)
#devolverá el siguiente resultado
#'Argentina,Uruguay,Chile,Paraguay,Brasil,Bolivia'

#Ejemplo del uso de split
nombreString = "Mi nombre es Edilberto"
nombreLista = nombreString.split()
#['Mi', 'nombre', 'es', 'Gabriel']

nombreString = "Fulano  Mengano Suntano"
nombreLista = nombreString.split(sep = '\t')
#['Fulano', 'Mengano', 'Suntano']