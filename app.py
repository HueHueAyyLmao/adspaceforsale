import card_random
import random
import itertools
stake = input ("How much money would you like to put in : ")

print("You receive:")

rank = random.choice(('Ace of','2 of','3 of','4 of','5 of','6 of','7 of','8 of','9 of','10 of','Jack of','Queen of','King of'))
#suit = random.choice((' Clubs',' Diamonds',' Hearts',' Spades'))
card = rank #+  suit

print(card)
if rank == "Ace of":
        choose= input ("Would you like 1 or 11: ")
        if choose==1:
            print("Ace will count as 1")
        elif choose==11:
            print("Ace will count as 11")

rank1 = random.choice(('Ace of','2 of','3 of','4 of','5 of','6 of','7 of','8 of','9 of','10 of','Jack of','Queen of','King of'))
#suit1 = random.choice((' Clubs',' Diamonds',' Hearts',' Spades'))
card1 = rank1 #+ suit1
yesno = input ("Do you want to draw another one? ")
if yesno =="Yes":
    print("You receive:")
    print(card1)
#versuche grad nen weg zu finden um die karten als zahlen zu definieren
if yesno =="No":
#print(sum(card))
