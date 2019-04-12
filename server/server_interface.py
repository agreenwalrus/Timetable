class ServerInterface:

    def __init__(self, ipv4_addr, port, socket, request_handler_factory):
        self.ipv4_addr = ipv4_addr
        self.port = port
        self.socket = socket
        self.request_handler_factory = request_handler_factory

    def __shutdown(self):
        raise NotImplementedError

    def start_server(self):
        raise NotImplementedError

    def stop_server(self):
        raise NotImplementedError


