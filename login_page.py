### Sign up and Log in page ###

import sqlite3
import sys


# Sign up function
def sign_up(new_user, new_password):
    connection = sqlite3.Connection("users.db")
    cursor = connection.cursor()

    # Verify if new username is already taken
    sql_script_new_user_verify = f'''SELECT * FROM Users WHERE Username = '{new_user}' '''
    cursor.execute(sql_script_new_user_verify)
    if cursor.fetchone():
        print("Username is taken.")
        connection.close()
        return

    # Create the new user
    sql_script_new_user_create = f'''INSERT INTO Users (Username, Password) VALUES ('{new_user}', '{new_password}'); '''
    cursor.execute(sql_script_new_user_create)
    connection.commit()
    print("User was successfully created!")
    connection.close()

# Log in function
def log_in(user, password):
    connection = sqlite3.Connection("users.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Users")
    rows = cursor.fetchall()

    connection.close()

    auth = False

    for row in rows:
        if user == row[1] and password == row[2]:
            auth = True
            return row[1]


    if auth:
        print("Logged in successfully!")
        #aici o sa adaug si functia sa ii deschida pagina cu toate alea
    else:
        print("Incorrect username or password!")




# Login/Sign Up Page
def login_page():
    while True:
        print("1. Sign Up")
        print("2. Log In")
        print("3. Quit")

        lp_user_choice = input("What would you like to do? ")
        if lp_user_choice == "1":
            new_user = input("Insert your new username: ")
            new_password = input("Insert your new password: ")
            sign_up(new_user, new_password)

        if lp_user_choice == "2":
            user = input("Enter your username: ")
            password = input("Enter your password: ")
            current_user = log_in(user, password)

            if current_user:
                import main_page
                main_page.display_main_page(current_user)
                break

        if lp_user_choice == "3":
            print("Goodbye!")
            sys.exit() # Closes the program
