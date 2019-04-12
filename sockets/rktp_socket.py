from __future__ import with_statement
import sys
from multiprocessing import Lock
from threading import Thread
from sockets import SocketInterface, IPV4_FAMILY_ADDRESS, UDP_SOCKET, PACKAGE_SIZE, ENCODE
import time

START_SEND_PACK_NUMBER = 0
START_RCV_PACK_NUMBER = 0
PACK_NUM = 0
TIMESTAMP = 1
DATA = 2
RCV_DATA = 1

MAX_LIFE_TIME = sys.maxsize
SEND_BUFFER_SIZE = 3


# server
class RKTPSocket(SocketInterface):
    connected_socket = ("0.0.0.0", 0)
    __shut_down = 0

    def listen(self, queue_size):
        pass

    def __init__(self):
        super().__init__(IPV4_FAMILY_ADDRESS, UDP_SOCKET)

        self.__send_th = 0

        self.sent_buffer = []
        self.sent_buffer_lock = Lock()
        self.sent_thread_is_started = False
        self.sent_thread_start_request = False

        self.ack_buffer = []
        self.ack_buffer_lock = Lock()

        self.recv_buffer = []
        self.recv_buffer_lock = Lock()

        self.next_send_pack_number = START_SEND_PACK_NUMBER
        self.next_rcv_pack_number = START_RCV_PACK_NUMBER

    def connect(self, address, port):
        self.connected_socket = (address, port)
        self.send('SYN'.encode(ENCODE))
        self.__recv_th = Thread(target=self.__rcv_thread).start()
        self.recv(self.BUF_SIZE)
        self.send('ACK'.encode(ENCODE))

    def accept(self):
        Thread(target=self.__rcv_thread).start()

        self.recv(self.BUF_SIZE)
        self.send('SYN ACK'.encode(ENCODE))
        self.recv(self.BUF_SIZE)
        return self, self.connected_socket

    def send(self, data):
        while True:
            with self.sent_buffer_lock:
                if len(self.sent_buffer) < SEND_BUFFER_SIZE:
                    self.sent_buffer.append((self.next_send_pack_number, time.time(), data))
                    break
            time.sleep(0.1)

        self.next_send_pack_number += 1
        if not self.sent_thread_is_started:
            # start sent_thread
            self.__send_th = Thread(target=self.__send_thread)
            self.__send_th.start()
        else:
            self.sent_thread_start_request = True

    def recv(self, size_of_data):
        while True:
            with self.recv_buffer_lock:
                for p in self.recv_buffer:
                    if p[PACK_NUM] == self.next_rcv_pack_number:
                        self.next_rcv_pack_number += 1
                        self.recv_buffer.remove(p)
                        return p[RCV_DATA]
            time.sleep(0.001)

    def __send_thread(self):
        print("new send thread")
        self.sent_thread_is_started = True

        with self.sent_buffer_lock:
            for pack in self.sent_buffer:
                if pack[TIMESTAMP] - time.time() < MAX_LIFE_TIME:
                    self.socket.sendto(RKTPSocket.get_pack(pack[PACK_NUM], pack[DATA]), self.connected_socket)
                    print('send : ', len(self.sent_buffer))
                else:
                    self.sent_buffer.remove(pack)

        time.sleep(0.01)
        with self.ack_buffer_lock:
            with self.sent_buffer_lock:
                for ack in self.ack_buffer:
                    RKTPSocket.remove_pack(self.sent_buffer, ack)
                self.ack_buffer = []

            if (len(self.sent_buffer) != 0 or self.sent_thread_start_request) and self.__shut_down == 0:
                self.sent_thread_start_request = False
                # start sent_thread
                time.sleep(0.001)
                self.__send_th = Thread(target=self.__send_thread)
                self.__send_th.start()

        self.sent_thread_is_started = False

    def __rcv_thread(self):
        while self.__shut_down == 0:
            try:
                data, self.connected_socket = self.socket.recvfrom(PACKAGE_SIZE)
                if len(data) == 8:
                    ack = int.from_bytes(data, byteorder='big')
                    with self.ack_buffer_lock:
                        self.ack_buffer.append(ack)
                else:
                    pack_num, message = RKTPSocket.unpack_data(data)
                    if pack_num >= self.next_rcv_pack_number:
                        with self.recv_buffer_lock:
                            flag = False
                            for p in self.recv_buffer:
                                if p[PACK_NUM] == pack_num:
                                    flag = True
                            if not flag:
                                self.recv_buffer.append((pack_num, message))

                    self.socket.sendto(pack_num.to_bytes(8, 'big'), self.connected_socket)
            except OSError:
                pass

    @staticmethod
    def get_pack(pack_num, data):
        return pack_num.to_bytes(8, 'big') + data

    @staticmethod
    def remove_pack(byffer, ack):
        for p in byffer:
            if p[PACK_NUM] == ack:
                byffer.remove(p)

    @staticmethod
    def unpack_data(data):
        pack_num = int.from_bytes(data[0:8], byteorder='big')
        return pack_num, data[8:]

    def shutdown(self, how=0):
        self.__shut_down = 1
        self.__send_th.join()
        self.socket.shutdown(how)

