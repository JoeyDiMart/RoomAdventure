import random
def playCards():
    card_suits = ["hearts", "diamonds", "spades", "clubs"] #list of suits
    card_numbers = ["two", "three", "four", "five", "six", "seven", "eight",
                          "nine", "ten", "jack", "queen", "king"] #list of cards

    #all 4 cards being flipped
    first_suit = random.randint(0, 3)
    first_number = random.randint(0, 11)
    first_card = "{} of {}".format(card_numbers[first_number], card_suits[first_suit]) #the first card flipped

    second_number = random.randint(0, 11)
    second_card = "{} of {}".format(card_numbers[second_number], card_suits[random.randint(0, 3)])
    #second card flipped

    third_number = random.randint(0, 11)
    third_card = "{} of {}".format(card_numbers[third_number], card_suits[random.randint(0, 3)])
    #third card flipped

    fourth_suit = random.randint(0, 3)
    fourth_card = "{} of {}".format(card_numbers[random.randint(0, 11)], card_suits[fourth_suit])
    #fourth card flipped


    color = input("What color (red/black)? ") #first question
    print(first_card) #show first card

    if (color.lower().strip() == "red" and first_suit <= 1) or \
    (color.lower().strip() == "black" and first_suit > 1):

        over_under = input("Correct! now over or under? ") #second question
        print(second_card) #show second card

        if (over_under.lower().strip() == "over" and second_number > first_number) or \
        (over_under.lower().strip() == "under" and second_number < first_number): #if correct guess
            between_outside = input("Correct! Now between or outside? ") #third question
            print(third_card) #third card showed
            if ((between_outside.lower().strip() == "between" and (second_number > third_number > first_number))) or \
            (between_outside.lower().strip() == "outside" and
                (second_number < third_number or third_number < first_number)): #see if third card is between our outside of the first and second card
                suit = input("Correct! Last one, what's the suit (hearts, diamonds, spades, clubs)? ")
                print(fourth_card) #show fourth card
                if (suit.lower().strip() == "hearts" and fourth_suit == 0) or \
                (suit.lower().strip() == "diamonds" and fourth_suit == 1) or \
                (suit.lower().strip() == "spades" and fourth_suit == 2) or \
                (suit.lower().strip() == "clubs" and fourth_suit == 3): #see if card guessed is specific suit
                    return ("You win! You know, the Captain got a hand on a few of these laser guns. "
                            "I overheard him saying they were a bit too powerful for use on the ship.") #gives a hint if guessed correctly
    return "Sorry, you lost." #return lose if any part was incorrect
