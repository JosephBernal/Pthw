from sys import exit

def start():
    print("You were sent here to return something of value to the king.")
    print("This house is dark and full of terrors.")
    print("What do you do?")
    first_room()


def first_room():
    print("What do you do?")

    choice = input("> ")

    if "look" in choice:
        print("You see a taxidermied bear. He looks mean.")
        print("There is a life-size hourglass")
        print("and there are two doors.")
        first_room()

    elif ("walk" or "open") and "door" and "1" in choice:
        print("The door squeaks open.")
        fight_room()

    elif ("walk" or "open" or "door") and "2" in choice:
        print("The door swings open with much aplumb.")
        troll_room()

    elif choice is "3":
        raise AssertionError("You crazy.") 

    else:
        print("What're you on about?")
        first_room()


def fight_room():

    print("""'Why do I always have to be bothered?
    Everyone is always bothering me!
    I don't want to have to work.
    I don't want to do anything!'says a massive man baby.
    What do you do?""")

    choice = input("> ")

    if "pocket sand" in choice:
        print("""
        You spray pocket sand in that man baby's face.
        Blinded he complains more (if that was even possible.)
        He pushes passed you and runs out of the house.
        You move forward onto adventure!""")
        prince_room()
    else:
        print("""'Why doesn\'t anyone love me?'
        you can't stand his complaining and just leave""")
        first_room()

def troll_room():
    print("There is a troll in front of you who is crouched in a sinister fashion.")
    print("What do you do?")

    choice = input("> ")

    if "look" in choice:
        print("It looks like a Japanese garden indoors.")
        print("There is a bridge in the center of the room and a waterfall in the corner.")
        print("The aesthetic is quite peaceful if it weren't for the ugly troll.")
        troll_room()
    elif "ask" or "question" in choice:
        print("A riddle it is!")
        print("Who has two thumbs and hates riddles?")
        troll_riddle()
    else:
        print("The troll disappears and you walk around aimlessly for awhile...")
        print("Finally getting bored you return to the last room.")
        first_room()


def troll_riddle():
    choice = input("> ")
    if "me" or "author" or "coder" in choice:
        print("You solved my riddle.")
        print("You are very smart you know.")
        prince_room()
    else:
        print("Get out of my sight!")
        first_room()


def prince_room():

    print("""Yay you got to the prince!
    He is forever grateful.
    He would like to present you with a token
    of his appreciation.
    Do you accept?""")
    
    choice = input("y/n")

    while choice != "y":
        choice = "y"
        print("why you no like me?")
        print("I like you.")
        break

    print("The prince kisses you on the cheek.")




start()
