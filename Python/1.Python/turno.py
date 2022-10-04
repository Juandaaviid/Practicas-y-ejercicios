import json
'''
#GENERO EL DICCIONARIO
turnos = {
    1:{'cubiculo':1,'nombre':'Juan Perez','ocupado':False},
    2:{'cubiculo':2,'nombre':'Pedro Martinez','ocupado':False},
    3:{'cubiculo':3,'nombre':'Jose Feliciano','ocupado':False},
    4:{'cubiculo':4,'nombre':'Maria Rodriguez','ocupado':False},
    5:{'cubiculo':5,'nombre':'Lucia Fernandez','ocupado':False}
    }
#GRABO EL DICCIONARIO
with open('turnos.json','w') as file:
    json.dump(turnos,file,indent=4)
'''
#LEO EL DICCIONARIO GUARDADO
with open('turnos.json') as file:
    turnojson=json.load(file)

#REALIZO ALGUN CAMBIO EN EL DICCIONARIO
asignar=input("Escriba un numero de asesor para asignar: (1-5)")
for clave in turnojson.keys():
    if asignar==clave:
        turnojson[asignar]['ocupado']=True

#turnojson['3']['ocupado']=True

#VOLVEMOS A GRABAR EL ARCHIVO JSON CON LOS CAMBIOS
with open('turnos.json','w') as file:
    json.dump(turnojson,file,indent=4)