# database.py
import sqlite3


def initialize_database():
    conn = sqlite3.connect("highscore.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS highscore (
            id INTEGER PRIMARY KEY,
            score INTEGER
        )
    """
    )
    cursor.execute("SELECT * FROM highscore WHERE id = 1")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO highscore (id, score) VALUES (1, 0)")
    conn.commit()
    conn.close()


def load_high_score():
    conn = sqlite3.connect("highscore.db")
    cursor = conn.cursor()
    cursor.execute("SELECT score FROM highscore WHERE id = 1")
    row = cursor.fetchone()
    conn.close()
    return row[0] if row is not None else 0


def save_high_score(new_score):
    conn = sqlite3.connect("highscore.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE highscore SET score = ? WHERE id = 1", (new_score,))
    conn.commit()
    conn.close()
