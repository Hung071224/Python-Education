



character_level : input("input your character level: ")
skills = [ {"Name" : "Tackle", "Minimum level": 1, "Damage": 5, "Hit rate": 0.3}, {"Name": "Quick Attack", "Minimum level": 2, "Damage": 3, "Hit rate": 0.5}, {"Name": "Strong Kick", "Minimum level": 4, "Damage": 9, "Hit rate": 0.2} ]

print("Chosse skill by number: ") 
for i in range(len(skills)):
    print("skill",i + 1, ":", skills[i]["Name"])

choice = int(input()) 
skill = skills[choice - 1]

if character_level < skill["minium level"]:
    print("you chose", skill["Name"])
    print("cannot deploy. Required level:",skill["minium level]"])
else:
    print("you chose", skill["Name"])
    import random 
    chance = random.random()
    if chance < skill["Hit rate"]:
        print("damage: ",skill["damage"])
    else:
        print("missed.")





















































