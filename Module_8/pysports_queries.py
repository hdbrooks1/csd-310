import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Pa55w0rd1!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    
    input("\n\n Press any key to continue...")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
        
    else: 
        print(err)


#Team Table Stuff
cursor = db.cursor()
cursor.execute("SELECT team_id, team_name, mascot FROM team")
teams = cursor.fetchall()

print("-- DISPLAYING TEAM RECORDS --")
for team in teams:
    team_id, team_name, mascot = team
    print("Team ID: {}".format(team_id))
    print("Team Name: {}".format(team_name))
    print("Mascot: {}".format(mascot))
    print()


#Player Table Stuff
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()


print("-- DISPLAYING PLAYER RECORDS --")
for player in players:
    player_id, first_name, last_name, team_id = player  # Assign values to individual variables
    print("Player ID: {}".format(player_id))
    print("First Name: {}".format(first_name))
    print("Last Name: {}".format(last_name))
    print("Team ID: {}".format(team_id))
    print()