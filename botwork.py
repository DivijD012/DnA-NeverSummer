import subprocess as sp
from bloat import *
from tabulate import tabulate

def IntegerCheck(i):
    try:
        float(i)
    except ValueError:
        print("Enter Valid intger value")
        return 1
    return 0

cur = 1
con = 2
def delete_expired_items():
    global cur, con
    print("Delete limited items after it's time is expired")
    Item_Id = input("Enter Item ID : ")
    try:
        # code here
        cmd = "delete from Item where Item_ID={} ;".format(Item_Id)
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
    tmp = input("Enter any key to CONTINUE>")
    pass

def delete_expired_bosses():
    global cur, con
    print("Delete limited time bosses after their time is expired")
    DungeonName = input("Enter the Name of the Dungeon that had the Boss: ")
    BossName = input("Enter Boss Name: ")
    try:
        # code here
        cmd = "delete from Boss where Dungeon_name='" + DungeonName.strip() 
        cmd += "'and Name='" + BossName.strip() +"' ;"
        print(cmd)
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def delete_account():
    global cur, con
    print("Delete a player's data who deletes their account")
    PlayerID = input("Enter Player ID: ")
    try:
        cmd = "Delete from Player where player_id=" + PlayerID + " ;";
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
    
    tmp = input("Enter any key to CONTINUE>")

def delete_expired_locations():
    global cur, con
    print("Delete a limited time location after it's time is expired")
    LocationID = input("Enter Location ID: ")
    try:
        # code here
        cmd = "Delete from Location where Location_id=" + LocationID + " ;";
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def update_player_spending():
    global cur, con
    print("Update player's total spending and currency_owned")
    PlayerID = input("Enter Player ID: ")
    NewSpending = input("Enter the player's new spending: ")
    if (IntegerCheck(NewSpending)):
        update_player_spending()
        return
    NewCurrencyGemsOwned = input("Enter the new currency gems owned: ") 
    if (IntegerCheck(NewCurrencyGemsOwned)):
        update_player_spending()
        return
    NewCurrencyGoldOwned = input("Enter the new currency gold owned: ")  
    if (IntegerCheck(NewCurrencyGoldOwned)):
        update_player_spending()
        return 
    try:
        # code here
        cmd = "Update Player set money_spent=" + NewSpending 
        cmd += " ,in_game_currency_gems=" + NewCurrencyGemsOwned
        cmd += " ,in_game_currency_gold=" + NewCurrencyGoldOwned 
        cmd += " where player_id=" + PlayerID + ";"
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
        if not (isinstance(NewSpending,int) and isinstance(NewCurrencyGemsOwned,int) and isinstance(NewCurrencyGoldOwned,int)):
            print("Enter Valid intger values")
    tmp = input("Enter any key to CONTINUE>")

def update_player_count():
    global cur, con
    print("Update server player count")
    ServerIP = input("Enter Server IP:")
    NewPlayerCOunt = input("New Player Count: ")
    if (IntegerCheck(NewPlayerCOunt)):
        update_player_count()
        return
    try:
        # code here
        cmd = "update SERVER set Player_count=" + NewPlayerCOunt
        cmd += " where IP='" + ServerIP + "' ;"
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
        if not (isinstance(NewPlayerCOunt,int)):
            print("Enter Valid intger values")
    tmp = input("Enter any key to CONTINUE>")



def update_player_level():
    global cur, con
    print("Update player's level")
    PlayerID = input("Enter Player ID: ")
    NewLevel = input("Enter new level: ")
    if (IntegerCheck(NewLevel)):
        update_player_level()
        return
    try:
        # code here
        cmd = "Update Player set Level=" + NewLevel 
        cmd += " where player_id=" + PlayerID + ";"
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
        if not (isinstance(NewLevel,int)):
            print("Enter Valid intger values")
    tmp = input("Enter any key to CONTINUE>")

def insert_new_player():
    global cur, con
    print("Insert new player to Players")
    player_id = input("Enter Player ID: ")
    if (IntegerCheck(player_id)):
        insert_new_player()
        return
    country_code = input("Enter Country Code: ")
    if (IntegerCheck(country_code)):
        insert_new_player()
        return
    username = input("Enter Username: ")
    name = input("Enter Name: ")
    money_spent = input("Enter Money Spent: ")
    if (IntegerCheck(money_spent)):
        insert_new_player()
        return
    in_game_currency_gems = input("Enter currency_gems: ")
    if (IntegerCheck(in_game_currency_gems)):
        insert_new_player()
        return
    in_game_currency_gold = input("Enter currency_gold: ")
    if (IntegerCheck(in_game_currency_gold)):
        insert_new_player()
        return
    Level = input("Enter Player Level: ")
    if (IntegerCheck(Level)):
        insert_new_player()
        return
    Player_location = input("Enter Player Location: ")
    server_ip = input("Enter Player's Server IP: ")
    Class_name = input("Enter Player's Class Name: ")
    try:
        # code here
        cmd = "insert into Player Values ("
        cmd += player_id + ","
        cmd += country_code + ",'"
        cmd += username + "','"
        cmd += name + "',"
        cmd += money_spent + ","
        cmd += in_game_currency_gems + ","
        cmd += in_game_currency_gold + ","
        cmd += Level + ",'"
        cmd += Player_location + "',"
        if server_ip == "NULL" :
            cmd += "NULL,"
        else:
            cmd += "'" + server_ip + "',"
        if Class_name == "NULL" :
            cmd += "NULL) ;"
        else:   
            cmd += "'" + Class_name + "') ;"
        cur.execute(cmd)
        con.commit()

        cmd = "insert into Player_Achievements values (" + player_id + ",'newbie') ; " 
        cur.execute(cmd)
        con.commit()
        pass
    except Exception as e:
        con.rollback()
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def dispatch_botwork(ch):
    global cur, con
    if(ch == 1):
        delete_expired_items()
    elif(ch == 2):
        delete_expired_bosses()
    elif(ch == 3):
        delete_account()
    elif(ch == 4):
        delete_expired_locations()
    elif(ch == 5):
        update_player_spending()
    elif(ch == 6):
        update_player_count()
    elif(ch == 7):
        update_player_level()
    elif(ch == 8):
        insert_new_player()
    else:
        print("Error: Invalid Option")

def botwork_menu(cur1, con1):
    global cur, con
    cur=cur1
    con=con1
    while(1):
        tmp = sp.call('clear', shell=True)
        print_bots()
        # Select what type of user you are
        print("0. Back")
        print("1. Delete limited items after it's time is expired")  
        print("2. Delete limited time bosses after their time is expired")  
        print("3. Delete a player's data who deletes their account") 
        print("4. Delete a limited time location after it's time is expired")
        print("5. Update player's total spending and currency_owned")
        print("6. Update server player count")
        print("7. Update player's level")
        print("8. Insert new player to Players")
        ch = int(input("Enter choice> "))
        tmp = sp.call('clear', shell=True)
        if ch == 0:
            return
        else:
            dispatch_botwork(ch)