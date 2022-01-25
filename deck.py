import random


def generateDeck(
        colors=['harten', 'klaveren', 'schoppen', 'ruiten'],
        specials=['boer', 'vrouw', 'heer', 'aas'],
        joker_amount=2):

    new_deck = []

    for color in colors:
        for colorIndex in range(2, 11):
            new_deck += [color + ' ' + str(colorIndex)]

        for special in specials:
            new_deck += [color + ' ' + special]

    new_deck += ['joker'] * joker_amount

    return new_deck


if __name__ == '__main__':
    deck = generateDeck()

    random.shuffle(deck)

    for i in range(1, 8):
        print(f'Kaart {i}: {deck.pop(0)}')

    print(f'Deck ({len(deck)} kaarten): {deck}')