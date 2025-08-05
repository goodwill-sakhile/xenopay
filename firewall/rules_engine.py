from utils.logger import log_event

class FirewallRulesEngine:
    def __init__(self):
        # IPs explicitly blocked from access
        self.blacklist = set()
        # IPs explicitly allowed even if other filtering applies
        self.whitelist = set()
        # Toggle for default-deny policy
        self.default_deny = False

    def add_to_blacklist(self, ip: str):
        self.blacklist.add(ip)
        log_event("Firewall", f"Blacklisted IP: {ip}")

    def remove_from_blacklist(self, ip: str):
        self.blacklist.discard(ip)
        log_event("Firewall", f"Removed IP from blacklist: {ip}")

    def add_to_whitelist(self, ip: str):
        self.whitelist.add(ip)
        log_event("Firewall", f"Whitelisted IP: {ip}")

    def remove_from_whitelist(self, ip: str):
        self.whitelist.discard(ip)
        log_event("Firewall", f"Removed IP from whitelist: {ip}")

    def check_access(self, ip: str) -> bool:
        """
        Checks whether the given IP is allowed or denied.
        """
        if ip in self.blacklist:
            log_event("Firewall", f"Access denied (blacklisted): {ip}")
            return False
        if ip in self.whitelist:
            log_event("Firewall", f"Access granted (whitelisted): {ip}")
            return True
        if self.default_deny:
            log_event("Firewall", f"Access denied (default policy): {ip}")
            return False
        log_event("Firewall", f"Access granted (default policy): {ip}")
        return True

    def enable_default_deny(self):
        self.default_deny = True
        log_event("Firewall", "Default deny policy enabled.")

    def disable_default_deny(self):
        self.default_deny = False
        log_event("Firewall", "Default deny policy disabled.")

    def list_rules(self) -> dict:
        """
        Returns a snapshot of current firewall rule settings.
        """
        return {
            "blacklist": list(self.blacklist),
            "whitelist": list(self.whitelist),
            "default_deny": self.default_deny,
        }

    def clear_all(self):
        self.blacklist.clear()
        self.whitelist.clear()
        log_event("Firewall", "Cleared all firewall rules.")
