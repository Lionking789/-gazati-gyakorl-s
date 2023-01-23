"""2. feladat:    összesen 14p szerezhető, a modul neve: sorozat.py
minta:
II/A, B, C:
           	20$28$124$166$15$188$174$243$221$22$945$841
II/D, E:
           	A páratlanok száma: 5.
kimutatas.txt tartalma:
II/F:
A páratlanok száma: 5.

A.Írasson ki a konzolra dollár jelel ($) elválasztva 12 számból álló véletlen számsorozatot [-10,1000] zárt intervallumon a mintának megfelelően! (4p)
B.A generált értékeket tárolja lista adatszerkezetben! (1p)
C.A $ jel csak az értékek között szerepeljen (a végén, elején ne)! (2p)
D.Írjon függvényt paratlanok_szama néven, amiben számolja meg, hogy hány olyan elem van, ami páratlanok. A visszatérési érték legyen egy egész szám! (3p)
E.A paratlanok_szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit konzol_kiir nevű metódusban fogalmazzon meg! (2p)
F.A paratlanok_szama függvény eredményét írassa ki a mintának megfelelően a eredmeny.txt nevű fájlba, amit fajlba_kiir nevű metódusban fogalmazzon meg! (2p)"""


import random
vel_lista = []

def veletlen_kiir():
    i = 0
    szoveg = ""
    while i <= 11:
        vel = int(random.random()*1111) -10
        vel_lista.append(vel)
        if i == 11:
            szoveg += str(vel) + ""

        else:
            szoveg += str(vel) + "$"
        i += 1

    print(f"II/ A, B, C: \n \t {szoveg}")

def paratlanok_szama():
    i = 0
    paratlandb = 0
    while i < len(vel_lista):
        if vel_lista[i] %2 !=0:
            paratlandb += 1
        i += 1
    return paratlandb


def konzol_kiir():
    print(f"II/D,E: \n \t A páratlanok száma:{paratlanok_szama()}")


def fajlba_kiir():
    fajl = open("eredmeny.txt", "w", encoding="utf-8" )
    fajl.write(f"II/F: \n \t A páratlanok száma: {paratlanok_szama()}")
    fajl.close()
    print(fajl) 




