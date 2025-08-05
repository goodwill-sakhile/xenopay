import hashlib
import sqlite3
import uuid
from utils.logger import log_event
from config.settings import DB_PATH


class UserManager:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._initialize_user_table()

    def _initialize_user_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                )
            """)
            conn.commit()
        log_event("UserManager", "User table initialized.")

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username: str, password: str) -> bool:
        user_id = str(uuid.uuid4())
        password_hash = self.hash_password(password)

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO users (id, username, password_hash)
                    VALUES (?, ?, ?)
                """, (user_id, username, password_hash))
                conn.commit()
            log_event("UserManager", f"User registered: {username}")
            return True
        except sqlite3.IntegrityError:
            log_event("UserManager", f"Registration failed: Username '{username}' already exists.")
            return False

    def authenticate_user(self, username: str, password: str) -> bool:
        password_hash = self.hash_password(password)
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id FROM users WHERE username = ? AND password_hash = ?
            """, (username, password_hash))
            result = cursor.fetchone()
            if result:
                log_event("UserManager", f"Authentication successful for user '{username}'")
                return True
            else:
                log_event("UserManager", f"Authentication failed for user '{username}'")
                return False

    def user_exists(self, username: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
            return cursor.fetchone() is not None

    def delete_user(self, username: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE username = ?", (username,))
            conn.commit()
            if cursor.rowcount > 0:
                log_event("UserManager", f"User '{username}' deleted.")
                return True
            else:
                log_event("UserManager", f"Failed to delete user '{username}'.")
                return False
