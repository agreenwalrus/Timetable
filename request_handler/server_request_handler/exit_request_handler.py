from request_handler.server_request_handler.server_request_handler_interface import RequestHandlerInterface, STOP_SERVER


class ExitRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        return STOP_SERVER
