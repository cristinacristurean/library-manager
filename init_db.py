### Initializes all required databases when running the software for the first time ###

import os # Operating System
import sqlite3

def init_db(): # Checks if the databases exist in the software directory; if not (e.g. running it the first time), creates databases
    print("Initializing databases...")

    if not os.path.exists("users.db"): # Users database
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Password TEXT NOT NULL
            )
        """)
        connection.commit()
        connection.close()

    if not os.path.exists("library.db"): # Library database
        connection = sqlite3.connect("library.db")
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Library (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                UserID INTEGER,
                Title TEXT,
                Author TEXT,
                Year TEXT,
                FOREIGN KEY(UserID) REFERENCES Users(ID)
            )
        """)
        connection.commit()
        connection.close()

    if not os.path.exists("reading_list.db"): # Reading list database
        connection = sqlite3.connect("reading_list.db")
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ReadingList (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                UserID INTEGER,
                Title TEXT,
                Status TEXT CHECK(Status IN ('Not Started', 'In Progress', 'Read')) DEFAULT 'Not Started',
                FOREIGN KEY(UserID) REFERENCES Users(ID)
            )
        """)
        connection.commit()
        connection.close()
    print("Finished initializing.")


if __name__ == "__main__":
    init_db()
    print("Databases initialized.")