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
    
    #print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    
    #input("\n\n Press any key to continue...")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
        
    else: 
        print(err)
        
#The cursor being defined | comments are basically thoughts
cursor = db.cursor()


#Defining the main menu
def show_menu():
    print("\nMenu:")
    print("1. View Books")
    print("2. View Store Locations")
    print("3. My Account")
    print("4. Exit Program")
    

#method for show books | Should work on a cleaner output? But how?
def show_books(cursor):
    cursor.execute("SELECT book_id, book_name, author, details FROM book;")
    books = cursor.fetchall()
    
    print("\nHere are the books that we have!:")
    for book in books:
        book_id, book_name, author, details = book
        print("Book ID: {}, Book Name: {}, Author: {}, Details: {}".format(book_id, book_name, author, details))
        
        
#method for show locations | I think this looks right for the output?
def show_locations(cursor):
    cursor.execute("SELECT store_id, locale FROM store;")
    locations = cursor.fetchall()
    
    print("\nOur Store Locations!:")
    for location in locations:
        store_id, locale = location
        print("Store ID: {}, Location Address: {}".format(store_id, locale))


#method for validate user | Should work on looping if user not in table. But this works :)
def validate_user():
    while True:
        user_id = input("\nEnter your user_id: ")
        cursor.execute("SELECT COUNT(*) FROM user WHERE user_id = %s", (user_id,))
        count = cursor.fetchone()[0]
        if count > 0:
            return user_id
        else:
            print("Invalid user_id. Please try again.")


#method for show account menu
def show_account_menu():
    print("\nAccount Menu:")
    print("1. Wishlist")
    print("2. Add Book")
    print("3. Main Menu")


#method for show wishlist
def show_wishlist(cursor, user_id):
    #query here because some reason it works lol
    query = """
    SELECT book.book_id, book_name, author, details
    FROM user
    INNER JOIN wishlist ON user.user_id = wishlist.user_id
    INNER JOIN book ON wishlist.book_id = book.book_id
    WHERE user.user_id = %s
    """
    cursor.execute(query, (user_id,))
    wishlist = cursor.fetchall()
    print("\nHere Is Your Wishlist For User" + user_id + "!:")
    for book in wishlist:
        book_id, book_name, author, details = book
        print("Book ID: {}, Book Name: {}, Author: {}, Details: {}".format(book_id, book_name, author, details))


#method for show books to add



#method for add book to wishlist




#Main program!
while True:
    show_menu()
    pick = input("\nPlease pick a number (1-4): ")

    
    if pick == '1':
        show_books(cursor)
    elif pick == '2':
        show_locations(cursor)
    elif pick == '3':
        #Please don't forget to validate the user before this
        user_id = validate_user()
        #After user is validated
        while True:
            show_account_menu()
            account_pick = input("\n Please pick a number (1-3): ")
            
            if account_pick == '1':
                show_wishlist(cursor, user_id)
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