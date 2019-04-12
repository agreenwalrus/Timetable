from request_handler.multiplex_server_request_handler.server_request_handler_interface import *


class EchoRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        if '\r\n' in self.params_and_data:
            params, data = self.parse_params_and_data()
            data_for_sending = params
        else:
            data_for_sending = '\r\n'
        return self.is_alive, OK, data_for_sending.encode(ENCODE)
