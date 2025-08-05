import struct
import json
from utils.logger import log_event


class PacketProcessor:
    HEADER_FORMAT = "!I"  # 4-byte unsigned int for payload size

    def __init__(self):
        self.packet_count = 0

    def build_packet(self, data: bytes) -> bytes:
        """
        Prefixes data with a 4-byte length header.
        """
        self.packet_count += 1
        header = struct.pack(self.HEADER_FORMAT, len(data))
        log_event("PacketProcessor", f"Packet #{self.packet_count} built with size {len(data)} bytes.")
        return header + data

    def parse_packet(self, packet: bytes) -> bytes:
        """
        Parses a packet, extracts the length-prefixed payload.
        """
        try:
            header_size = struct.calcsize(self.HEADER_FORMAT)
            if len(packet) < header_size:
                raise ValueError("Incomplete packet header")

            length = struct.unpack(self.HEADER_FORMAT, packet[:header_size])[0]
            payload = packet[header_size:header_size + length]
            log_event("PacketProcessor", f"Parsed packet of length {length} bytes.")
            return payload

        except Exception as e:
            log_event("PacketProcessor", f"Error parsing packet: {e}")
            return b""

    def inspect_packet(self, payload: bytes) -> dict:
        """
        Inspect and parse payload assuming it's JSON-encoded for logging/demo purposes.
        """
        try:
            data = json.loads(payload.decode())
            log_event("PacketProcessor", f"Payload inspected: {data}")
            return data
        except json.JSONDecodeError:
            log_event("PacketProcessor", "Payload is not valid JSON.")
            return {"raw": payload.decode(errors="ignore")}

    def route_packet(self, payload: bytes) -> bytes:
        """
        Dummy routing function. In a real-world VPN this would determine where to send the data.
        """
        log_event("PacketProcessor", f"Routing packet: {payload[:50]}...")
        # Here, you could implement DNS spoofing, redirecting, etc.
        return payload[::-1]  # Just reverse the payload as a mock response

