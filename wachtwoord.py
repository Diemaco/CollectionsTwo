import random


def generatePassword(letters='abcdefghijklmnopqrstuvwxyz', cijfers='0123456789', speciaal='@#$%&_?'):
    new_pass = []

    # 2 - 6 hoofdletters
    aantal_hoofdletters = random.randrange(2, 7)

    # 4 - 7 cijfer niet op de eerste 3 plekken
    aantal_cijfers = random.randrange(4, 8)

    # 3 speciaal niet aan het begin/einde (of op vaste plek)
    aantal_speciaal = 3

    # 8+ letters
    aantal_letters = 24 - (aantal_hoofdletters + aantal_cijfers + aantal_speciaal)

    for i in range(aantal_hoofdletters):
        new_pass += [letters.upper()[random.randrange(len(letters))]]

    for i in range(aantal_letters):
        new_pass.insert(random.randrange(0, len(new_pass) - 1), letters[random.randrange(len(letters))])

    for i in range(aantal_speciaal):
        new_pass.insert(random.randrange(1, len(new_pass) - 1), speciaal[random.randrange(len(speciaal))])

    for i in range(aantal_cijfers):
        new_pass.insert(random.randrange(4, len(new_pass) - 1), cijfers[random.randrange(len(cijfers))])

    return ''.join(new_pass)


if __name__ == '__main__':
    print(generatePassword())
