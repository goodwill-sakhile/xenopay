import os

# Database configuration
DB_PATH = os.getenv("VPN_DB_PATH", "vpn_backend.sqlite3")

# Server configuration
VPN_HOST = os.getenv("VPN_HOST", "0.0.0.0")
VPN_PORT = int(os.getenv("VPN_PORT", "1194"))
BUFFER_SIZE = int(os.getenv("VPN_BUFFER_SIZE", "4096"))

# Security settings
TOKEN_EXPIRATION_SECONDS = int(os.getenv("TOKEN_EXPIRATION_SECONDS", "3600"))
ENCRYPTION_ALGORITHM = os.getenv("ENCRYPTION_ALGORITHM", "AES-256-CBC")

# Logging settings
LOG_FILE_PATH = os.getenv("VPN_LOG_FILE", "vpn_backend.log")
LOG_TO_FILE = os.getenv("VPN_LOG_TO_FILE", "True").lower() in ("true", "1", "yes")
LOG_LEVEL = os.getenv("VPN_LOG_LEVEL", "INFO")  # DEBUG, INFO, WARNING, ERROR

# Firewall defaults
DEFAULT_DENY_POLICY = os.getenv("DEFAULT_DENY_POLICY", "False").lower() in ("true", "1", "yes")

# Session settings
MAX_SESSION_AGE_SECONDS = int(os.getenv("MAX_SESSION_AGE_SECONDS", "3600"))

# Optional: API server config (if API module used)
API_ENABLED = os.getenv("API_ENABLED", "False").lower() in ("true", "1", "yes")
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", "8000"))

# Miscellaneous
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() in ("true", "1", "yes")

# Print summary for verification (only if debug mode)
if DEBUG_MODE:
    print("VPN Backend Configuration:")
    print(f"DB_PATH = {DB_PATH}")
    print(f"VPN_HOST = {VPN_HOST}")
    print(f"VPN_PORT = {VPN_PORT}")
    print(f"BUFFER_SIZE = {BUFFER_SIZE}")
    print(f"TOKEN_EXPIRATION_SECONDS = {TOKEN_EXPIRATION_SECONDS}")
    print(f"ENCRYPTION_ALGORITHM = {ENCRYPTION_ALGORITHM}")
    print(f"LOG_FILE_PATH = {LOG_FILE_PATH}")
    print(f"LOG_TO_FILE = {LOG_TO_FILE}")
    print(f"LOG_LEVEL = {LOG_LEVEL}")
    print(f"DEFAULT_DENY_POLICY = {DEFAULT_DENY_POLICY}")
    print(f"MAX_SESSION_AGE_SECONDS = {MAX_SESSION_AGE_SECONDS}")
    print(f"API_ENABLED = {API_ENABLED}")
    print(f"API_HOST = {API_HOST}")
    print(f"API_PORT = {API_PORT}")
    print(f"DEBUG_MODE = {DEBUG_MODE}")
