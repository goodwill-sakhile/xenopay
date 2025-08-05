import uuid
import time
from utils.logger import log_event

# In-memory token store for simplicity (replace with Redis or DB in production)
TOKEN_STORE = {}


class TokenService:
    def __init__(self, expiration_seconds=3600):
        self.expiration = expiration_seconds

    def generate_token(self, username: str) -> str:
        """
        Generates a unique token for a user and stores it with expiration.
        """
        token = str(uuid.uuid4())
        expiry_time = time.time() + self.expiration
        TOKEN_STORE[token] = {
            "username": username,
            "expires_at": expiry_time
        }
        log_event("TokenService", f"Token generated for {username}, expires in {self.expiration} seconds.")
        return token

    def validate_token(self, token: str) -> bool:
        """
        Validates a token's existence and expiry.
        """
        token_data = TOKEN_STORE.get(token)
        if not token_data:
            log_event("TokenService", f"Invalid token: {token}")
            return False

        if time.time() > token_data['expires_at']:
            log_event("TokenService", f"Token expired for user {token_data['username']}")
            del TOKEN_STORE[token]
            return False

        log_event("TokenService", f"Token validated for user {token_data['username']}")
        return True

    def get_username_from_token(self, token: str) -> str:
        """
        Retrieves the username associated with the token.
        """
        data = TOKEN_STORE.get(token)
        if data and time.time() < data['expires_at']:
            return data['username']
        return None

    def revoke_token(self, token: str) -> bool:
        """
        Deletes the token from the store.
        """
        if token in TOKEN_STORE:
            user = TOKEN_STORE[token]["username"]
            del TOKEN_STORE[token]
            log_event("TokenService", f"Token revoked for user {user}")
            return True
        return False

    def cleanup_expired_tokens(self):
        """
        Removes all expired tokens (called periodically if needed).
        """
        now = time.time()
        expired_tokens = [t for t, data in TOKEN_STORE.items() if data["expires_at"] < now]
        for token in expired_tokens:
            del TOKEN_STORE[token]
        if expired_tokens:
            log_event("TokenService", f"Cleaned up {len(expired_tokens)} expired tokens.")
