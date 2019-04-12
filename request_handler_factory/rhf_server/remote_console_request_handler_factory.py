from request_handler.server_request_handler import exit_request_handler, unknown_request_handler, \
    file_download_request_handler, echo_request_handler, date_request_handler, file_upload_request_handler
from request_handler_factory.request_handler_factory_interface import RequestHandlerFactoryInterface


class RemoteConsoleRequestHandlerFactory(RequestHandlerFactoryInterface):

    def parse_request_handler(self, request_str):
        if ' ' in request_str:
            command, data = request_str.split(' ', maxsplit=1)
        else:
            command, data = request_str.split('\r\n', maxsplit=1)

        return command, data

    def get_request_handler(self, request_str):
        command, data = self.parse_request_handler(request_str)
        handlers_dict = {
            "echo": RemoteConsoleRequestHandlerFactory.get_echo_request_handler,
            "date": RemoteConsoleRequestHandlerFactory.get_date_request_handler,
            "exit": RemoteConsoleRequestHandlerFactory.get_exit_request_handler,
            "upload": RemoteConsoleRequestHandlerFactory.get_file_upload_request_handler,
            "download": RemoteConsoleRequestHandlerFactory.get_file_download_request_handler,
            "unknown": RemoteConsoleRequestHandlerFactory.get_unknown_request_handler
        }       
        try:
            request_handler_creator = handlers_dict[command]
        except KeyError:
            request_handler_creator = handlers_dict["unknown"]
        return request_handler_creator(data)

    @staticmethod
    def get_echo_request_handler(params):
        return echo_request_handler.EchoRequestHandler(params)

    @staticmethod
    def get_date_request_handler(params):
        return date_request_handler.DateRequestHandler(params)

    @staticmethod
    def get_exit_request_handler(params):
        return exit_request_handler.ExitRequestHandler(params)

    @staticmethod
    def get_file_upload_request_handler(params):
        return file_upload_request_handler.FileUploadRequestHandler(params)

    @staticmethod
    def get_file_download_request_handler(params):
        return file_download_request_handler.FileDownloadRequestHandler(params)

    @staticmethod
    def get_unknown_request_handler(params):
        return unknown_request_handler.UnknownRequestHandler(params)

