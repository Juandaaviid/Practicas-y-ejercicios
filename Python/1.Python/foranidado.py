añolimite=2022
for año in range(2021,añolimite+1,1):
    print(f"Año {año}")
    for mes in range(1,13,1):
        print(f"  Mes {mes}")
        limitedias=30
        if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
            limitedias=31
        if(mes==2):
            limitedias=28
        for dia in range(1,limitedias+1,1):
            print(f"    Dia {dia}")
