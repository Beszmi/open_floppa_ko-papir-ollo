def rps2():
    global draw
    global win
    global loss
    global tied
    global reset
    global eredmeny
    dontetlen="döntetlen.\n"+eredmeny+"\nújra?"
    nyertel="nyertél.\n"+eredmeny+"\nújra?"
    vesztes = "vesztettél.\n"+eredmeny+"\nújra?"
    while True:
        if reset==True:
            print(tied)
            import random
            lehet = ["kő", "papír", "olló"]
            valasz = random.choice(lehet)
            if valasz == tied:
                print("Döntetlen")
                draw += 1
                if messagebox.askyesno(title="Floppa eredmény",message=dontetlen):
                    pass
                else:
                    messagebox.showinfo(title="Eredményed",message=eredmeny)
                    break
            elif valasz == "kő" and tied == "papír" or valasz == "papír" and tied == "olló" or valasz == "olló" and tied == "kő":
                print("nyertél")
                win += 1
                if messagebox.askyesno(title="Floppa eredmény",message=nyertel):
                    pass
                else:
                    messagebox.showinfo(title="Eredményed",message=eredmeny)
                    break
            elif valasz == "kő" and tied == "olló" or valasz == "papír" and tied == "kő" or valasz == "olló" and tied == "papír":
                print("vesztettél")
                loss += 1
                if messagebox.askyesno(title="Floppa eredmény",message=vesztes):
                    pass
                else:
                    messagebox.showinfo(title="Eredményed",message=eredmeny)
                    break
            reset = False
        else:
            pass