import random

def slumpa_card():
    colors = ["ruter", "hrarts", "spades", "clubs"]
    value = random.randint(2, 15)
    color = random.choice(colors)
    return[color, value]

def compare_cards(kort1, kort2):
    if kort1[1] == kort2[1]:
        print("korten har samma valor! " + str(kort1[1]) + " " + str(kort2[1]))

def poker_hand(cards):
    values = [card[1] for card in cards]
    hand = {value: values.count(value) for value in values}
    paren = []
    if 2 in hand.values():
        for k, v in hand.items():
            if v >= 2:
                paren.append(k)
        print(f"Du har fatt ett par! {paren}")
    else:
        print("Ingen vist denna gang")

hand = []
for _ in range(1, 6):
    hand.append(slumpa_card())

poker_hand(hand)

print(len(hand))
