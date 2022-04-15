CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '1', 'J', 'Q', 'K',
         'A']  # nulu v 10 musim posleze nahradit mezerou, protoze porovnani ve stringu jde znak od znaku


def battle(string1, string2):
    if type(string1) != str or type(string2) != str:
        raise Exception("Jiný typ inputu než string není povolen")
    stav1 = 0
    stav2 = 0
    hrac1 = string1.replace("0", "")
    hrac2 = string2.replace("0", "")
    hrac1 = string1.upper()
    hrac2 = string2.upper()
    if len(hrac1) != len(hrac2):
        raise IndexError("Oba hráči musí mít stejně karet")
    for kolo in range(len(hrac1)):
        if CARDS.index(hrac1[kolo]) == CARDS.index(hrac2[kolo]):
            continue
        elif CARDS.index(hrac1[kolo]) < CARDS.index(hrac2[kolo]):
            stav2 += 1
        else:
            stav1 += 1
    return f"Hrac 1 vyhral {stav1} her, Hrac 2 vyhral {stav2} her"


print("Ahoj!!! Vitejte ve hře")
players = {}
for i in range(10):
    jmeno_hrace = "hrac" + str(i + 1)
    karty = input(f"Zadejte karty pro hráče{i + 1}: ")
    players[jmeno_hrace] = karty
    next_round = input("Pokračovat? y/n")
    if next_round == "y":
        continue
    else:
        break

if len(players) != 2:
    raise Exception("Tato hra je len pre dvoch hráčov.")

try:
    battle(players["hrac1"], players["hrac2"])

except Exception as e:
    print(str(e))

finally:
    print(f"Dakujeme za hru, nech uz dopadla akokolvek.")
