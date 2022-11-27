import subprocess as sp
from tabulate import tabulate
cur = 1
con = 2
def delete_expired_items():
    global cur, con
    print("Delete limited items after it's time is expired")
    nat = input("Enter nation")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")
    pass

def delete_expired_bosses():
    global cur, con
    print("Delete limited time bosses after their time is expired")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def delete_account():
    global cur, con
    print("Delete a player's data who deletes their account")
    try:
        cmd = "select * from SERVER"
        cur.execute(cmd)
        rows = cur.fetchall()
        print(tabulate(rows))
        pass
    except Exception as e:
        print (e)
    
    tmp = input("Enter any key to CONTINUE>")

def delete_expired_locations():
    global cur, con
    print("Delete a limited time location after it's time is expired")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def update_player_spending():
    global cur, con
    print("Update player's total spending and currency_owned")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def update_player_count():
    global cur, con
    print("Update server player count")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")



def update_player_level():
    global cur, con
    print("Update player's level")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def insert_new_player():
    global cur, con
    print("Insert new player to Players")
    try:
        # code here
        pass
    except Exception as e:
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