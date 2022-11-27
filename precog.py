import subprocess as sp
from tabulate import tabulate
from bloat import *
cur = 1
con = 2
def players_nation():
    global cur, con
    print("player nation")
    nat = input("Enter nation")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")
    pass

def get_whales():
    global cur, con
    print("whales")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def traffic_sum():
    global cur, con
    print("traffic sum")
    try:
        cmd = "select * from SERVER"
        cur.execute(cmd)
        rows = cur.fetchall()
        print(tabulate(rows))
        pass
    except Exception as e:
        print (e)
    
    tmp = input("Enter any key to CONTINUE>")

def cuss():
    global cur, con
    print("cuss")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def severwise_top_players():
    global cur, con
    print("Serverwise top players")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def popular_classes():
    global cur, con
    print("Popular classes")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def popular_items():
    global cur, con
    print("Popular items")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def top_locations():
    global cur, con
    print("top locations")
    try:
        # code here
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def dispatch_precog(ch):
    global cur, con
    if(ch == 1):
        players_nation()
    elif(ch == 2):
        get_whales()
    elif(ch == 3):
        traffic_sum()
    elif(ch == 4):
        cuss()
    elif(ch == 5):
        severwise_top_players()
    elif(ch == 6):
        popular_classes()
    elif(ch == 7):
        popular_items()
    elif(ch == 8):
        top_locations()
    else:
        print("Error: Invalid Option")

def precog_menu(cur1, con1):
    global cur, con
    cur=cur1
    con=con1
    while(1):
        tmp = sp.call('clear', shell=True)
        print_precog()
        # Select what type of user you are
        print("0. Back")
        print("1. Get Players By nation")  
        print("2. Get Whales")  
        print("3. Traffic sum") 
        print("4. Cuss Like Names")
        print("5. Serverwise top players")
        print("6. popular classes")
        print("7. popular items")
        print("8. top locations")
        ch = int(input("Enter choice> "))
        tmp = sp.call('clear', shell=True)
        if ch == 0:
            return
        else:
            dispatch_precog(ch)