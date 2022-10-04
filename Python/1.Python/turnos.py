import json
agenda = {
    '9':{'nombre':'Juan','Ocupado':False},
    '2':{'nombre':'Pedro','Ocupado':False},
    '7':{'nombre':'Jose','Ocupado':False},
    '8':{'nombre':'Maria','Ocupado':False},
    '4':{'nombre':'Lucia','Ocupado':False}
    }

with open('turnos.json','w') as file:
    json.dump(agenda,file,indent=4)

with open('turnos.json') as file:
    agendajson=json.load(file)