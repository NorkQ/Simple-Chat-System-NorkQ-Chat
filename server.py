import socket
import threading
from interface import Interface

class Server(Interface):
    def __init__(self):
        #create thread for ui
        threading.Thread(target=self.create_window).start()
        self.bind_ip = "localhost"
        self.bind_port = 3333

        #create server
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.bind_ip, self.bind_port))

        #set client count
        print("Waiting for client")
        self.server.listen(1)
        
        self.client = None
        #wait for clients
        self.find_client()

    def listen_client(self, client_socket):
        self.client = client_socket
        client_socket.send(bytes("Welcome to server !", "utf-8"))
        #when connect to client, wait for messages
        self.take_message()

    def find_client(self):
        while True:
            client, addr = self.server.accept()
            print(f"Client accepted - ({addr[0]}:{addr[1]})")
            client_handler = threading.Thread(target=self.listen_client,args=(client,))
            client_handler.start()
        
    def send_message(self):
        message = self.add_message(self.get_text())
        if message != "":
            message = bytes(message, "utf-8")
            self.client.send(message)
        else:
            print("Message is empty")

    def take_message(self):
        while True:
            request = self.client.recv(1024)
            request = request.decode("utf-8")
            self.add_message(request)

server = Server()
