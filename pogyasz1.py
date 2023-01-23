"""A csomag.txt forrásállomány, csomagok méret adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
A csomag.txt állomány szerkezete:
·         a (szélesség cm): pl: 51
·         b (magasság cm): pl.: 33
·         c (mélység cm): pl.: 24
·         m (súly kg-ban megadva): pl.: 10
Az állomány első sora a mezőneveket tartalmazza kettőskereszttel elválasztva.
A megoldás mintája:
III/A, B:
            	A pogyászok száma: 101
III/C:
            	Az 51 cm-es pogyászok átlag súlyértéke: 7375 g
III/D:
            	A legmagasabb pogyász méretei: 47x46x16, súlya: 4 kg.
A.Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a csomag.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.Írassa ki a pogyászok számát a mintának megfelelően a konzolra! (2p)
C.Határozza meg és írassa ki a konzolra a minta szerint, hogy mennyi az 51 cm széles pogyászok átlag súlya gramban. (1kg = 1000g) (4p)
D.Írassa ki konzolra a mintának megfelelően a legmagasabb pogyász  méreteit és súlyát (ha több is van, akkor az első legmagasabb adatait).(4p)"""

from Pogyasz import Pogyasz
pogyasz_lista = []


def beolvas():
    fajl = open("csomag.txt", "r", encoding="utf-8")
    fajl.readline()
    sorok= fajl.readlines()
    fajl.close()
    print(sorok)

    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("#")
        print(sor)
        pogyasz_lista.append(Pogyasz(sor))
        i += 1

    print(pogyasz_lista[3].suly)


def pogyaszok_szama():
    print(f"III/A,B: \n \t A pogyászok száma: {len(pogyasz_lista)}")

def pogyaszok_sulya():
    i = 0
    suly_osszesen = 0
    otvenegy_db = 0


    while i < len(pogyasz_lista):
        if pogyasz_lista[i].szelesseg == 51:
            otvenegy_db += 1
            suly_osszesen += pogyasz_lista[i].suly

        i += 1
    szam = suly_osszesen / otvenegy_db

    print(f"III/C: \n \t Az 51 cm-es pogyászok átlag súlyértéke: {int(szam*1000)} g")

def pogyaszok_magassaga():
    i = 0
    legmagasabb = pogyasz_lista[0]
    while i < len(pogyasz_lista):
        if pogyasz_lista[i].magassag > legmagasabb.magassag:
            legmagasabb = pogyasz_lista[i]
        i += 1
    print(f"III/D: \n \t A legmagasabb pogyász méretei:{legmagasabb.szelesseg}x{legmagasabb.magassag}x{legmagasabb.melyseg}, súlya: {legmagasabb.suly} kg")
