from socket import *

class Server:
    def __init__(self):
        self.my_host = ""
        self.my_port = 50007
    def startServer(self, my_host, my_port):
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.bind((my_host, my_port))
        sockobj.listen(5)
        while True:
            connection,address = sockobj.accept()
            print("Server connected by:", address)
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                connection.send(b'Echo = >' + data)
                client_info = eval(data)
                if client_info["login"] == 1:
                    print("Informarion: ", client_info["login"])
            connection.close()
if __name__ == "__main__":
    server_object  = Server()
    server_object.startServer(server_object.my_host, server_object.my_port)
