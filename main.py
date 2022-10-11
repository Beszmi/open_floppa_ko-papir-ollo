import rockpaperscissors
import os
import autorps

config_file='config.txt'
if os.path.exists(config_file):
    if os.path.isfile(config_file):
        while True:
            olvas=input("Szeretnél a legutóbb megjegyzettek szerint játszani? igen/nem")
            if olvas=="igen":
                with open(config_file, "r") as config:
                    auto=str(config.readline())
                    rep=str(config.readline())
                    print(auto)
                    break
            elif olvas=="nem":
                os.remove(config_file)
                break
            else:
                print("Kérlek csak nemmel vagy igennel válaszolj")
                print(olvas)
else:
    olvas="nem"
if olvas=="nem":
    while True:
        config_input=(input("automatikus vagy manuális játékot szeretnél?"))
        if config_input=="automatikus":
            config_meny=str(input("Hány játékot játszon le automatikusan?"))
            rep=int(config_meny)
        mem = input("Elszeretnéd menteni legközelebbre? igen/nem")
        if mem=="igen":
            with open(config_file, 'w') as config:
                if config_input=="automatikus":
                    config.write("auto=1\nr="+config_meny)
                    auto="auto=1"
                elif config_input=="manuális":
                    config.write("auto=0")
                    auto="auto=0"
            break
        elif mem=="nem":
            if config_input=="automatikus":
                auto="auto=1"
                break
            else:
                auto="auto=0"
                break
        else:
            print("Csak igennel vagy nemmel válaszolj")
print(auto)
if auto=="auto=1":
    statok = autorps.rpsa(rep)
    print("Az első játékos", statok[0], " játékot nyert", statok[1], " döntetelene volt", " és", statok[2], " játékot veszített")
elif auto=="auto=0":
    statok=rockpaperscissors.rps(az:=input("Válassz: (ékezetes legyen és kisebetűs legyen!)"))
    print(statok[0]," játékot nyertél", statok[1]," döntetelened volt", " és",statok[2]," játékot veszítettél")
else:
    print("bruh")

if statok[0]==0:
    win_rate=0
else:
    win_rate=statok[0]/(statok[1]+statok[2])

szazalek=win_rate*100
print("Nyerési százalékod ",szazalek,"% volt")
