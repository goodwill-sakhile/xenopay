import sys
from socket import *
server_host = "localhost"
server_port = 50007
message = [b'{"Hello_Network_World":1}']
class Client:
    def __init__(self):
        self.server_host = "localhost"
        self.server_port = 50007
        self.message = [b'' + str({"login":1})]
    def clientMainFunction(self, server_host, server_port, message):
        if len(sys.argv) > 1:
            server_host = sys.argv[1]
            if len(sys.argv) > 2:
                message = (x.encode() for x in sys.argv[2:])
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.connect((server_host, server_port))
        for line in message:
            sockobj.send(line)
            data = sockobj.recv(1024)
            print("Client received:", data)
        sockobj.close()
if __name__ == "__main__":
    client = Client()
    client.clientMainFunction(client.server_host, client.server_port, client.message)
