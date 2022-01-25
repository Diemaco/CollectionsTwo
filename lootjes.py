import random

print('Please enter a minimum of 2 names (Leave name empty to start)\n')

namen = {}

while True :
    naam = input('Enter Name: ')

    # Checken of de naam al toegevoegd is
    if naam in namen:
        print('Already addded')
        continue

    # Gebruiker heeft de naam leeg gelaten
    if naam == '':

        # Minimaal 2 namen moeten worden toegevoegd om te stoppen
        if len(namen) < 2:
            print('Need a minimum of 2 names to start')
            continue

        # Genoeg namen dus starten
        else:
            print('Starting')
            break

    # Naam toevoegen aan de dictionary met een leeg lootje
    namen[naam] = ' '

while True:
    try:
        # Namen randomizen
        for naam in namen:
            namen[naam] = random.choice(
                [key for key, value in namen.items() if key not in list(namen.values()) and key != naam])

        # While loop stoppen
        break
    except IndexError:

        # Index error omdat de laatste speler niet zichzelf kan pakken
        continue

# Uitkomst printen
for naam, lootje in namen.items():
    print(f'{naam} heeft {lootje} gekregen')
