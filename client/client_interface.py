class ClientInterface:

    def __init__(self, ipv4_addr, port, socket, request_handler_factory):
        self.ipv4_addr = ipv4_addr
        self.port = port
        self.request_handler_factory = request_handler_factory
        self.socket = socket

    def __shutdown(self):
        raise NotImplementedError

    def start_client(self):
        raise NotImplementedError

    def stop_client(self):
        raise NotImplementedError


