import sqlite3
from pathlib import Path

from app.models.memory_models import Message


DB_PATH = Path(__file__).resolve().parents[2] / "memory.db"


class MemoryService:

    def __init__(self):

        self.conn = sqlite3.connect(
            DB_PATH,
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS conversation (

                session_id TEXT,
                role TEXT,
                content TEXT

            )
            """
        )

        self.conn.commit()

    def save(self, session_id: str, role: str, content: str):

        self.cursor.execute(
            """
            INSERT INTO conversation VALUES (?,?,?)
            """,
            (session_id, role, content)
        )

        self.conn.commit()

    def history(self, session_id: str, limit: int = 10):

        self.cursor.execute(
            """
            SELECT role, content
            FROM conversation
            WHERE session_id=?
            ORDER BY rowid DESC
            LIMIT ?
            """,
            (session_id, limit)
        )

        rows = self.cursor.fetchall()[::-1]

        return [
            Message(role=r, content=c)
            for r, c in rows
        ]

    def clear(self, session_id: str):

        self.cursor.execute(
            """
            DELETE FROM conversation
            WHERE session_id=?
            """,
            (session_id,)
        )

        self.conn.commit()