import sqlite3
from .models.pomodoro_models import PomodoroSession, WindowActivity

class PomodoroDBController:

    def __init__(self, db_path):
        self.db_path = db_path

    def add_pomodoro_session(self, start_time, end_time, ai_comment):
        session = PomodoroSession(start_time, end_time, ai_comment)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO pomodoro_sessions (start_time, end_time, ai_comment)
            VALUES (?, ?, ?)
            """, (session.start_time, session.end_time, session.ai_comment))
        conn.commit()
        session.id = cursor.lastrowid
        conn.close()
        return session.id

    def get_pomodoro_session(self, session_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM pomodoro_sessions WHERE session_id = ?
            """, (session_id,))
        row = cursor.fetchone()
        conn.close()
        if row is None:
            return None
        return PomodoroSession(*row)

    # Add similar methods for WindowActivity model
    # ...
