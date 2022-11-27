filenames = ["SERVER", "Class", "Class Weapons", "Location", "NPC_Gender", "NPC", "Item ", "Player", "BUY", "Player_Achievements", "OWNED_BY", "Dungeon", "Dungeon_Mob", "Boss", "Boss_Attacks", "Drop", "Damage", "TRADE"]

cmd = "INSERT INTO {} VALUES"

for filename in filenames:
    file = open('data/' + filename + '.csv', 'r')
    for line in file.readlines():
        print(line.split(','))