año=2021
añolimite=2022
while año<=añolimite:
    print(f"Año: {año}")
    mes=1
    while mes <=12:
        print(f" Mes {mes}")
        limitedias=30
        if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
            limitedias=31
        if(mes==2):
            limitedias=28
        dia=1
        while dia <= limitedias:
            print(f"        Día: {dia}")
            dia=dia+1
        mes=mes+1
    año=año+1
