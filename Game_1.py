'''
Programmer: Joseph DiMartino
Peer Programmer: Ricky Almeida
Program: Room Adventure: Deep Space
'''
# import libraries
import random
from Room import Room
from RockPaperScissors import RPCGame
from tictactoe import tictactoe
from RideTheBus import playCards
first_run = True
alien_alive = True # Initialize alien_alive here
state = "sober"
drink_counter = 0

# support for tab completion
# don't delete this!
try:
    TAB_COMPLETE = True
    import TabCompleter as TC           # for tab completion (if available)
except ModuleNotFoundError:
    TAB_COMPLETE = False

###########################################################################################
# constants
# don't delete this!
VERBS = ["go", "look", "take", "use", "play", "fight"]   # the supported vocabulary verbs
QUIT_COMMANDS = ["exit", "quit", "bye"]                  # the supported quit commands
ATTACK_DAMAGES = {"sword": 20, "fist": 10, "laser_gun": 20}  # damages for each attack type
###########################################################################################
'''
def update_captains_quarters_description(room):
    global alien_alive, ship_repaired

    if ship_repaired:
        room.description = "The hole is repaired! Now the room just needs to be cleaned up."
    elif alien_alive:
        room.description = ("OH NO! You see the alien, time to fight. \n"
                            "Oxygen depletion up 50% in the captains_quarters")
    else:
        room.description = ("A once polished and organized room, destroyed by a hole and wrecked by this alien.\n"
                            "Oxygen depletion up 50%\n{}\n"
                            "PA Speaker: WARNING, hole located in the Captain's quarters, repair_kit needed\n{}".format("="*80, "="*80))
'''


def combat():
    global player_health, alien_health, inventory, alien_alive  # Include inventory in the global declaration

    while player_health > 0 and alien_health > 0:
        print("Your health: {}, Alien's health: {}".format(player_health, alien_health))

        # Display available attack options based on inventory
        available_attacks = ['fist'] + [weapon for weapon in ATTACK_DAMAGES.keys() if weapon in inventory]
        print("Available attacks: {}".format(", ".join(available_attacks)))

        attack = input("Choose your attack: ").lower().strip()

        # Check if chosen attack is available

        if attack in available_attacks:
            if attack == 'sword':
                # Random damage for weapon attacks
                damage = random.randint(1, ATTACK_DAMAGES[attack])
                alien_health -= damage
                print("You hit the alien with your {} for {} damage.".format(attack, damage))
            elif attack == "laser_gun":
                global current_oxygen
                current_oxygen = 0
                print("The laser_gun is too powerful to be used on the ship, destroying a wall and depleting all oxygen.")
                death_by_oxygen_depletion()
                break
            else:
                # Random damage for bare hands
                damage = random.randint(1, ATTACK_DAMAGES[attack])
                alien_health -= damage
                print("You hit the alien with your bare hands for {} damage.".format(damage))
        else:
            print("Invalid attack. You miss your turn.")

        # Alien's turn (random damage)
        alien_damage = random.randint(1, 15)  # Alien damage range from 1 to 15
        if "cloak" in inventory:
            alien_damage = random.randint(1, 10)  # Reduced alien damage range if player has a cloak
        else:
            alien_damage = random.randint(1, 15)  # Original alien damage range

        player_health -= alien_damage
        print("The alien attacks you for {} damage!".format(alien_damage))

        if alien_health <= 0:
            print("You defeated the alien!")
            alien_alive = False  # Update the alien's state
            currentRoom.description = ("A once polished and organized room, destroyed by a hole and wrecked by this alien.\n"
                                "Oxygen depletion up 50%\n{}\n"
                                "PA Speaker: WARNING, hole located in the Captain's quarters, repair_kit needed\n{}".format(
                "=" * 80, "=" * 80))  # Update room description
            return True
        elif player_health <= 0:
            print("You were defeated by the alien.")
            death_by_alien()
            return False

def death_by_oxygen_depletion():
    print("=" * 80)
    print("You have run out of oxygen and have suffocated to death")
    print("""                                                                                                                                  
                                                              :&&&&&                                                               
                                                           &&&&&&&&&&&&&                                                           
                                                      :&&&&&&&      &$&&&&&&&                                                      
                                                  &&&&&&&&&&&       & &&&&&&&&&&&&                                                 
                                               &&&&&&&   &&&&       & &&&&   X&&&&&&&                                              
                                            &&&&&    &   &&&&&&&&&&&&&&&&&&  X  &&&&&&&                                            
                                          $&&&&      &   &&&&&&    x&&&&&&&  &  &  &&&&&&                                          
                                         &&&&        &   &&&&&&&&&&&&&&&&&&&    &  &&&&&&&;                                        
                                        &&&&       &&&&&&&&+&& : && : &&$&&&&&&&&  &&&&&&&&:                                       
                                       &&&     &&&&&;  &&   &;   &&   &    &+   &&&&&&&&&&&&                                       
                                      &&&   &&&&  &&    &&&&&&&&&&&&&&&&&&&&:  &&X +&&&&&&&&&                                      
                                      &&X &&&&&:    :&$&&&                &&&&&&&   &&&&&&&&&&                                     
                                     &&&&&&      X$&                           &&&&&&   &&&&&&X                                    
                                     &&&&&&&   ++                          &:&    x&&  &&&&&&&&                                    
                                    &&&&&   ;: +                                    &&&&   &&&&                                    
                                    &&&&&           &&&X                            &&&&  +&&&&                                    
                                    &&&  &&&&&&&                                    &&&&&&& &&&$                                   
                                    &&&   &&&&&&                                    &&&&&&   &&X                                   
                                    &&&&&&&&&&&&                                    &&&&&&&&&&&&                                   
                                  &&&&    &&&&&&                                   &&&&&&&x   &&&&                                 
                                &&&&&&   &&&&&&&&                                  &&&&&&&&  :&&&&&&                               
                               +&&& &&&&&&&&&&&&&   &&&&&&&&&&       &&&&&&&&&&   &&&&&&&&&&&&&& &&&&                              
                               &&&  &&    &&&&&&&& +&&&&&&&&&&&      &&&&&&&&&&& :&&&&&&&&:   &&& &&&                              
                               &&&  &&&&&&&&&&&&&&  &&&&&&&&&&X      &&&&&&&&&&& &&&&&&&&&&&&&&&&&&&&                              
                               &&&  &&   ;&&&&&&    &&&&&&&&&&  +&&  &&&&&&&&&&    &&&&&&&X   &&&&&&&                              
                                &&& &&   :&&&&&&&        +     +&&&&     ;         &&&&&&&+   &&&&&&                               
                                 &&&&&&&&&&&&&&&&&             &&&&&              &&&&&&&&&&&&&&&&&                                
                                   &&&    &&&&&&&&&&&&&&&                  &&&&&&&&&&&&&&&    &&&                                  
                                    &&&&&&&&&&&&&&&&&&&&++ :           x + &&&&&&&&&&&&&&&&&&&&&                                   
                                   &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                                   
                                  &&&&   ;Xx: x&                                    & &&&&&&&&&&&                                  
                                  &&&                                               & &&&&&&&&&&&+                                 
                                   &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                                  
                                     &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                                    
                                        &&&         &&    &     &&&     &    &&   &  &&&&&&                                        
                                        &&&        &&&X   &     &&&     &   &&&&  &  &&&&&&                                        
                                        &&&   &&         :&             &        &&x&&&&&&&                                        
                                        &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$                                       
                                            &&&                 &&&&  &   &&&&&&&&&&&&&&                                           
                                            &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                                           
                                  +&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                                   
                                   &&&  &   &&  &&  &&  &&  ;&  &&   &   &+ &&  &&& &&&&&&&&&&&&                                   
                                   &&&  &   &&  &   &&  &&   &  &&   &   &   &  &&&  &&& &&&&&&&                                   
                                  :&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                                   
                                   &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                   """)
    print("THE END")
    print("=" * 80)

def death_by_alien():
    print("=" * 80)
    print("The Alien has killed you, better luck next time.")
    print("""o
 \_/\o
( Oo)                    \|/
(_=-)  .===O-  ~~Z~A~P~~ -O- 
/   \_/U'                /|\\\

||  |_/
\\\\  |
{K ||
 | PP
 | ||
 (__\\\\
                    """)
    print("THE END")
    print("=" * 80)

# creates the rooms
def createRooms():
    global alien_alive
    # a list of rooms will store all of the rooms
    # 8 rooms in total in this spaceship
    # currentRoom is the room the player is in, starting off in airlock
    rooms = []
    # first, create the room instances so that they can be referenced below
    airlock = Room("airlock")
    barracks = Room("barracks")
    cargo_bay = Room("cargo_bay")
    gaming_room = Room("gaming_room")
    bar = Room("bar")
    armory = Room("armory")
    medical_bay = Room("medical_bay")
    captains_quarters = Room("captains_quarters")
    #update_captains_quarters_description(captains_quarters)

    # starting room, airlock
    airlock.description = ("Heavy metal doors seal the deep black vacuum of space in here... creepy.\n"
                           "{}\nPA Speaker: WARNING, hole punctured, oxygen levels depleting.\n"
              "PA Speaker: SECURITY BREACH, unexpected life forms entering.\n{}\n".format("="*80, "="*80))
    airlock.addExit("barracks", barracks)
    airlock.addExit("cargo_bay", cargo_bay)
    airlock.addGrabbable("oxygen_tank")
    airlock.addItem("equipment", "looks like there's an oxygen_tank here!")
    airlock.addItem("pressure_gauge", "you tap on the pressure gauge, but looks like it stopped working.")
    rooms.append(airlock)

    # barracks stuff
    barracks.description = "Rows of aligned beds and an eerie fluorescent light. The captain's lucky to have his own room.\n"
    barracks.addExit("airlock", airlock)
    barracks.addExit("cargo_bay", cargo_bay)
    barracks.addExit("gaming_room", gaming_room)
    barracks.addItem("bed", "I could use some rest, but I need to figure out what's going on.")
    barracks.addItem("computer", "It's still unlocked! "
                                 "You check the cameras and notice a shadow run across the gaming_room.")
    rooms.append(barracks)

    # cargo bay stuff
    cargo_bay.description = "It's full of shipping containers, the automatic loading drones make it easy to move it around."
    cargo_bay.addExit("air_lock", airlock)
    cargo_bay.addExit("barracks", barracks)
    cargo_bay.addExit("bar", bar)
    cargo_bay.addGrabbable("cloak")
    cargo_bay.addItem("escape_pod", "This things been broken forever, that damn engineer needs to fix it.")
    cargo_bay.addItem("container", "looks like there's a cloak in here, this will help to blend in.")
    cargo_bay.addItem("generator", "Good thing this generators here, we'd be screwed if we lost power.")
    rooms.append(cargo_bay)

    # gaming room stuff
    gaming_room.description = ("*A shadow run across and escape towards the armory*\n"
                                   "This place seems fun.") #for the first time entering the gaming_room
    gaming_room.addExit("barracks", barracks)
    gaming_room.addExit("bar", bar)
    gaming_room.addExit("armory", armory)
    gaming_room.addItem("gaming_chair", "These chairs are SICK AF.")
    gaming_room.addItem("robo_gamer", "Hello there! interested in playing (rock,paper,scissors | tictactoe)?")
    rooms.append(gaming_room)

    # bar stuff
    bar.description = ("The smell of alcohol fills the air. There's one hell of a liquor selection.\n"
                       "{}\n PA Speaker: WARNING, Captain issued emergency alert.\n{}\n".format("="*80, "="*80))
    bar.addExit("cargo_bay", cargo_bay)
    bar.addExit("gaming_room", gaming_room)
    bar.addExit("medical_bay", medical_bay)
    bar.addGrabbable("key")
    bar.addItem("robo_bartender", "Woah you look pretty stressed, this one's on me. Now how about a game of cards?")
    bar.addItem("empty_glass", "A Guinness, this is what the Captain drinks, this key must be to his room.")
    rooms.append(bar)

    # armory stuff
    armory.description = "Racks of weapons would fill these shelves if we were a military vessel."
    armory.addExit("gaming_room", gaming_room)
    armory.addExit("medical_bay", medical_bay)
    armory.addExit("captains_quarters", captains_quarters)
    armory.addGrabbable("sword")
    armory.addGrabbable("laser_gun")
    armory.addItem("weapons_chest", "My lucky day, a chest with swords and laser_guns..."
                                    "\ntoo bad I can only carry one.")
    rooms.append(armory)

    # medical bay stuff
    medical_bay.description = ("A completely white room with medical equipment... "
                               "This robo doctor looks a little creepy when he's shut down.")
    medical_bay.addExit("bar", bar)
    medical_bay.addExit("armory", armory)
    medical_bay.addExit("captains_quarters", captains_quarters)
    medical_bay.addGrabbable("oxygen_tank")
    medical_bay.addGrabbable("steroids")
    medical_bay.addItem("shelf", "The shelf with all the emergency oxygen_tank, lovely.")
    medical_bay.addItem("robo_doctor", "HELLO... EXAMINING... HEALTHY ENOUGH... GOODBYE.")
    medical_bay.addItem("cabinet", "This medicine cabinet is full of crazy pills, these steroids might be "
                                   "risky to take.")
    rooms.append(medical_bay)

    # captains quarters stuff
    #the aliens in here fighting the captain, you need to fight,
    captains_quarters.description = "OH NO! You see the alien, time to fight."
    captains_quarters.addExit("armory", armory)
    captains_quarters.addExit("medical_bay", medical_bay)
    captains_quarters.addGrabbable("repair_kit")
    captains_quarters.addItem("tool_case", "There's a repair_kit in here, finally the ship can be fixed.")
    rooms.append(captains_quarters)

    # set room 1 as the current room at the beginning of the game
    currentRoom = airlock

    return rooms, currentRoom, captains_quarters



###########################################################################################
# MAIN PROGRAM



# support for tab completion
# don't delete this!
if (TAB_COMPLETE):
    TC.parse_and_bind("tab: complete")

# START THE GAME!!!
inventory = []                      # nothing in inventory...yet
rooms, currentRoom, captains_quarters = createRooms()  # add the rooms to the game

#Initialize Health
player_health = 100
alien_health = 100

# an introduction
print("WELCOME TO ROOM ADVENTURE!")
print("=" * 80)
print("You've been on a deep space mission for the past 10 years,\nit seems to have been "
      "going smooth until now...\n"
      "VERBS: \"go\", \"look\", \"take\", \"use\", \"play\", \"fight\"\n"
      "TO QUIT: \"exit\", \"quit\", \"bye\"")

# play forever (well, at least until the player dies or asks to quit)
while (True):
    # set the status so the player has situational awareness
    # the status has room and inventory information
    status = "{}\nYou are carrying: {}".format(currentRoom, inventory)

    #change the description of rooms if it isn't the first time entering
    if (currentRoom.name == "gaming_room"):
        currentRoom.description = "Full of neon colors, LED lights, and lots of games. This place is great."
    elif (currentRoom.name == "bar"):
        currentRoom.description = ("The smell of alcohol fills the air. There's one hell of a liquor selection.")
    elif (currentRoom.name == "airlock"):
        currentRoom.description = ("Heavy metal doors seal the deep black vacuum of space in here... creepy.\n")

    # support for tab completion
    # don't delete this!
    if (TAB_COMPLETE):
        # add the words to support
        words = VERBS + QUIT_COMMANDS + inventory + currentRoom.exits + currentRoom.items + currentRoom.grabbables
        # setup tab completion
        tc = TC.TabCompleter(words)
        TC.set_completer(tc.complete)

    # display the status
    print("=" * 80)
    print(status)

    def oxygen():
        global depletion_rate
        global current_oxygen
        global current_oxygen_percent
        current_oxygen = current_oxygen - depletion_rate
        if (current_oxygen // 6) <= 0:
            death_by_oxygen_depletion()
        current_oxygen_percent = current_oxygen // 6
        return current_oxygen_percent
    if not first_run:
        print("Oxygen Level: {}%".format(oxygen()))
    if first_run:
        initial_oxygen = 505
        if currentRoom.name == "captains_quarters":
            depletion_rate = 32.5
        else:
            depletion_rate = 25
        current_oxygen = (initial_oxygen - depletion_rate)
        current_oxygen_percent = (initial_oxygen - depletion_rate) // 6
        print("Oxygen Level : {}%".format(current_oxygen_percent))
        first_run = False

    # prompt for player input
    # the game supports a simple language of <verb> <noun>
    # valid verbs are go, look, take, use, fight
    # valid nouns depend on the verb
    action = input("What would you like to do? ")

    # set the user's input to lowercase to make it easier to compare the verb and noun to known values
    action = action.lower().strip()

    # exit the game if the player wants to leave (supports quit, exit, and bye)
    if (action in QUIT_COMMANDS):
        break

    # set a default response
    response = "I don't understand. Try verb noun. Valid verbs are {}.".format(", ".join(VERBS))
    # split the user input into words (words are separated by spaces) and store the words in a list
    words = action.split()

    # the game only understands two word inputs
    if (len(words) == 2):
        # isolate the verb and noun
        verb = words[0].strip()
        noun = words[1].strip()

        # we need a valid verb
        if verb in VERBS:

            if (verb != "fight") and (currentRoom.name == "captains_quarters") and (alien_alive == True):
                print("You needed to fight the alien before doing other things in the "
                      "captains_quarters!")
                death_by_alien()
                exit()

            # the verb is: go
            if (verb == "go"):
                # set a default response
                response = "You can't go in that direction."

                # check if the noun is a valid exit
                if (noun in currentRoom.exits):
                    # get its index
                    i = currentRoom.exits.index(noun)
                    if (currentRoom.name == "medical_bay" or currentRoom.name == "armory") and \
                       (noun == "captains_quarters") and ("key" in inventory): #check if you have key to enter final room
                        currentRoom = currentRoom.exitLocations[i]
                        response = "You walk and enter the {}.".format(noun)
                    elif (currentRoom.name == "medical_bay" or currentRoom.name == "armory") and \
                            noun != "captains_quarters": #not trying to enter captains_room, no key required
                        currentRoom = currentRoom.exitLocations[i]
                        response = "You walk and enter the {}.".format(noun)
                    elif (currentRoom.name != "medical_bay" and currentRoom.name != "armory"):
                        currentRoom = currentRoom.exitLocations[i]
                        response = "You walk and enter the {}.".format(noun)
                    elif (currentRoom.name == "medical_bay" or currentRoom.name == "armory") and \
                         (noun == "captains_quarters") and ("key" not in inventory): #trying to enter final room with no key
                        response = "You cant go into the Captain's quarters without a key."

                    # set the response (success)
            # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "You don't see that item."

                # check if the noun is a valid item
                if (noun in currentRoom.items):
                    # get its index
                    i = currentRoom.items.index(noun)
                    # set the response to the item's description
                    response = currentRoom.itemDescriptions[i]

                if state == "drunk" and drink_counter < 2:
                    response = "Everything looks so blurry, maybe I drank too much..."
                    drink_counter += 1

                elif (noun == "equipment") and ("oxygen_tank" in inventory) and (currentRoom.name == "airlock"):
                    i = currentRoom.items.index(noun)
                    currentRoom.itemDescriptions[i] = "A pile of broken equipment, what a waste."
                    response = currentRoom.itemDescriptions[i]
                elif (noun == "shelf") and ("oxygen_tank" in inventory) and (currentRoom.name == "medical_bay"):
                    i = currentRoom.items.index(noun)
                    currentRoom.itemDescriptions[i] = "A shelf of empty oxygen tanks, how helpful."
                    response = currentRoom.itemDescriptions[i]

                elif (noun == "robo_bartender") and ("whiskey" not in inventory):
                    inventory.append("whiskey")
                elif (noun == "robo_bartender") and ("whiskey" in inventory):
                    i = currentRoom.items.index(noun)
                    currentRoom.itemDescriptions[i] = "No more drinks until the alert is over, but how about a game of cards?"
                    response = currentRoom.itemDescriptions[i]

                elif (noun == "empty_glass") and ("key" in inventory):
                    i = currentRoom.items.index(noun)
                    currentRoom.itemDescriptions[i] = "The Captain sure loves Guinness, there's not a drop left."
                    response = currentRoom.itemDescriptions[i]

                elif (noun == "container") and ("cloak" in inventory):
                    i = currentRoom.items.index(noun)
                    currentRoom.itemDescriptions[i] = "A container full of cloth made with fine silk."
                    response = currentRoom.itemDescriptions[i]

                elif (noun == "cabinet") and ("steroids" in inventory):
                    i = currentRoom.items.index(noun)
                    currentRoom.itemDescriptions[i] = "All the medicine looks pretty useless in here."
                    response = currentRoom.itemDescriptions[i]


            # the verb is: take
            elif (verb == "take"):
                # set a default response
                response = "You don't see that item."

                # check if the noun is a valid grabbable and is also not already in inventory
                if (noun in currentRoom.grabbables and noun not in inventory):
                    # get its index
                    i = currentRoom.grabbables.index(noun)
                    # add the grabbable item to the player's inventory
                    inventory.append(currentRoom.grabbables[i])
                    # set the response (success)
                    if noun == "oxygen_tank":
                        response = "You take {}. This may be useful when oxygen gets low.".format(noun)
                    elif noun == "key":
                        response = "You take {}. Hopefully this works for the Captains quarters.".format(noun)
                    elif noun == "steroids":
                        response = "You take {}. You feel much stronger, but your heart rate is insanely high.".format(noun)
                    else:
                        response = "You take {}.".format(noun)
                if (noun == "sword") and ("laser_gun" in inventory) and (currentRoom.name == "armory"):
                    response = "You can't take the {}, you already have the laser_gun".format(noun)
                elif (noun == "laser_gun") and ("sword" in inventory) and (currentRoom.name == "armory"):
                    response = "You can't take the {}, you already have the sword".format(noun)


                #remove specific grabbables already taken
                if (noun in currentRoom.grabbables and noun in inventory):
                    i = currentRoom.grabbables.index(noun)
                    currentRoom.grabbables.pop(i)

                    if (noun == "sword") and (currentRoom.name == "armory"):
                        i = currentRoom.grabbables.index("laser_gun")
                        currentRoom.grabbables.pop(i)
                    if (noun == "laser_gun") and (currentRoom.name == "armory"):
                        i = currentRoom.grabbables.index("sword")
                        currentRoom.grabbables.pop(i)



            elif (verb == "use"): #verb is: use
                response = "You can't use this item." #default response

                if (noun in inventory):
                    i = inventory.index(noun)
                    inventory.pop(i)
                    response = "You use {}.".format(noun)
                    if noun == "oxygen_tank":
                        current_oxygen = 620
                    elif noun == "whiskey":
                        state = "drunk"
                        response = "You drank the whiskey! This stuff is pretty strong."
                    elif noun == "steroids":
                        player_health -= 30
                        for key in ATTACK_DAMAGES:
                            ATTACK_DAMAGES[key] += 10
                    elif (noun == "repair_kit") and (currentRoom.name == "captains_quarters"):
                        response = "You repaired the ship! Feel free to enjoy the mini games!"
                        current_oxygen = 600
                        depletion_rate = 0
                        currentRoom.description = "The hole is repaired! Now the room just needs to be cleaned up."


            elif (verb == "play"):
                if (noun.lower().strip() == "rock,paper,scissors" and currentRoom.name == "gaming_room"):
                    response = "play_RPC"
                elif (noun.lower().strip() == "tictactoe" and currentRoom.name == "gaming_room"):
                    response = "play_ttt"
                elif (noun == "cards" and currentRoom.name == "bar"):
                    response = "play_cards"
                else:
                    response = "You can't play that here!"

            elif verb == "fight" and currentRoom.name == "captains_quarters":
                won = combat()
                if won:
                    response = "You have defeated the alien, now repair the ship!"
                else:
                    response = "You were defeated by the alien."
                    currentRoom = None  # Player dies
                    break  # End the game loop if the player dies
        else:
            # Handle other verbs (go, look, take, etc.)
            if len(words) == 2:
                noun = words[1]
                # ... (existing code to handle 'go', 'look', 'take', etc.)
            else:
                print("Invalid command. Try verb noun.")
    else:
        print("I don't understand. Try verb noun. Valid verbs are {}.".format(", ".join(VERBS)))

    # display the response
    if (currentRoom != None):
        print("=" * 80)

        if response == "play_RPC": #if game is rock,paper,scissors
            print(RPCGame())
        elif response == "play_ttt": #if game is tictactoe
            print(tictactoe())
        elif response == "play_cards": #if game is cards
            print(playCards())
        else:
            print(response) #default response for anything else



