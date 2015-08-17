# This is a quick text adventure I have made as a learning project and as homework for the LPTHW book.
# It is going to be a fairly basic text adventure with standard commands such as go north, look and i for inventory. 
# The pet companion can be interacted with also.
from sys import exit

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
            print "statue_room()"
        
        elif prompt.lower() == "go east":
            print "fountain_room()"

        elif prompt.lower() == "go south":
            print "I have waited for this moment all my life. No way am I turning back now."
        
        else:
            print "I don't understand what you mean."

    



entrance_room()



