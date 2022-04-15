vowels = {"a", "e", "i", "o", "u", "y"}
vyraz = (input("Zadej vyraz: "))
vyraz = vyraz.lower()
pocet = 0

for samohlaska in vowels:
    if samohlaska in vyraz:
        pocet += vyraz.count(samohlaska)

print (f"Ve vyraze {vyraz} je {pocet} samohlasek.")


slovo = input("Zadejte slovo: ")
slovo = slovo.lower()
samohlasky = 0
souhlasky = 0
ostatni = 0
cisel = 0
for znak in slovo:
    if znak in "aáeéěiíoóuúůyý":
        samohlasky = samohlasky + 1
    elif znak in "bcčdďfghjklmnňpqrřsštťvwxzž":
        souhlasky = souhlasky + 1
    elif znak in "0123456789":
        cisel = cisel + 1
    else:
        ostatni = ostatni + 1
print(slovo, "má: ")
print("samohlásek", samohlasky)
print("souhlásek", souhlasky)
print("čísel", cisel)
print("ostatních znaků...", ostatni)
