class DAOFactoryInterface:

    def get_form_dao(self):
        raise NotImplementedError

    def get_program_class_dao(self):
        raise NotImplementedError

    def get_room_dao(self):
        raise NotImplementedError

    def get_subject_dao(self):
        raise NotImplementedError

    def get_teacher_dao(self):
        raise NotImplementedError

    def get_time_period_dao(self):
        raise NotImplementedError
