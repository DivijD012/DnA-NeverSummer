import subprocess as sp
import pymysql
import pymysql.cursors
import bloat
from precog import *
from gamedesigner import *
from botwork import *


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        precog_menu(cur, con)
    elif(ch == 2):
        game_designer_menu(cur, con)
    elif(ch == 3):
        botwork_menu(cur, con)
    else:
        print("Error: Invalid Option")


# Global

bloat.print_title()


while(1):
    # tmp = sp.call('clear  ', shell=True)

    # Can be skipped if you want to hardcode username and password
    # username = input("Username: ")
    # password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user="user1",
                              password="Password@123",
                              db='neversummer0',
                              cursorclass=pymysql.cursors.DictCursor)
    #    tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                #tmp = sp.call('clear', shell=True)
                # Select what type of user you are
                print("1. Precog")  # Precog
                print("2. GameDesigner")  # Fire an Employee
                print("3. BotWork")  # Promote Employee
                print("4. Logout")
                ch = int(input("Enter choice> "))
                #tmp = sp.call('clear', shell=True)
                if ch == 4:
                    exit()
                else:
                    dispatch(ch)
                    # tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
     #   tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE    >")

