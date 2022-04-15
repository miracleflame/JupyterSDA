smädný = True
mince = ["10c", "20c", "50c", "1 euro", "2 eura"]


def zaplatit():

    cena = 70

    while cena > 0:
        vhodene = input(f"\nAutomat prijíma mince 10c, 20c, 50c, 1 euro, 2 eura.\n\n"
                        f"VHOĎTE {cena}c PRE VÝDAJ BOROVIČKY: ")

        if vhodene not in mince:
            print("\nTOTO NIE JE PRIJATEĽNÁ MINCA!")

        elif vhodene == "10c":
            cena -= 10
        elif vhodene == "20c":
            cena -= 20
        elif vhodene == "50c":
            cena -= 50
        elif vhodene == "1 euro":
            cena -= 100
        elif vhodene == "2 eura":
            cena -= 200
        continue

    vratit = abs(cena)
    if vratit == 0:
        print(f"\n\nĎakujeme za nákup. Vezmite si svoju borovičku.\n\n")
    else:
        vydavok = []
        while vratit > 0:
            if vratit >= 100:
                vratit -= 100
                vydavok.append("1 euro")
            elif vratit in range(50, 91):
                vratit -= 50
                vydavok.append("50c")
            elif vratit in range(20, 41):
                vratit -= 20
                vydavok.append("20c")
            elif vratit == 10:
                vratit -= 10
                vydavok.append("10c")
            continue

        print(f"\n\nĎakujeme za nákup. Vezmite si svoju borovičku.\n\n"
              f"VÝDAVOK JE")
        for i in vydavok:
            print(i)


while smädný:
    zaplatit()
