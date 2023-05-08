import sqlite3

def create_connection():
    conn = sqlite3.connect("travel_buddy.db")
    return conn

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL UNIQUE,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        gender TEXT NOT NULL,
        countries_visited TEXT,
        countries_wishlist TEXT,
        travel_type TEXT NOT NULL,
        phone_number TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_search (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        travel_type TEXT NOT NULL,
        destination TEXT NOT NULL,
        travel_dates TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_matches (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        match_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (user_id),
        FOREIGN KEY (match_id) REFERENCES users (user_id)
    )
    """)

    conn.commit()

if __name__ == "__main__":
    connection = create_connection()
    create_tables(connection)
    connection.close()
