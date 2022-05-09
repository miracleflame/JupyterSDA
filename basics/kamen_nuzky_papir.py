import random

# kamen, nuzky, papir vs. PC
zbrane = ["kamen", "nuzky", "papir"]

def play(pocet_kol):
    skore = {"hrac":0, "pc":0}
    kolo = 1
    while pocet_kol != 0:
        print(f"Kolo číslo {kolo}.")
        hrac = str(input("Zvol kamen, nuzky alebo papir: "))
        pc = random.choice(zbrane)
        print(f"Oponent zvolil {pc}.")
        if hrac == pc:
            print("REMIZA")
        elif hrac == "kamen" and pc == "nuzky":
            print("Hrac kamenom porazil oponentove nuzky.")
            skore["hrac"] += 1
        elif hrac == "kamen" and pc == "papir":
            print("Oponent porazil papirom hracov kamen.")
            skore["pc"] += 1
        elif hrac == "nuzky" and pc == "kamen":
            print("Oponent porazil kamenom hracove nuzky.")
            skore["pc"] += 1
        elif hrac == "nuzky" and pc == "papir":
            print("Hrac nuzkami porazil oponentov papir.")
            skore["hrac"] += 1
        elif hrac == "papir" and pc == "kamen":
            print("Hrac papirom porazil oponentov kamen.")
            skore["hrac"] += 1
        elif hrac == "papir" and pc == "nuzky":
            print("Oponent porazil nuzkami hracov papir.")
            skore["pc"] += 1
        print(f"Skore je {skore}.\n")
        pocet_kol -= 1
        kolo += 1
        continue

print("Koniec hry.")
if skore[hrac] > skore[pc]:
    print("Vitazom je hrac.")
else
    print("Vitazom je oponent.")
play(5)