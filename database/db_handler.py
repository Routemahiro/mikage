import sqlite3
import os

DB_DIR = 'database/data'
DB_PATH = os.path.join(DB_DIR, 'mikage_timer.db')

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(DB_PATH)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

    return connection

def start_pomodoro_session(start_time):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO PomodoroSession (start_time)
        VALUES (?)
    ''', (start_time,))

    connection.commit()
    session_id = cursor.lastrowid
    connection.close()

    return session_id

def end_pomodoro_session(session_id, end_time, ai_comment):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('''
        UPDATE PomodoroSession 
        SET end_time = ?, ai_comment = ? 
        WHERE session_id = ?
    ''', (end_time, ai_comment, session_id))

    connection.commit()
    connection.close()
