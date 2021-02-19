import sqlite3
import os

DB_FILE_PATH = "messages.db"

def initialize_db(app):
    if (not os.path.isfile(DB_FILE_PATH)) or os.stat(DB_FILE_PATH).st_size == 0:
        connection = get_connection()
        connection.execute('''CREATE TABLE MESSAGES
                (id INTEGER PRIMARY KEY,
                sender TEXT NOT NULL,
                message INT NOT NULL
                );''')
        connection.commit()


def get_connection():
    connection = sqlite3.connect(DB_FILE_PATH)
    connection.row_factory = sqlite3.Row
    return connection