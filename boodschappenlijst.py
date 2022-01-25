booschappen = {}

while input('Wilt u iets toevoegen aan uw boodschappenlijstje?') != 'nee':
    wat = input('Wat wilt toevoegen aan uw boodschappenlijstje?')
    hoeveel = int(input('Hoeveel wilt u daarvan?'))

    booschappen[wat] = hoeveel

print('Broodschappenlijstje:')
for boodschap in booschappen:
    print('{:<6} - {:}'.format(booschappen.get(boodschap),  boodschap))
