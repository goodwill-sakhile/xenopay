import os
import time
from datetime import datetime
from threading import Lock

LOG_FILE = "vpn_backend.log"
LOG_LOCK = Lock()


class Logger:
    def __init__(self, log_file: str = LOG_FILE):
        self.log_file = log_file
        self.enable_file_logging = True
        self.ensure_log_dir()

    def ensure_log_dir(self):
        """
        Ensures the log directory exists.
        """
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def log(self, component: str, message: str):
        """
        Logs an event with a timestamp and component name.
        """
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        formatted = f"[{timestamp}] [{component}] {message}"
        self._write_console(formatted)
        if self.enable_file_logging:
            self._write_file(formatted)

    def _write_console(self, text: str):
        """
        Writes to standard output.
        """
        print(text)

    def _write_file(self, text: str):
        """
        Writes the log to a file using a lock to avoid race conditions.
        """
        with LOG_LOCK:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(text + "\n")

    def enable_console_only(self):
        self.enable_file_logging = False

    def clear_log_file(self):
        """
        Clears the log file contents.
        """
        if os.path.exists(self.log_file):
            with open(self.log_file, "w"):
                pass
            print("[Logger] Log file cleared.")


# Global instance for other modules to use
_logger_instance = Logger()


def log_event(component: str, message: str):
    """
    Public logging function used across modules.
    """
    _logger_instance.log(component, message)

