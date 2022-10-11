def rps(az):
    import random
    again=False
    elso=True
    win=0
    loss=0
    draw=0
    rossz=0
    tied=az
    statok=list()
    def kerdes():
        tied = input("Válassz: (ékezetes legyen és kisebetűs legyen!)")
        return tied
    while elso==True or again==True or rossz==1:
        elso = False
        if again==True and rossz==0:
            tied=kerdes()
        lehet=["kő","papír","olló"]
        valasz=random.choice(lehet)
        if tied=="ko" or tied=="papir" or tied=="ollo":
            print("Használj ékezeteket!")
            rossz=1
            tied=kerdes()
        elif tied!="kő" and tied!="papír" and tied!="olló":
            print("kérlek csak kőt, papírt vagy ollót válassz")
            rossz = 1
            tied=kerdes()
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
    statok.append(win)
    statok.append(draw)
    statok.append(loss)
    return statok
if __name__=="__main__":
    statok=rps(input("Válassz: (ékezetes legyen és kisebetűs legyen"))
    print(statok[0], " játékot nyertél", statok[1], " döntetelened volt", " és", statok[2], " játékot veszítettél")
    win_rate = statok[0] / (statok[1] + statok[2])
    szazalek = win_rate * 100
    print("Nyerési százalékod ", szazalek, "% volt")