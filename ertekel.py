"""1. feladat:  összesen 7p szerezhető, a modul neve: ertekel.py
minta:
I/A, B:
Étel neve: Ananászos pizza
Étel rendelőjének neve: Kiss Előd
Értékelés (1-5): 4

I/C:
Köszönjük az értékelést!

A.Kérje be az alábbi adatokat a fenti mintának megfelelően:
étel neve, étel rendelőjének neve és értékelés!(2p)
B.A program az adatbekérés után írja ki, ha az értékelés nem a megfelelő határokon belül lett megadva ( [1,5], zárt intervallum értendő):
Amennyiben negatív számot adott meg:
“Az értékelés nem lehet negatív!”,
Amennyiben 5 feletti egész számot adott meg:
“5 pont feletti értékelés nem elfogadható!”
Helyes pont-adat esetén:
“Köszönjük az értékelést!”
Feltételezzük, hogy csak egész számokat adnak meg. (4p)
C.A mintának megfelelően írassa ki az eredményt! (1p)"""


def ertekeles():
    etel = input("Étel neve: ")
    nev = input("Étel rendelőjének neve:")
    szam = int(input("Értekelés (1-5): "))

    if szam < 0:
        print("Az értékelés nem lehet negativ!")

    elif szam > 5:
        print(" 5 pont feletti értékelés nem elfogadható!")

    else:
        print("Köszönjük az értékelést!")

    print(f"I/A,B: \n \t Étele neve: {etel}\n \t Étel rendelőjének neve:{nev}\n \t Értékelés:{szam}")
    print(f"I/C: \n \t Köszönjük az értékelést!")





