### Entry point of the app ###
from init_db import init_db
from login_page import login_page

def main():
    init_db()
    print("Welcome!")
    login_page()

if __name__ == "__main__":
    main()

