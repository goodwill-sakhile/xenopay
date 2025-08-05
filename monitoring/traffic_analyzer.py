import time
from collections import defaultdict
from threading import Lock
from utils.logger import log_event


class TrafficAnalyzer:
    def __init__(self):
        self.user_traffic = defaultdict(lambda: {"in": 0, "out": 0})
        self.start_times = {}
        self.traffic_lock = Lock()

    def log_data(self, username: str, direction: str, byte_count: int):
        """
        Logs incoming or outgoing data for a specific user.
        Direction can be 'in' or 'out'.
        """
        if direction not in ("in", "out"):
            return

        with self.traffic_lock:
            self.user_traffic[username][direction] += byte_count
            if username not in self.start_times:
                self.start_times[username] = time.time()

        log_event("TrafficAnalyzer", f"{direction.upper()} {byte_count} bytes for user {username}")

    def get_usage_report(self, username: str) -> dict:
        """
        Returns the total usage stats for a user.
        """
        with self.traffic_lock:
            traffic = self.user_traffic.get(username, {"in": 0, "out": 0})
            session_time = time.time() - self.start_times.get(username, time.time())
            return {
                "bytes_in": traffic["in"],
                "bytes_out": traffic["out"],
                "total_bytes": traffic["in"] + traffic["out"],
                "session_duration_sec": round(session_time, 2)
            }

    def get_all_usage(self) -> dict:
        """
        Returns usage stats for all users.
        """
        report = {}
        with self.traffic_lock:
            for user in self.user_traffic:
                report[user] = self.get_usage_report(user)
        return report

    def reset_user_stats(self, username: str):
        """
        Resets usage statistics for a specific user.
        """
        with self.traffic_lock:
            self.user_traffic[username] = {"in": 0, "out": 0}
            self.start_times[username] = time.time()
        log_event("TrafficAnalyzer", f"Reset traffic stats for user {username}")

    def reset_all(self):
        """
        Clears all recorded stats.
        """
        with self.traffic_lock:
            self.user_traffic.clear()
            self.start_times.clear()
        log_event("TrafficAnalyzer", "Reset traffic stats for all users")
