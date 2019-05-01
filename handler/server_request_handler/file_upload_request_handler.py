from handler.server_request_handler.server_request_handler_interface import *
from sockets.socket_interface import PACKAGE_SIZE


class FileUploadRequestHandler((RequestHandlerInterface)):

    def parse_params_and_data(self):
        filename, data = self.params_and_data.split(' ', maxsplit=1)
        file_size, data = data.split('\r\n', maxsplit=1)
        return filename, file_size, data

    def handle_request(self, socket):
        try:
            file_name, file_size, data = self.parse_params_and_data()
            file = open('./files_server/' + file_name, 'wb+')
            file_size_remaining = int(file_size)

            socket.send(bytes('123', ENCODE)) #sync
            print("File [", file_name, "] is uploading")
            while file_size_remaining != 0:

                data = socket.recv(PACKAGE_SIZE)
                file.write(data)
                file_size_remaining -= len(data)

            file.close()
            print("File is uploaded!")
            return OK
        except IOError as e:
            print(str(e))
            return ERROR



