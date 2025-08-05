import time
import uuid
from utils.logger import log_event

# In-memory session store
SESSION_STORE = {}


class SessionManager:
    def __init__(self):
        self.session_store = SESSION_STORE

    def create_session(self, username: str, client_ip: str, port: int) -> dict:
        """
        Creates a new session and stores session metadata.
        """
        token = str(uuid.uuid4())
        session_info = {
            "token": token,
            "username": username,
            "client_ip": client_ip,
            "port": port,
            "connected_at": time.time(),
            "key": self.generate_session_key(username),
        }
        self.session_store[token] = session_info
        log_event("SessionManager", f"Session started for {username} at {client_ip}:{port}")
        return session_info

    def generate_session_key(self, username: str) -> str:
        """
        Generates a pseudo-random session key for encryption (simplified).
        """
        salt = str(uuid.uuid4()).replace("-", "")
        return f"{username}-{salt}"

    def get_session_by_token(self, token: str) -> dict:
        """
        Retrieves session details using the session token.
        """
        session = self.session_store.get(token)
        if session:
            log_event("SessionManager", f"Session retrieved for user {session['username']}")
        else:
            log_event("SessionManager", f"Session not found for token {token}")
        return session

    def close_session(self, token: str) -> bool:
        """
        Closes an active session.
        """
        if token in self.session_store:
            user = self.session_store[token]["username"]
            del self.session_store[token]
            log_event("SessionManager", f"Session closed for user {user}")
            return True
        return False

    def get_active_sessions(self) -> list:
        """
        Returns all currently active sessions.
        """
        return list(self.session_store.values())

    def session_count(self) -> int:
        """
        Returns the number of active sessions.
        """
        return len(self.session_store)

    def cleanup_expired_sessions(self, max_age_seconds=3600):
        """
        Optionally remove sessions that are too old.
        """
        now = time.time()
        expired = []
        for token, session in list(self.session_store.items()):
            if now - session["connected_at"] > max_age_seconds:
                expired.append(token)
        for token in expired:
            user = self.session_store[token]["username"]
            del self.session_store[token]
            log_event("SessionManager", f"Session expired and removed for user {user}")
