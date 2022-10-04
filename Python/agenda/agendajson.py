import json
'''
agenda = {
    '9':{'nombre':'Juan','telefono':3156367367,'correo':'juan@uis.edu.co','direccion':'Calle 9 Cra 27','ciudad':'Bucaramanga'},
    '2':{'nombre':'Pedro','telefono':3206367367,'correo':'pedro@uis.edu.co','direccion':'Calle 8 Cra 21','ciudad':'Bogota'},
    '7':{'nombre':'Jose','telefono':3226367367,'correo':'jose@uis.edu.co','direccion':'Calle 7 Cra 22','ciudad':'Cali'},
    '8':{'nombre':'Maria','telefono':3506367367,'correo':'maria@uis.edu.co','direccion':'Calle 2 Cra 17','ciudad':'Medellín'},
    '4':{'nombre':'Lucia','telefono':3176367367,'correo':'lucia@uis.edu.co','direccion':'Calle 12 Cra 19','ciudad':'Barranquilla'}
    }

with open('agenda.json','w') as file:
    json.dump(agenda,file,indent=4)
'''

with open('agenda.json') as file:
    agendajson=json.load(file)

print("________________________________________________________________________________________________________")
print("| NOMBRE \t TELEFONOS \t\t\t CORREO \t\t DIRECCION \t CIUDAD         |")
print("|_______________________________________________________________________________________________________|")
for fila in agendajson.keys():
    print(f"{agendajson[fila]['nombre']} \t {agendajson[fila]['telefono']} \t {agendajson[fila]['correo']} \t {agendajson[fila]['direccion']} \t {agendajson[fila]['ciudad']}")

agendajson['8']['nombre']="Carlos"
agendajson['8']['telefono']="3502551222"
agendajson['8']['correo']="carlos@uis.edu.co"
agendajson['8']['direccion']="Calle 52 No. 21-23"
agendajson['8']['ciudad']="Cartagena"

with open('agenda.json','w') as file:
    json.dump(agendajson,file,indent=4)