print("""You enter a dark room with two doors. Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    elif insanity == "2":
        print("You are struck with a lightning bolt of brilliance!")
        print("You sore far into the sky.")
        print("Upon reaching a city of cloud you are confronted by a guard.")
        print("'You may only pass if you know the true answer.'")
        print("How old am I?")

        guess = input(" >")

        if guess <= 100:
            print("You are sent to a fiery abyss. You believe him to be but a baby?")
        elif guess >= 100:
            print("You have no concept of time young one.\n please leave and never return.")
        elif guess == str:
            print("That is correct there is no concept of numerals nor time here.")
        else:
            print("You may die now. Your time has come smart one.")
            print("Good job!")

    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good Job!")
