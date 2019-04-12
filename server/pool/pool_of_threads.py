from server.pool.pool_interface import PoolInterface
from concurrent.futures.thread import ThreadPoolExecutor

class ThreadsPool(PoolInterface):

    def __init__(self, amount_of_entities):
        super().__init__(amount_of_entities)
        self.pool = ThreadPoolExecutor(self.max_amount)

    def shutdown(self, timeout):
        return self.pool.shutdown(timeout)

    def execute(self, funct, socket, addr):
        return self.pool.submit(funct, socket, addr)
