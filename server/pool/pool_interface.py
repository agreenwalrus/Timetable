class PoolInterface:

    def __init__(self, amount_of_entities):
        self.max_amount = amount_of_entities

    def shutdown(self, timeout):
        raise NotImplementedError

    def execute(self, funct, socket):
        raise NotImplementedError