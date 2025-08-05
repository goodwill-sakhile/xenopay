import socket
import threading
import time
from utils.logger import log_event
from utils.encryption_engine import encrypt_data, decrypt_data
from sessions.session_manager import get_session_by_token


class TunnelHandler:
    def __init__(self, host='0.0.0.0', port=1194, buffer_size=4096):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.server_socket = None
        self.active_connections = {}
        self.running = True

    def start_server(self):
        """Starts the tunnel server socket"""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(100)
        log_event("TunnelHandler", f"VPN Tunnel Server started on {self.host}:{self.port}")
        while self.running:
            try:
                client_sock, client_addr = self.server_socket.accept()
                log_event("TunnelHandler", f"Connection accepted from {client_addr}")
                threading.Thread(target=self.handle_client, args=(client_sock, client_addr), daemon=True).start()
            except Exception as e:
                log_event("TunnelHandler", f"Error accepting connection: {e}")

    def handle_client(self, client_socket, client_address):
        """Handles a client VPN connection"""
        try:
            token = client_socket.recv(1024).decode().strip()
            session = get_session_by_token(token)

            if not session:
                log_event("TunnelHandler", f"Invalid token from {client_address}")
                client_socket.send(b"AUTH_FAILED")
                client_socket.close()
                return

            client_socket.send(b"AUTH_SUCCESS")
            self.active_connections[client_address] = client_socket
            log_event("TunnelHandler", f"Session authenticated for {client_address}")

            while True:
                encrypted_data = client_socket.recv(self.buffer_size)
                if not encrypted_data:
                    break
                data = decrypt_data(encrypted_data, session['key'])
                log_event("TunnelHandler", f"Received data from {client_address}: {data.decode(errors='ignore')}")

                # Echo back or forward to destination if implemented
                response = encrypt_data(b"ACK: " + data, session['key'])
                client_socket.send(response)

        except Exception as e:
            log_event("TunnelHandler", f"Error in tunnel with {client_address}: {e}")
        finally:
            client_socket.close()
            self.active_connections.pop(client_address, None)
            log_event("TunnelHandler", f"Connection closed for {client_address}")

    def stop_server(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        log_event("TunnelHandler", "VPN Tunnel Server stopped")

