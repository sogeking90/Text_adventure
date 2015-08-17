# This is a quick text adventure I have made as a learning project and as homework for the LPTHW book.
# It is going to be a fairly basic text adventure with standard commands such as go north, look and i for inventory. 
# The pet companion can be interacted with also.
from sys import exit
import random

# A list which contains the players inventory.
invent = ["Dog toy", "Pick Axe"]

#A list of rooms currently visited
rooms_visited = ["entrance_room"]

def game_help():
    print """
    Commands:
    go [direction] eg: go north
    look - Read the rooms description
    take [item] eg: take sword
    stroke mia - Comfort your trusty dog companion
    throw ball - Throw your ball for your dog
    cls - Clear the screen, type look to reread description
    """

def cls():
    print "\n" * 100

def dog_events():
    # Random chance of the dog Mia interacting with you.
    chance = random.randint(1, 61)
    if chance == 1:
        print "Mia starts doing somersaults whilst screaming \"Gobshite!\". Huh. Strange."

    elif chance > 1 and chance < 5:
        print "Mia rolls on her back and looks at you expectantly.\nYou of course rub her belly."

    elif chance > 20 and chance < 10:
        print "Mia paws at you annoyingly."

def start():
    print """
    The young scholar enters the newly opened "Temple of the maker" which has been the subject
    of mystery for hundreds of years. All that anyone knows for sure is that it was built by 
    the Elves thousands of years ago. Sadly Elves have been extinct for over a millennia so 
    it was never as simple as asking an elf how to open the temple. 

    The passage is opened to you not by chance. You spent nearly half your life obsessed with
    the idea of opening the temple and discovering what mysteries await.
    After getting your hands on an ancient elvish tome you finally opened the door with the 
    runes you discovered in the tome.

    -----------------------------------
    Type 'help' at any time to see a full list of commands. Press Enter to start the game.
    """
    raw_input("> ")
    cls()

def entrance_room():
    playing = True
    description = """
    The entrance chamber is relatively small and almost disappointingly bland.
    The walls are plain with no markings or wards which you would expect from an Elvish temple. 
    To the west there is a stone door.
    To the east there is an open archway, you can hear running water coming from within.
    To the north there is a huge stone door. With a lot of effort you may be able to open it.
    """
    print description
    while playing:
        dog_events()
        prompt = raw_input("> ")

        if "help" in prompt.lower():
            game_help()
    
        elif "cls" in prompt.lower():
            cls()

        elif "look" in prompt.lower():
            print description

        elif prompt.lower() == "go north":
            print "large_room()"

        elif prompt.lower() == "go west":
            statue_room()
            playing = False
        
        elif prompt.lower() == "go east":
            print "fountain_room()"

        elif prompt.lower() == "go south":
            print "I have waited for this moment all my life. No way am I turning back now."
        
        else:
            print "I don't understand what you mean."

def statue_room():
    playing = True
    description = """
    This room appears to be some sort of a shrine to the Maker. The statue itself take up half of 
    the room. The Maker looks down at you like an unwelcome guest. It just occurred to me that it
    is maybe unusual that the torches are all still lit in this building after thousands of years.
    The elves are long gone but their magic is still strong it seems. 

    Just at the statue's feet you see a basket with some kind of token. A tribute to the Maker perhaps?

    There is nowhere to go but back into the entrance chamber to the east. 
    """
    print description
    while playing:
        dog_events()
        prompt = raw_input("> ")

        if "help" in prompt.lower():
            game_help()
    
        elif "cls" in prompt.lower():
            cls()

        elif "look" in prompt.lower():
            print description

        elif prompt.lower() == "go east":
            entrance_room()
            playing = False
        
        elif "take token" in prompt or "take tribute" in prompt:
            print "You pick up the token and place it in your backpack."
            invent.append("token")


start()
entrance_room()



