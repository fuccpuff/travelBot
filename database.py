import sqlite3

def create_connection():
    conn = sqlite3.connect("travel_buddy.db")
    return conn

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            countries_cities TEXT,
            travel_type TEXT,
            contact_info TEXT
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

def delete_profile_from_db(chat_id):
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE chat_id=?", (chat_id,))
    conn.commit()
    conn.close()


def add_selected_companion(user_id, companion_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO selected_companions (user_id, companion_id) VALUES (?, ?)
    ''', (user_id, companion_id))
    conn.commit()
    conn.close()

def remove_selected_companion(user_id, companion_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM selected_companions WHERE user_id = ? AND companion_id = ?', (user_id, companion_id))
    conn.commit()
    conn.close()

def get_selected_companions(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT companion_id FROM selected_companions WHERE user_id = ?', (user_id,))
    companions = cursor.fetchall()
    conn.close()
    return companions

def create_selected_companions_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS selected_companions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            companion_id INTEGER,
            UNIQUE(user_id, companion_id)
        )
    ''')
    conn.commit()
    conn.close()

create_selected_companions_table()

if __name__ == "__main__":
    connection = create_connection()
    create_tables(connection)

    connection.close()
