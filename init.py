import pymysql
import pymysql.cursors

con = pymysql.connect(host='localhost',
                              port=3306,
                              user="user1",
                              password="Password@123",
                              db='neversummer0',
                              cursorclass=pymysql.cursors.DictCursor)

if(con.open):
    print("Connected")
else:
    print("Failed to connect")

# filenames = ["SERVER", "Class", "Class_Weapons", "Location", "NPC_Gender", "NPC", "Item ", "Player", "BUY", "Player_Achievements", "OWNED_BY", "Dungeon", "Dungeon_Mob", "Boss", "Boss_Attacks", "DROPS", "DAMAGE", "TRADE"]
filenames = ["SERVER", "Class", "Class_Weapons", "Location", "NPC_Gender"]

cmd = "INSERT INTO {} VALUES ("
with con.cursor() as cur:
    for filename in filenames:
        file = open('data/' + filename + '.csv', 'r')
        for line in file.readlines():
            query = cmd.format(filename)
            line = line.strip()
            if line == "":
                continue
            query += line
            query += ")"
            print(query)
            cur.execute(query)
            con.commit()