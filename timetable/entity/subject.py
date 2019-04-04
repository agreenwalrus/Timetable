class Subject:

    def __init__(self, name: str, short_name: str):
        """

        :param name: Full name of the subject
        :param short_name: Short name of the subject
        """
        self.name = name
        self.short_name = short_name

    def str(self):
        return self.name + " " + self.short_name
