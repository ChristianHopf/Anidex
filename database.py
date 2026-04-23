import sqlite3

DB_PATH = "anime_data.db"

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    return connection

def initialize_db():
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS anime (
                       mal_id INTEGER PRIMARY KEY,
                       title TEXT,
                       score REAL,
                       year INTEGER
                   )
                   """
    )
    
    connection.commit()
    connection.close()