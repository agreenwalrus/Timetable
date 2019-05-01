from handler.client_request_handler.client_request_handler_interface import *
import os

from sockets.socket_interface import PACKAGE_SIZE, USEFUL_PACKAGE_SIZE


class FileUploadRequestHandler(RequestHandlerInterface):

    def parse_params_and_data(self):
        filename, data = self.params_and_data.split(' ', maxsplit=1)
        file_size, data = data.split('\r\n', maxsplit=1)
        return filename, file_size, data

    def handle_request(self, socket):
        input_line = self.request

        if ' ' in input_line:
            file_name = input_line.split(' ', maxsplit=1)[1]
            if file_name != '':
                pack_size = USEFUL_PACKAGE_SIZE

                try:
                    statinfo = os.stat(file_name)
                    file_size_remaining = statinfo.st_size

                    file_name_without_path = file_name.split('\\')[-1]
                    socket.send(
                        ('upload ' + file_name_without_path + ' ' + str(file_size_remaining) + "\r\n").encode(ENCODE))

                    file = open(file_name, 'rb')

                    socket.recv(PACKAGE_SIZE)  # sync

                    file_size = file_size_remaining
                    #with progressbar.ProgressBar() as bar:
                    while file_size_remaining != 0:
                        if file_size_remaining < pack_size:
                            pack_size = file_size_remaining

                        data = file.read(pack_size)
                        socket.send(data)
                        file_size_remaining -= pack_size

                    #        bar.update(int(((file_size - file_size_remaining) / file_size) * 100))
                    file.close()
                except FileNotFoundError:
                    return ERROR, "File is not found!"

                return OK, "File is sent!"
        return ERROR, "Input file name, please!"




