import inquirer
import random
import time

print("What is your name?")
name = input()
questions = [
    inquirer.List('weapon',
                message="What is your weapon?",
                choices=['Sword', 'Bow', 'Axe', 'Shortsword', "Staff"],
            ),
    inquirer.List('armor',
            message="What is your armor?",
            choices=['Leather', 'Chainmail', 'Plate', 'Cloth'],
        ),
            
]
answers = inquirer.prompt(questions)

hp = 100
damage = 0
enemyhp = 100
enemychoices = ["Goblin", "Orc", "Troll", "Dwarf"]
enemy = random.choice(enemychoices)
enemydamage = 8
hitchance = 2
enemyhit = 3

if answers['weapon'] == "Sword":
    damage = 10
    hitchance = 3
elif answers['weapon'] == "Bow":
    damage = 5
    hitchance = 2
elif answers['weapon'] == "Axe":
    damage = 15
    hitchance = 3
elif answers['weapon'] == "Shortsword": 
    damage = 7
    hitchance = 2
elif answers['weapon'] == "Staff":
    damage = 3
    hitchance = 4

if answers['armor'] == "Leather":
    hp = hp + 5
elif answers['armor'] == "Chainmail":
    hp = hp + 10
elif answers['armor'] == "Plate":
    hp = hp + 15
elif answers['armor'] == "Cloth":
    hp = hp + 3

print(f"Here are your stats:")
print("Weapon: " + answers['weapon'])
print("Armor: " + answers['armor'])
print("Starting health: 100")
print(f"You are now ready to fight!\n Your enemy is a {enemy}!\n")
time.sleep(1)
print("3!")
time.sleep(1)
print("2!")
time.sleep(1)
print("1!")
time.sleep(1)
print("Fight!")

while hp > 0 and enemyhp > 0:
    
    time.sleep(0.5)
    dohit = random.randint(1, hitchance)
    if dohit == 1 or dohit == 2:
        print("You Hit!")
        adddamagedone = random.randint(1, 5)
        print("You did " + str(damage + adddamagedone) + " damage!")
        enemyhp = enemyhp - (damage + adddamagedone)
        print("Enemy health: " + str(enemyhp))
    else:
        print("You Missed!")
    if enemyhp <= 0:
        print("You Win!")
        break
    enemyhit = random.randint(1, enemyhit)
    if enemyhit == 1 or enemyhit == 2:
        print("Enemy Hit!")
        adddamagedone = random.randint(1, 4)
        print("Enemy did " + str(enemydamage + adddamagedone) + " damage!")
        hp = hp - (enemydamage + adddamagedone)
        print("Your health: " + str(hp))
    else:
        print("Enemy Missed!")
    if hp <= 0:
        print("You Lose!")
        break