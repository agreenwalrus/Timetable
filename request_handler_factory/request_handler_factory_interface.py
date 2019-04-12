class RequestHandlerFactoryInterface:

    OK = 0
    ERROR = 1

    def parse_request_handler(self, request_str):
        raise NotImplementedError
        '''_
        command_and_params, data = request_str.split('\r\n', maxsplit=1)
        if ' ' in command_and_params:
            command, params_str = command_and_params.split(' ', maxsplit=1)
            params = params_str.split(' ')
        else:
            command = command_and_params
            params = []

        return command, params, data
        '''
