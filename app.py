import random

def cardname(cardval):
    global points
    suit = random.choice([' of Clubs', ' of Diamonds', ' of Hearts', ' of Spades'])
    if cardval == 1:
        print("Ace" + suit)
        pointsace = input("ACE! Enter 1 or 11 points?")
        if pointsace == 1:
            points += pointsace
        elif pointsace == 11:
            points += pointsace
        else:
            print("DO NOT CHEAT!")
    elif cardval < 11:
        print(str(cardval) + suit)
        points += cardval
    elif cardval == 11:
        print("Jack" + suit)
        points += 10
    elif cardval == 12:
        print("Queen" + suit)
        points += 10
    elif cardval == 13:
        print("King" + suit)
        points += 10
    return

card1 = random.randint(1, 13)
points = 0
print("1. Card:")
cardname(card1)
print("Current Points: " + str(points))

newcard = input("Draw another one? (y/n)")
#So...