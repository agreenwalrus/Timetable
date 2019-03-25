class DataBankFiller:

    @staticmethod
    def read_data(dao_factory, data_bank):

        fd = dao_factory.get_form_dao()
        all = fd.select_all()
        data_bank.add_data("Form", all)
    
        fd = dao_factory.get_teacher_dao()
        all = fd.select_all()
        data_bank.add_data("Teacher", all)
    
        fd = dao_factory.get_room_dao()
        all = fd.select_all()
        data_bank.add_data("Room", all)
    
        fd = dao_factory.get_subject_dao()
        all = fd.select_all()
        data_bank.add_data("Subject", all)
    
        fd = dao_factory.get_time_period_dao()
        all = fd.select_all()
        data_bank.add_data("TimePeriod", all)
    
        fd = dao_factory.get_program_class_dao()
        all = fd.select_all()
        data_bank.add_data("ProgramClass", all)

