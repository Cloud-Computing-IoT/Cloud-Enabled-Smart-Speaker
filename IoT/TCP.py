import os
import socket
import wave

# TCP_IP = "192.168.86.26"
# TCP_PORT = 5005
BUFFER_SIZE = 1024



class TCPsocket:
    def __init__(self, TCP_IP, TCP_PORT):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((TCP_IP,TCP_PORT))

    def sendData(self, message):
        self.s.send(message.encode())

    def sendFile(self, path):
        print("PATH: " + path)
        f = open(path, 'rb')
        l = f.read(1024)
        while(l):
            print("sending...")
            self.sendData(l)
            l = f.read(1024)
        f.close()
        print("done sending")

    def receive(self):
        data = self.s.recv(BUFFER_SIZE)
        return data.decode()

    def closeSocket(self):
        self.s.close()
