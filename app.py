#import card_random
import random
import itertools
stake = input("How much money would you like to put in: ")

print("You receive: ")

cardval = random.randint(1, 13)

choose cardval:
    case 1:
        rank = "Ace of"
    case 2:
        rank = "2 of"
        points = 2
    case 3:
        rank = "3 of"
        #points....
    case 4:
        rank = "4 of"
    case 5:
        rank = "5 of"    
    case 6:
        rank = "6 of"
    case 7:
        rank = "7 of"
    case 8:
        rank = "8 of"
    case 9:
        rank = "9 of"
    case 10:
        rank = "10 of"
    case 11:
        rank = "Jack of"
    case 12:
        rank = "Queen of"
    case 13:
        rank = "King of"

suit = random.choice((' Clubs',' Diamonds',' Hearts',' Spades'))
card = rank + suit

print(card)

if cardval = 1:
    ace = input("Would you like 1 or 11 points: ")
    choose ace:
        case 1:
            print("Ace will count as 1")
            points = 1
            break
        case 11:
            print("Ace will count as 11")
            points = 11
            break
        default:
            print("ERROR")
            #Musst du noch weiter ausfuehren


rank1 = random.choice(('Ace of','2 of','3 of','4 of','5 of','6 of','7 of','8 of','9 of','10 of','Jack of','Queen of','King of'))
#suit1 = random.choice((' Clubs',' Diamonds',' Hearts',' Spades'))
card1 = rank1 #+ suit1
yesno = input ("Do you want to draw another one? ")
if yesno =="Yes":
    print("You receive:")
    print(card1)
#versuche grad nen weg zu finden um die karten als zahlen zu definieren
#print(sum(card))