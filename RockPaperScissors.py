import random
def RPCGame():
    player_choice = input("Choose your move (rock, paper, scissors): ") #players move
    options = ["rock", "paper", "scissors"] #three options to make a move
    npc = random.choice(options)
    result = "robo_gamer chose: {}\n".format(npc)
    if player_choice == npc: #tie
        result += "It's a tie!"
    elif (player_choice == "rock" and npc == "scissors") or \
         (player_choice == "paper" and npc == "rock") or \
         (player_choice == "scissors" and npc == "paper"): #if result is a players win
        result += ("You win! By the way, I overheard that taking steroids will make you much stronger, "
                   "but you'll be way less durable.")
    else:
        result += "You lose! Try again soon!" #everything else would be NPC winning
    return result  #return results for main game
