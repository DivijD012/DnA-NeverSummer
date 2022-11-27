import subprocess as sp
from tabulate import tabulate
import math
from bloat import *
cur = 1
con = 2
def insert_items():
    global cur, con
    print("Insert Items")
    item_id = input("Enter Item ID : ")
    item_name = input("Enter Item Name : ")
    print("Choose an Item Rarity from :")
    print("1. Common")
    print("2. Rare")
    print("3. Epic")
    print("4. Legendary")
    print("5. Mythic")
    while(1):
        rarity = input("Enter rarity b/w 1 to 5 : ")
        try:
            rarity = int(rarity)
        except:
            continue
        if(rarity < 1 or rarity > 5):
            print("Invalid rarity")
            continue
        else:
            break
        # if(not(math.isnan(rarity))):
        #     if(rarity > 5 or rarity < 1):
        #         print("Invalid Rarity")
        #         continue
        #     else:
        #         break
        # else:
        #     continue
    if(rarity == 1):
        rarity = "Common"
    elif(rarity == 2):
        rarity = "Rare"
    elif(rarity == 3):
        rarity = "Epic"
    elif(rarity == 4):
        rarity = "Legendary"
    elif(rarity == 5):
        rarity = "Mythic"
    while(1):
        cost = input("Enter the cost (positive number or 'NULL'):")
        try:
            cost = int(cost)
        except:
            continue
        if(cost < 0):
            print("Invalid cost")
            continue
        else:
            break
        # if(not(math.isnan(cost))):
        #     if(cost < 0):
        #         print("Invalid cost")
        #         continue
        #     else:
        #         break    
        # else:
        #     if(cost != 'NULL'):
        #         print("Invalid cost")
        #         continue
        #     else:
        #         break
    try:
        cmd = f"INSERT INTO Item VALUES ('{item_id}', '{item_name}', '{rarity}', {cost});"
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
    tmp = input("Enter any key to CONTINUE> ")
    pass

def insert_dungeon():
    global cur, con
    print("Insert Dungeon")
    name = input("Enter dungeon name : ")
    while(1):
        min_level_requirement = input("Enter the minimum level requirement: ")
        try:
            min_level_requirement = int(min_level_requirement)
        except:
            continue
        if(min_level_requirement < 0):
            print("Invalid minimum level requirement")
            continue
        else:
            break
    while(1):
        avg_clear_time = input("Enter the average clear time: ")
        try:
            avg_clear_time = int(avg_clear_time)
        except:
            continue
        if(avg_clear_time < 0):
            print("Invalid avg_clear_time")
            continue
        else:
            break
    while(1):
        party_size = input("Enter the maximum party size (4, 8 or 20): ")
        try:
            party_size = int(party_size)
        except:
            continue
        if(party_size != 4 and part_size != 8 and part_size != 20):
            print("Invalid party_size")
            continue
        else:
            break
    try:
        cmd = f"INSERT INTO Dungeon VALUES ('{name}', {min_level_requirement}, {avg_clear_time}, {party_size});"
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
    tmp = input("Enter any key to CONTINUE> ")

def insert_boss():
    global cur, con
    print("Insert Boss")
    d_name = input("Enter the dungeon name : ")
    boss_name = input("Enter the boss name : ")
    while(1):
        max_health = input("Enter the max_health : ")
        try:
            max_health = int(max_health)
        except:
            continue
        if(max_health < 0):
            print("Invalid max_health")
            continue
        else:
            break
    print("Choose a boss difficulty from :")
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")
    print("4. Advanced")
    while(1):
        difficulty = input("Enter difficulty b/w 1 to 4 :")
        try:
            difficulty = int(difficulty)
        except:
            continue
        if(difficulty < 0):
            print("Invalid difficulty")
            continue
        else:
            break
    if(difficulty == 1):
        difficulty = "Easy"
    elif(difficulty == 2):
        difficulty = "Normal"
    elif(difficulty == 3):
        difficulty = "Rare"
    elif(difficulty == 4):
        difficulty = "Advanced"
    try:
        cmd = f"INSERT INTO Boss VALUES ('{d_name}', '{boss_name}', {max_health}, '{difficulty}');"
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
    
    tmp = input("Enter any key to CONTINUE>")

def insert_npc():
    global cur, con
    print("Insert NPC")
    npc_name = input("Enter NPC name : ")
    while(1):
        locat_id = input("Enter the Location ID : ")
        try:
            locat_id = int(locat_id)
        except:
            continue
        if(locat_id < 0):
            print("Invalid locat_id")
            continue
        else:
            break
    print("Choose an NPC type from :")
    print("1. Trader NPC")
    print("2. Battle NPC")
    print("3. Idle NPC")
    print("4. Story NPC")
    while(1):
        npc_type = input("Enter NPC type b/w 1 to 4 : ")
        try:
            npc_type = int(npc_type)
        except:
            continue
        if(npc_type < 0):
            print("Invalid npc_type")
            continue
        else:
            break
    if(npc_type == 1):
        npc_type = "Trader NPC"
    elif(npc_type == 2):
        npc_type = "Battle NPC"
    elif(npc_type == 3):
        npc_type = "Idle NPC"
    elif(npc_type == 4):
        npc_type = "Story NPC"
    try:
        # code here
        cmd = f"INSERT INTO NPC VALUES ('{npc_name}', {locat_id}, '{npc_type}');"
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def update_rarity():
    global cur, con
    print("Update rarity")
    item_id = input("Enter item_id that you wish to update : ")
    print("Choose an Item Rarity from :")
    print("1. Common")
    print("2. Rare")
    print("3. Epic")
    print("4. Legendary")
    print("5. Mythic")
    while(1):
        rarity = input("Enter rarity b/w 1 to 5 : ")
        try:
            rarity = int(rarity)
        except:
            continue
        if(rarity < 1 or rarity > 5):
            print("Invalid rarity")
            continue
        else:
            break
    if(rarity == 1):
        rarity = "Common"
    elif(rarity == 2):
        rarity = "Rare"
    elif(rarity == 3):
        rarity = "Epic"
    elif(rarity == 4):
        rarity = "Legendary"
    elif(rarity == 5):
        rarity = "Mythic"
    try:
        # code here
        cmd = f"UPDATE Item SET Rarity='{rarity}' WHERE Item_ID = {item_id}"
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
    tmp = input("Enter any key to CONTINUE> ")

def update_boss_difficulty():
    global cur, con
    print("Update boss difficulty")
    boss_name = input("Enter boss_name that you wish to update : ")
    d_name = input("Enter dungeon name that you wish to update :")
    print("Choose a boss difficulty from :")
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")
    print("4. Advanced")
    while(1):
        diffic = input("Enter difficulty b/w 1 to 4 : ")
        try:
            diffic = int(diffic)
        except:
            continue
        if(diffic < 0):
            print("Invalid difficulty")
            continue
        else:
            break
    if(diffic == 1):
        diffic = "Easy"
    elif(diffic == 2):
        diffic = "Normal"
    elif(diffic == 3):
        diffic = "Hard"
    elif(diffic == 4):
        diffic = "Advanced"
    try:
        # code here
        cmd = f"UPDATE Boss SET difficulty='{diffic}' WHERE Dungeon_name = '{d_name}' AND Name = '{boss_name}'"
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def update_dungeon_lvl_req():
    global cur, con
    print("Update dungeons min_level_requirement")
    d_name = input("Enter the dungeon name : ")
    while(1):
        min_level_requirement = input("Enter the minimum level requirement (1 to 20) : ")
        try:
            min_level_requirement = int(min_level_requirement)
        except:
            continue
        if(min_level_requirement < 0):
            print("Invalid minimum level requirement")
            continue
        else:
            break
    try:
        # code here
        cmd = f"UPDATE Dungeon SET min_level_requirement={min_level_requirement} WHERE name = '{d_name}'"
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def dispatch_game_designer(ch):
    global cur, con
    if(ch == 1):
        insert_items()
    elif(ch == 2):
        insert_dungeon()
    elif(ch == 3):
        insert_boss()
    elif(ch == 4):
        insert_npc()
    elif(ch == 5):
        update_rarity()
    elif(ch == 6):
        update_boss_difficulty()
    elif(ch == 7):
        update_dungeon_lvl_req()
    else:
        print("Error: Invalid Option")

def game_designer_menu(cur1, con1):
    global cur, con
    cur=cur1
    con=con1
    while(1):
        tmp = sp.call('clear', shell=True)
        print_gamedev()
        # Select what type of user you are
        print("0. Back")
        print("1. Insert items")  
        print("2. Insert Dungeon")  
        print("3. Insert Boss") 
        print("4. Insert NPC")
        print("5. Update rarity of items")
        print("6. update boss difficulty")
        print("7. Update dungeon's min_level_requirement")
        ch = int(input("Enter choice> "))
        tmp = sp.call('clear', shell=True)
        if ch == 0:
            return
        else:
            dispatch_game_designer(ch)