from request_handler.server_request_handler.server_request_handler_interface import *
import os

#from sockets.tcp_socket import USEFUL_PACKAGE_SIZE


class FileDownloadRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):
        pack_size = 1024#USEFUL_PACKAGE_SIZE
        try:
            file_name, data = self.parse_params_and_data()

            statinfo = os.stat('./files_server/' + file_name)
            file_size_remaining = statinfo.st_size

            file = open('./files_server/' + file_name, 'rb')

            socket.send(file_size_remaining.to_bytes(8, 'big'))
            print("File [", file_name, "] is downloading")

            while file_size_remaining != 0:
                if file_size_remaining < pack_size:
                    pack_size = file_size_remaining

                data = file.read(pack_size)
                file_size_remaining -= pack_size

                socket.send(data)
            file.close()
            return OK
        except IOError:
            file_size_remaining = -1
            socket.send(file_size_remaining.to_bytes(8, 'big', signed=True))
            return ERROR

