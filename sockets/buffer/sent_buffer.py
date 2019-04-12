class SentBuffer:

    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.current_pack_num_to_send = 0
        self.next_pack_num = 0
        self.buffer = {}
        self.current_size = 0

    def get_buffer_capacity(self):
        return self.buffer_size

    def get_current_size(self):
        return self.current_size

    def set_start_pack_num(self, start_pack_num):
        self.current_pack_num_to_send = start_pack_num
        self.next_pack_num = start_pack_num

    def add_pack(self, data):
        print("sb: add_pack ", self.next_pack_num)
        self.buffer[self.next_pack_num] = data
        self.next_pack_num += 1
        self.current_size += 1

    def get_next_pack(self):
        print("sb: get_next_pack")
        self.current_pack_num_to_send += 1
        keys = self.buffer.keys()
        if self.current_pack_num_to_send > max(keys):
            self.current_pack_num_to_send = min(keys)
        return self.current_pack_num_to_send, self.buffer[self.current_pack_num_to_send]

    def delete_pack(self, ack):
        print("sb: delete_pack ", ack)
        if self.current_size != 0:
            keys = self.buffer.keys()
            min_key = min(keys)
            for key in range(min_key, ack):
                self.buffer.pop(key)
                self.current_size -= 1
