from server.serial_socket_server import SerialTCPSocketServer
from handler.server_handler.remote_console_request_handler_factory import RemoteConsoleRequestHandlerFactory
from sockets.tcp_socket import TCPSocket
from server.pool import pool_interface

if __name__ == '__main__':
    MAX_AMOUNT_OF_CLIENTS = 2
    server = SerialTCPSocketServer("0.0.0.0", 37000, RemoteConsoleRequestHandlerFactory())
    server.start_server()

# if __name__=='__main__':
#     address = ''
#     while not re.match(
#             '^(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]{2}|[0-9])(\.(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]{2}|[0-9])){3}$',
#             address):
#         print('ipv4 : ', end='')
#         address = input()
#
#     port = -1
#     while port < 0 or port > 65235:
#         print('port : ', end='')
#         try:
#             port = int(input())
#         except ValueError:
#             continue
#     try:
#         server= SerialTCPSocketServer(address, port, UDPSocket(), RemoteConsoleRequestHandlerFactory())
#         server.start_server()
#     except ConnectionRefusedError:
#         print('Connection is refused')
