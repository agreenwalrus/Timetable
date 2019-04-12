OK = 0
ERROR = 1
STOP_SERVER = 2
ENCODE = "cp1252"

# code:
#     0 - OK
#     1 - ERROR
#     2 - StopServer


class RequestHandlerWrapper:

    def __init__(self, request_handler_factory):
        self.command = ''
        self.initialized = False
        self.request_handler = None
        self.request_handler_factory = request_handler_factory

    def handle_request(self, data):
        if self.initialized:
            self.initialized, code, message = self.request_handler.handle_request(data)
            print("handle_request1", self.initialized, code, message)
            if not self.initialized:
                self.command = ''
        else:
            code = OK
            message = None
            data = data.decode(ENCODE)
            self.command += data
            if '\n' in data:
                self.request_handler = self.request_handler_factory.get_request_handler(self.command)
                print("command ", self.request_handler)
                self.initialized, code, message = self.request_handler.handle_request('')
                print("handle_request2", self.initialized, code, message)
                if not self.initialized:
                    self.command = ''
        return code, message

