from server.pool.pool_interface import PoolInterface
from concurrent.futures.process import ProcessPoolExecutor


class ProcessesPool(PoolInterface):

    def __init__(self, amount_of_entities):
        super().__init__(amount_of_entities)
        self.pool = ProcessPoolExecutor(self.max_amount)


    def shutdown(self, timeout):
        self.pool.close()

    def execute(self, funct, socket):
        return self.pool.submit(funct, socket[0], socket[1])
