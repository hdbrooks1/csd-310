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
    print()
#    input("\n\n Press any key to continue...")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
        
    else: 
        print(err)


#Insert into player
cursor = db.cursor()
cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1);")


#Display players after inserting a player
cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id ASC;")
players = cursor.fetchall()


print("-- DISPLAYING PLAYERs AFTER INSERT --")
for player in players:
    player_id, first_name, last_name, team_name = player  # Assign values to individual variables
    print("Player ID: {}".format(player_id))
    print("First Name: {}".format(first_name))
    print("Last Name: {}".format(last_name))
    print("Team Name: {}".format(team_name))
    print()


#update the player
cursor = db.cursor()
cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")


#Display players after update
cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id ASC;")
players = cursor.fetchall()


print("-- DISPLAYING PLAYERs AFTER UPDATE --")
for player in players:
    player_id, first_name, last_name, team_name = player  # Assign values to individual variables
    print("Player ID: {}".format(player_id))
    print("First Name: {}".format(first_name))
    print("Last Name: {}".format(last_name))
    print("Team Name: {}".format(team_name))
    print()


#remove the player
cursor = db.cursor()
cursor.execute("DELETE FROM player WHERE first_name = 'Gollum';")


#Display players after player has been removed
cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id ASC;")
players = cursor.fetchall()


print("-- DISPLAYING PLAYERS AFTER DELETE --")
for player in players:
    player_id, first_name, last_name, team_name = player  # Assign values to individual variables
    print("Player ID: {}".format(player_id))
    print("First Name: {}".format(first_name))
    print("Last Name: {}".format(last_name))
    print("Team Name: {}".format(team_name))
    print()