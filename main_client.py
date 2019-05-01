from client.client import SerialTCPSocketClient
from handler.rhf_client.remote_console_request_handler_factory import RemoteConsoleRequestHandlerFactory

#from sockets.rktp_socket import RKTPSocket
#from sockets.tcp_socket import TCPSocket

if __name__=='__main__':
    client = SerialTCPSocketClient("127.0.0.1", 37000, RemoteConsoleRequestHandlerFactory())
    client.start_client()
#

# if __name__=='__main__':
#
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
#         client = SerialTCPSocketClient(address, port, UDPSocket(), RemoteConsoleRequestHandlerFactory())
#         client.start_client()
#     except ConnectionRefusedError:
#         print('Connection is refused')