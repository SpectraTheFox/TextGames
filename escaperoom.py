from cgitb import lookup
import inquirer
import random
import time

print("Would You like to play a game? (y/n)")
yn = input()

whatdoquestions = [
    inquirer.List('whatdo',
                message="What do you do?",
                choices=['Look around', 'Use an Item', 'Inspect and object', 'Give up']
            )
]
lookquestions = [
    inquirer.List('lookaround',
                message="What direction do you look?",
                choices=['Up', 'Down', 'Left', 'Right', 'Back', 'Forward']
            )
]

inspectquestions = [
    inquirer.List('inspect',
                message="What do you inspect?",
                choices=['Circut Breaker Box', 'Toolbox', 'Light', 'Chain', 'Door', 'Window']
            )
]

escaped = False
free = False
inventory = []
if yn == "y":
    print("What is your name?")
    name = input()
    print(f"Hello {name}. Welcome to the most dangerous game!")
    time.sleep(1)
    print("You awake in a dark room. You have no idea how you got here. THe only thing you know is that you must escape.")
    time.sleep(1)
    while escaped == False:
        whatdo = inquirer.prompt(whatdoquestions)
        if whatdo['whatdo'] == "Look around":
            lookup = inquirer.prompt(lookquestions)
            if lookup['lookaround'] == "Up":
                print("You look up and see a light sitting in the ceiling.")
                time.sleep(1)
                print("You try to reach for it but you can't reach it.")
                time.sleep(1)
            elif lookup['lookaround'] == "Down":
                print("You look down and see a chain connected to the floor holding you to the ground.")
                time.sleep(1)
                print("You see a lock on the chain and try to unlock it but it's locked.")
                time.sleep(1)
            elif lookup['lookaround'] == "Left":
                print("You look to your left and see a door.")
                time.sleep(1)
                print("You try to open the door but the chain holding you down keeps you from reaching it.")
                time.sleep(1)
            elif lookup['lookaround'] == "Right":
                print("You look to your right and see a toolbox with a word combination lock on it.")
                time.sleep(1)
                print("You try to open the lock but it's locked.")
                time.sleep(1)
            elif lookup['lookaround'] == "Back":
                print("You look behind you and see a window. It is boarded up.")
                time.sleep(1)
                print("You try to break the boards but they are too strong.")
                time.sleep(1)
            elif lookup['lookaround'] == "Forward":
                print("You look forward and see a circut breaker box.")
                time.sleep(1)
        elif whatdo['whatdo'] == "Use an Item":
            print("What would you like to use?")
            time.sleep(1)
            print("You have {inventory} in your inventory.")
            if inventory == []:
                print("You have nothing in your inventory.")
            else:
                useitem = input()
            time.sleep(1)
        elif whatdo['whatdo'] == "Inspect an object":
            inspect = inquirer.prompt(inspectquestions)
            if inspect['inspect'] == "Circut Breaker Box":
                print("The box opens and a piece of paper falls out.")
                time.sleep(1)
                print("The paper reads: 'What can you put in a bucket to make it weigh less?'")
                time.sleep(1)
            if inspect['inspect'] == "Toolbox":
                print("The toolbox is locked. with a combination lock. what is the combination?")
                inputkey = input()
                if inputkey == "hole":
                    print("The lock opens and you find a key.")
                    time.sleep(1)
                    inventory.append("Key")
                    time.sleep(1)
                else:
                    print("The lock doesn't open.")
                    time.sleep(1)
            if inspect['inspect'] == "Light":
                print("The light is too high to reach.")
                time.sleep(1)
            if inspect['inspect'] == "Chain":
                print("The chain is locked to the floor.")
                time.sleep(1)
                if "Key" in inventory:
                    print("You use the key to unlock the chain.")
                    time.sleep(1)
                    print("You are now free to move around the room.")
                    free = True
                    time.sleep(1)
            if inspect['inspect'] == "Door":
                print("The door is locked.")
                time.sleep(1)
                if "Key" in inventory:
                    print("You use the key to unlock the door.")
                    time.sleep(1)
                    print("You are now free! Thanks for playing!")
                    escaped = True
                    exit()

            if inspect['inspect'] == "Window":
                print("The window is boarded up.")
                time.sleep(1)
                if "Hammer" in inventory:
                    print("You use the hammer to break the boards.")
                    time.sleep(1)
                    print("You are now free")
                    escaped = True
                    time.sleep(1)
        elif whatdo['whatdo'] == "Give up":
            print("You give up and die.")
            time.sleep(1)
            print("Goodbye!")
            exit()

else:
    print("Goodbye!")
    exit()