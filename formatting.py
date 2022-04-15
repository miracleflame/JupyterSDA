# Displaying multiple strings at once
print("What", "a", "beautiful", "day", ".")
print("1", "2", 3, 4, 5)
fruit = "orange"
print("apple", "banana", fruit)

sample_string = 'PyCharm'
print(len(sample_string))

hello = "Hello, World!"
print(hello.index('o'))
print(hello.count('o'))
print(hello[7])  # Prints W
print(hello[7:12])  # Prints World
print(hello[7:12:2])  # Prints "Wrd"
print(hello[::3])
print(hello[::-1])
print(hello.upper())  # Prints hello, world!

# Displaying multiple strings simultaneously with separator and final string
print("What", "for", "beautiful", "day", ".", sep="-", end="! \n")
print("1", "2", 3, 4, 5, sep="<", end="<... \n")
fruit = "orange"
print("apple", "banana", fruit, sep="+", end="= yummy \n")

# Format and display (older way)
title = "General"
name = "Kenobi"
print("Hello there, %s %s" % (title, name))

# Format and display (newer way)
title = "General"
name = "Kenobi"
print("Hello there, {} {}".format(title, name))

# Format and display (most recent way)
title = "General"
name = "Kenobi"
print("Hello there, {name} {title}".format(name=name, title=title))

# Format and display (most recent way)
title = "General"
name = "Kenobi"
print("Hello there, {1} {0}".format(title, name))

# Format and display (latest method)
title = "General"
name = "Kenobi"
print(f"Hello there, {title} {name}")

header1 = "Name"
header2 = "Age"
name = "John"
age = 22

print(f"| {header1} | {header2} |")
print("-" * 27)
print(f"| {name} | {age} |")

# Changing the way the variable is displayed
n = 109.2345654324
print(f"{n: .3f}")  # will display 109.234

percent = 0.71
print(f"{percent: .1%}")  # will display 71.0%

#kazdy treti vypis vety bude VELKYMI PISMENY
def zmen_vetu(veta, n_opakovani):

    #iterace od 0 do n_opakovani
    for i in range (n_opakovani):
        pracovni_veta = veta

        #delitelne 3
        if i % 3 == 0:
            pracovni_veta = pracovni_veta.upper()

        # delitelne 4
        if i % 4 == 0:
            pracovni_veta = pracovni_veta + "!" #f"{pracovni_veta}!"

        print(pracovni_veta)

zmen_vetu("Kobyla ma maly bok", 11)