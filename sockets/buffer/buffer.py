from heapq import heappush, heappop, nsmallest
from copy import copy

KEY = 0
DATA = 1
SMALLEST_EL_IND = 0

class Buffer:

    def __init__(self, buffer_size):
        self.heap = []
        self.max_size = buffer_size
        self.size = 0

    def add(self, pack_number, pack_data):
        raise NotImplementedError

    def get_buffer_size(self):
        return self.max_size
    
    def get_amount_of_packs(self):
        return self.size

    def get_smallest_pack(self):
        return copy(self.heap[SMALLEST_EL_IND])

    def remove_smallest_pack(self):
        if self.size >= 1:
            el = heappop(self.heap)
            self.size -= 1
            return el
        else:
            raise MemoryError("There are less objects in buffer, than expected")

    def get_packs(self, amount):
        if amount <= self.size:
            return nsmallest(amount, self.heap)
        else:
            raise MemoryError("There are less objects in buffer, than expected")

    
    
    