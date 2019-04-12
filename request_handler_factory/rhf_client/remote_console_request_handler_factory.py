from request_handler.client_request_handler import file_upload_request_handler, exit_request_handler, \
    unrecognized_commads_request_handler, file_download_request_handler
from request_handler_factory.request_handler_factory_interface import RequestHandlerFactoryInterface


class RemoteConsoleRequestHandlerFactory(RequestHandlerFactoryInterface):

    def parse_request_handler(self, request_str):
        if ' ' in request_str:
            command, _ = request_str.split(' ', maxsplit=1)
        else:
            command = request_str
        return command

    def get_request_handler(self, request_str):
        command = self.parse_request_handler(request_str)
        handlers_dict = {
            "exit": RemoteConsoleRequestHandlerFactory.get_exit_request_handler,
            "upload": RemoteConsoleRequestHandlerFactory.get_file_upload_request_handler,
            "download": RemoteConsoleRequestHandlerFactory.get_file_download_request_handler,
            "unrecognized": RemoteConsoleRequestHandlerFactory.get_unrecognized_request_handler
        }       
        try:
            request_handler_creator = handlers_dict[command]
        except KeyError:
            request_handler_creator = handlers_dict["unrecognized"]
        return request_handler_creator(request_str)

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
    def get_unrecognized_request_handler(params):
        return unrecognized_commads_request_handler.UnrecognizedCommandsRequestHandler(params)

