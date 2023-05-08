import sqlite3

def create_connection():
    conn = sqlite3.connect('travel_bot.db')
    return conn

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        age INTEGER,
                        gender TEXT,
                        visited_places TEXT,
                        preferred_trip_type TEXT,
                        phone TEXT,
                        email TEXT
                      )''')

    conn.commit()

def init_database():
    conn = create_connection()
    create_tables(conn)
    conn.close()

if __name__ == '__main__':
    init_database()
