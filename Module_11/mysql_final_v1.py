import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    
    #input("\n\n Press any key to continue...")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
        
    else: 
        print(err)
        
#The cursor being defined
cursor = db.cursor()


#Defining the main menu
def show_menu():
    print("\nMenu:")
    print("1. View Books")
    print("2. View Store Locations")
    print("3. My Account")
    print("4. Exit Program")
    
#method for show books


#method for show locations


#method for validate user


#method for show account menu
def show_account_menu():
    print("\nAccount Menu:")
    print("1. Wishlist")
    print("2. Add Book")
    print("3. Main Menu")

#method for show wishlist


#method for show books to add


#method for add book to wishlist




#Main program!

while True:
    show_menu()
    pick = input("\nPlease pick a number (1-4): ")

    
    if pick == '1':
        print("\nThis is 1 where it shows stuff")
    elif pick == '2':
        print("\nShow stuff for 2 here")
    elif pick == '3':
        #Please don't forget to validate the user before this
        
        #After user is validated
        while True:
            show_account_menu()
            account_pick = input("\n Please pick a number (1-3): ")
            
            if account_pick == '1':
                print("\nThis is 1 where it shows stuff")
            elif account_pick == '2':
                print("\nShow stuff for 2 here")
            elif account_pick == '3':
                break
            else:
                print("Your choice is invalid. Please try again.")
        
        
        
    elif pick == '4':
        break
    else:
        print("Your choice is invalid. Please try again.")
    

#Close the connection and cursor
cursor.close()
db.close()