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
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT OR IGNORE INTO selected_companions (user_id, companion_id)
        VALUES (?, ?)
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
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT companion_id FROM selected_companions WHERE user_id = ?
    ''', (user_id,))

    companions = [row[0] for row in cursor.fetchall()]
    conn.close()

    return companions


def create_selected_companions_table():
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS selected_companions (
            user_id INTEGER,
            companion_id INTEGER,
            PRIMARY KEY (user_id, companion_id)
        )
    ''')

    conn.commit()
    conn.close()


def get_companion_by_id(companion_id):
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM users WHERE id = ?''', (companion_id,))
    user = cursor.fetchone()
    return user

def remove_selected_companion(user_id, companion_id):
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM selected_companions WHERE user_id = ? AND companion_id = ?', (user_id, companion_id))

    conn.commit()
    conn.close()

def get_chat_id_by_user_id(user_id):
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()

    cursor.execute("SELECT chat_id FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return None

def get_user_by_id(user_id):
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()

    return result



create_selected_companions_table()

if __name__ == "__main__":
    connection = create_connection()
    create_tables(connection)

    connection.close()