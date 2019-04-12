class RecvBuffer:

    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.buffer = {}
        self.current_size = 0
        self.next_ack = 0

    def get_buffer_capacity(self):
        return self.buffer_size

    def set_start_pack_num(self, start_pack_num):
        self.next_ack = start_pack_num

    def get_current_size(self):
        return self.current_size

    def add_pack(self, syn, data):
        print("rb:  add_pack syn", syn)
        if self.next_ack == 0:
            self.next_ack = syn + 1
        elif self.next_ack == syn:
            self.next_ack += 1
        self.buffer[syn] = data
        self.current_size += 1
        print(self.buffer)

    def pop_next_pack(self):
        print("rb:  pop_next_pack")
        min_key = min(self.buffer.keys())
        self.current_size -= 1
        return self.buffer.pop(min_key)

    def is_possible_to_add_pack(self, syn):
        return not(self.current_size + 1 == self.buffer_size and self.next_ack != syn)

    def get_ack(self):
        print("rb:  get_ack", self.next_ack)
        return self.next_ack
