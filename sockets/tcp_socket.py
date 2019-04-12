from sockets.socket_interface import SocketInterface, IPV4_FAMILY_ADDRESS, TCP_SOCKET


ENCODE = "cp1252"

class TCPSocket(SocketInterface):

    def __init__(self):
        super().__init__(IPV4_FAMILY_ADDRESS, TCP_SOCKET)

    def listen(self, queue_size):
        return self.socket.listen(queue_size)

    def connect(self, address, port):
        return self.socket.connect((address, port))

    def accept(self):
        return self.socket.accept()

    def send(self, data):
        return self.socket.send(data)#data.encode(ENCODE))

    def recv(self, size_of_data):
        return self.socket.recv(size_of_data)
