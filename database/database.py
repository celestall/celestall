import sqlite3

def initialize_db():
        conn = sqlite3.connect('bot_database.dp')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,   
                username TEXT, 
                first_name TEXT,
                last_name TEXT
            )
        ''')
        conn.commit()
        conn.close()

def add_user(user_id, username, first_name, last_name):
    conn = sqlite3.connect('bot_database.dp')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (user_id, username, first_name, last_name)
    VALUES (?, ?, ?, ?)
    ''', (user_id, username, first_name, last_name))
    conn.commit()
    conn.cursor()

def get_user(user_id):
    conn = sqlite3.connect('bot_database.dp')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE user_id = ? 
    ''', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user