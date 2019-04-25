class AbstractDAO:

    def save(self, object):
        raise NotImplementedError

    def select_all(self):
        raise NotImplementedError

    def select(self, id):
        raise NotImplementedError

    def delete(self, id):
        raise NotImplementedError
