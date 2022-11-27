import subprocess as sp
from tabulate import tabulate
import pymysql
import pymysql.cursors
import re
cur = 1
con = 2

def take_int(value):
    while(True):
        inp = input(value)
        if inp.lower() == "null":
            return inp
        try:
            i = int(inp)
            return i
        except:
            print("Enter a valid integer please")


def print_table(cmd):
    cur.execute(cmd)
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No results")
        return
    # print(rows)
    cols = [(i) for i in rows[0].keys()]
    rows2 = [[i[j] for j in cols] for i in rows]
    print(tabulate(rows2, cols))


def players_nation():
    global cur, con
    print("Player nation")
    try:
        nat = input("Enter location: ")
        print_table(f"select player_id , country_code,  username , name , in_game_currency_gems , in_game_currency_gold , Level , Class_name from Player where Player_location like '{re.escape(nat)}'")
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")
    pass

def get_whales():
    global cur, con
    print("whales")
    try:
        print_table(f"""SELECT player_id , country_code,  username , 
                        name , money_spent, Level , Class_name 
                        FROM Player
                        where money_spent >= 1000
                        ORDER BY money_spent DESC """)
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def traffic_sum():
    global cur, con
    # print("traffic sum")
    try:
        cmd = "select sum(Traffic) as Traffic_Sum from SERVER"
        print_table(cmd)
        pass
    except Exception as e:
        print (e)
    
    tmp = input("Enter any key to CONTINUE>")

def cuss():
    global cur, con
    print("cuss")
    try:
        cuss_wrd = input("Enter the cuss word: ")
        print_table(f""" SELECT player_id, username, name 
                   FROM Player
                   WHERE username like '%{re.escape(cuss_wrd)}%'
                   OR  name like '%{re.escape(cuss_wrd)}%'  """)
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def severwise_top_players():
    global cur, con
    print("Serverwise top players")
    try:
        s_loc = re.escape(input("Enter Server Location: "))
        print_table(f"""
            SELECT p1.player_id, p1.username, p1.name, p1.level, p1.class_name, count(p2.Achievements) as AchivementsCount
            FROM Player as p1, Player_Achievements as p2, SERVER
            WHERE p1.player_id = p2.player_id AND SERVER.ip = p1.server_ip
            AND SERVER.server_location like '{s_loc}'
            GROUP BY p1.player_id
            ORDER BY p1.level, AchivementsCount DESC
        """)
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def popular_classes():
    global cur, con
    print("Popular classes")
    try:
        print_table("""
            SELECT c.class_name as Class_Name, c.class_type as Class_Type,
                     count(p.Player_id) as Player_Count
            FROM Class as c, Player as p
            WHERE c.class_name = p.class_name
            GROUP BY c.class_name
            ORDER BY count(p.Player_id) DESC
        """)
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def popular_items():
    global cur, con
    print("Popular items")
    try:
        print_table("""
            SELECT i.item_id, i.item_name, i.rarity, cost, count(p.player_id) as Player_Count
            FROM Item as i, OWNED_BY as o, Player as p
            WHERE i.item_id = o.item_id and p.player_id = o.player_id
            GROUP BY i.item_id
            ORDER BY count(p.player_id) DESC
        """)
        pass
    except Exception as e:
        print (e)
    tmp = input("Enter any key to CONTINUE>")

def top_locations():
    global cur, con
    print("top locations")
    try:
        print_table("""
            SELECT Player_Location as Location, count(play er_id) as Player_Count
            FROM Player
            GROUP BY Player_Location
            ORDER BY count(player_id) DESC;
        """)
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

if __name__ == '__main__':
    con = pymysql.connect(host='localhost',
                              port=3306,
                              user="user1",
                              password="Password@123",
                              db='neversummer0',
                              cursorclass=pymysql.cursors.DictCursor)
    with con.cursor() as cur:
        precog_menu(cur, con)