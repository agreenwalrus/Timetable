OK = 0
ERROR = 1
STOP_SERVER = 2
ENCODE = "cp1252"


class RequestHandlerInterface:

    def __init__(self, data):
        self.is_alive = False
        self.params_and_data = data

    def parse_params_and_data(self):
        params, data = self.params_and_data.split('\r\n', maxsplit=1)
        return params, data

    def handle_request(self, data):
        raise NotImplementedError
