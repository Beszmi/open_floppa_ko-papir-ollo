
import random
again=False
elso=True
win=0
loss=0
draw=0

while elso==True or again==True:
    elso=False
    lehet=["kő","papír","olló"]
    valasz=random.choice(lehet)
    tied=""
    while tied=="" or rossz==1:
        tied=input('Válassz: (ékezetes legyen és kisebetűs legyen!) ')
        if tied=="ko" or tied=="papir" or tied=="ollo":
            print("Használj ékezeteket!")
            rossz=1
        elif tied!="kő" and tied!="papír" and tied!="olló":
            print("kérlek csak kőt, papírt vagy ollót válassz")
            rossz=1
        else:
            rossz=0

    print("gép: "+valasz)
    print("te: "+tied)
    if valasz==tied:
        print("Döntetlen")
        draw+=1
    elif valasz=="kő" and tied=="papír" or valasz=="papír" and tied=="olló" or valasz=="olló" and tied=="kő":
        print("nyertél")
        win+=1
    elif valasz=="kő" and tied=="olló" or valasz=="papír" and tied=="kő" or valasz=="olló" and tied=="papír":
        print("vesztettél")
        loss+=1

    while True:
        ujra=(input("Újra? "))

        if ujra=="igen":
            again=True
            break
        elif ujra=="nem":
            again=False
            break
        else:
            print("Nem adtad meg hogy újra akarod-e kezdeni")

print(win," játékot nyertél", draw," döntetelened volt", " és",loss," játékot veszítettél")
print(0" játékot nyertél" 0" döntetelened volt", " és",0," játékot veszítettél")