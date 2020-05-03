import socket
import threading
from interface import Interface

class Client(Interface):
    def __init__(self):
        #create thread for ui
        threading.Thread(target=self.create_window).start()

        #connection info
        self.target_host = "localhost"
        self.target_port = 3333

        #create client and connect to server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.target_host,self.target_port))

        #wait messages from server
        threading.Thread(target=self.take_message).start()

    #wait and get messages
    def take_message(self):
        while True:
            response = self.client.recv(4096)
            response = response.decode("utf-8")
            self.add_message(response)

    #send messages to server
    def send_message(self):
        message = self.add_message(self.get_text())
        if message != "":
            message = bytes(message, "utf-8")
            self.client.send(message)
        else:
            print("Message is empty !")

client = Client()
