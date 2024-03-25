import sqlite3


def create_database():
    conn = sqlite3.connect("bot_execs.db")
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS bot_execs (
                id INTEGER PRIMARY KEY,
                start_time TIMESTAMP NOT NULL,
                duration INTEGER NOT NULL,
                start_number INTEGER NET NULL
                )''')
    
    conn.commit()
    conn.close()
