from tkinter import *
import threading
from tkinter import messagebox
from tkinter import ttk
from tkinter import colorchooser
import os
config_file='config_gui.txt'
eredmeny_file='eredmeny.txt'
if os.path.exists(config_file):
    if os.path.isfile(config_file):
        with open(config_file, "r") as config:
            szin = str(config.readline())
draw=0
win=0
loss=0
tied=None
megszam=0
szam=6
reset=False
eredmeny="eddigi eredményed: nyertél "+str(win)+" játékot, "+str(draw)+" döntetlened volt és "+str(loss)+" játékot vesztettél"
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
x=threading.Thread(target=rps2,daemon=True)
x.start()
def ko():
    global tied
    global reset
    tied="kő"
    reset=True
def papir():
    global tied
    global reset
    tied="papír"
    reset = True
def ollo():
    global tied
    global reset
    tied="olló"
    reset = True
def szines():
    global szin
    color=colorchooser.askcolor()
    szin=color[1]
    with open(config_file, "r") as config:
        check = str(config.readline())
        if szin!=check:
            if messagebox.askyesno(title="Háttérszín változtatás", message="Biztos meg akarod változtatni a háttérszínt?"):
                with open(config_file, "w") as config:
                    config.write(szin)
            else:
                pass
#if meg()
hat=szin #háttér szín
window= Tk()
notebook=ttk.Notebook(window)
tab1=Frame(notebook)
tab2=Frame(notebook)
notebook.add(tab1,text="Játék")
notebook.add(tab2,text="Beállítások")
notebook.pack()
szel=str(1600)
mag=str(1000)
geo=str(szel+'x'+mag)
window.geometry(geo)
window.title("Kő papír olló pro Gaming")
icon=PhotoImage(file='floppa.png')
hatterkep=PhotoImage(file='floppa_bg.png')
beallitaskep=PhotoImage(file='kadfloppa.png')
window.iconphoto(True,icon)
window.config(background=hat)
label=Label(tab1,text="Kő papír olló",font=('Arial',40,'bold'),fg='#013e54',bg=hat,
            relief=RAISED,padx=20,image=hatterkep,compound='bottom')
label.pack()
label=Label(tab2,text="Kő papír olló beállítások",font=('Consolas',40,'bold'),fg='#ab0707',bg='#ed6d64',
            relief=RAISED,padx=20,image=beallitaskep,compound='bottom')
label.pack()
szinvalaszto=Button(tab2,text='háttérszín választás',command=szines,font=("Times new Roman",20))
szinvalaszto.place(x=int(szel)/15,y=100)
ko_gomb=Button(tab1,
              text="Kő",
              command=ko,
              font=("Times new Roman",20))
ko_gomb.place(x=int(szel)/4,y=int(mag)-100)
papir_gomb=Button(tab1,
              text="Papír",
              command=papir,
              font=("Times new Roman",20))
papir_gomb.place(x=int(szel)/2,y=int(mag)-100)
ollo_gomb=Button(tab1,
              text="olló",
              command=ollo,
              font=("Times new Roman",20))
ollo_gomb.place(x=int(szel)/1.25,y=int(mag)-100)
window.mainloop()
print("win: ", win, "draw: ", draw, "loss: ", loss)
if win==0 and draw==0 and loss==0:
    pass
else:
    with open(eredmeny_file, 'a') as ide:
        ide.write("\n"+str(win)+" "+str(draw)+" "+str(loss))