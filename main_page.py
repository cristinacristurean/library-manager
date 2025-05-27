### Main page once logged in
from login_page import login_page
# from my_library import Library, display_library_page


# Function that displays the main page
def display_main_page(current_user):
    # Welcome message on the main page
    print(f"Welcome, {current_user}!")
    print()

    #Statistics
        #Books owned
        #Read books
        #Last read book
        #Last added book
        #Currently reading
    #Accessing the sub-pages: Library, Reading List, Account Settings + log-out option
    print("1. My Library")
    print("2. My Reading List")
    print("3. Account Settings")
    print("4. Log Out")
    print()
    mp_user_choice = input("What would you like to access? ")

    if mp_user_choice == "1": #ACCESS MY LIBRARY PAGE
        print("Library page loading...")
        # display_library_page()
    elif mp_user_choice == "2": #ACCESS MY READING LIST PAGE
        print("Reading List page loading...")
        # call my_reading_list()
    elif mp_user_choice == "3": #ACCESS ACCOUNT SETTINGS PAGE
        print("Account Settings page loading...")
        # call account_settings()
    elif mp_user_choice == "4": #LOG OUT
        print("Logging out...")
        login_page()
    else:
        print("Invalid choice. Please try again.")