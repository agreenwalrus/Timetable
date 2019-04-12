from request_handler.client_request_handler.client_request_handler_interface import *
import progressbar

from sockets.socket_interface import PACKAGE_SIZE


class FileDownloadRequestHandler(RequestHandlerInterface):

    def handle_request(self, socket):

        input_line = self.request
        if ' ' in input_line:
            file_name = input_line.split(' ', maxsplit=1)[1]
            if file_name != '':
                socket.send(bytes(input_line + "\r\n", ENCODE))

                file_size_remaining = int.from_bytes(socket.recv(PACKAGE_SIZE), byteorder='big', signed=True)

                if file_size_remaining == -1:
                    return ERROR, "File is not found!"

                file = open('./files_client/' + file_name, 'w+b')

                file_size = file_size_remaining
                with progressbar.ProgressBar(max_value=100) as bar:
                    while file_size_remaining != 0:
                        data = socket.recv(PACKAGE_SIZE)
                        file.write(data)
                        file_size_remaining -= len(data)

                        bar.update(int(((file_size - file_size_remaining) / file_size)*100))

                file.close()
                return OK, "File is downloaded."

        return ERROR, "Input file name!"

