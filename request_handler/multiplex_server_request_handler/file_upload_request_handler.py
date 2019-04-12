from request_handler.multiplex_server_request_handler.server_request_handler_interface import *


class FileUploadRequestHandler((RequestHandlerInterface)):

    def __init__(self, data):
        super().__init__(data)
        self.is_alive = True
        self.file_is_opened = False
        self.file_size_remaining = 0
        self.file = None

    def parse_params_and_data(self):
        filename, data = self.params_and_data.split(' ', maxsplit=1)
        file_size, data = data.split('\r\n', maxsplit=1)
        return filename, file_size, data

    def handle_request(self, data):

        try:
            if not self.file_is_opened:
                file_name, file_size, d = self.parse_params_and_data()
                self.file = open('./files_server/' + file_name, 'wb')
                self.file_size_remaining = int(file_size)
                print("File [", file_name, "] is uploading")
                self.is_alive = True
                self.file_is_opened = True
                msg = bytes('123', ENCODE)
            else:
                self.file.write(data)
                self.file_size_remaining -= len(data)
                if self.file_size_remaining == 0:
                    self.is_alive = False
                    self.file.close()
                    self.file_is_opened = False
                msg = None
            code = OK

        except IOError:
            self.file.close()
            self.file_is_opened = False
            code = ERROR
            msg = None

        return self.is_alive, code, msg





