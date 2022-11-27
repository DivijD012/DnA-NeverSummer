import subprocess as sp
from tabulate import tabulate
cur = 1
con = 2
def insert_items():
    global cur, con
    print("Insert Items")
    nat = input("Enter nation")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")
    pass

def insert_dungeon():
    global cur, con
    print("Insert Dungeon")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def insert_boss():
    global cur, con
    print("Insert Boss")
    try:
        cmd = "select * from SERVER"
        cur.execute(cmd)
        rows = cur.fetchall()
        print(tabulate(rows))
        pass
    except Exception as e:
        print (e)
    
    tmp = input("Enter any key to CONTINUE>")

def insert_npc():
    global cur, con
    print("Insert NPC")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def update_rarity():
    global cur, con
    print("UPdate rarity")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def update_boss_difficulty():
    global cur, con
    print("UPdate boss difficulty")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def update_dungeon_lvl_req():
    global cur, con
    print("Update dungeon’s min_level_requirement")
    try:
        # code here
        pass
    except Exception as e:
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