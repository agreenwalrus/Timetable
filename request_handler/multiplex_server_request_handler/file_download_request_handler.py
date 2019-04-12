from request_handler.multiplex_server_request_handler.server_request_handler_interface import *
import os

from sockets import USEFUL_PACKAGE_SIZE


class FileDownloadRequestHandler(RequestHandlerInterface):

    def __init__(self, data):
        super().__init__(data)
        self.is_alive = True
        self.file_is_opened = False
        self.file_size_remaining = 0
        self.file = None
        self.pack_size = USEFUL_PACKAGE_SIZE

    def handle_request(self, socket):
        try:
            if not self.file_is_opened:
                print("if not self.file_is_opened")
                file_name, data = self.parse_params_and_data()
                statinfo = os.stat('./files_server/' + file_name)
                self.file = open('./files_server/' + file_name, 'rb')
                self.file_size_remaining = statinfo.st_size
                print("File [", file_name, "] is downloading")
                self.is_alive = True
                self.file_is_opened = True
                msg = self.file_size_remaining.to_bytes(8, 'big')
            else:
                print("if self.file_is_opened")
                if self.file_size_remaining < self.pack_size:
                    self.pack_size = self.file_size_remaining
                msg = self.file.read(self.pack_size)
                self.file_size_remaining -= self.pack_size
                if self.file_size_remaining == 0:
                    self.is_alive = False
                    self.file.close()
                    self.file_is_opened = False
            code = OK

        except IOError:
            self.is_alive = False
            print("except IOError")
            self.file_size_remaining = -1
            msg = self.file_size_remaining.to_bytes(8, 'big', signed=True)
            code = OK
            if self.file_is_opened:
                self.file.close()
                self.file_is_opened = False
                msg = None
                code = ERROR

        return self.is_alive, code, msg


