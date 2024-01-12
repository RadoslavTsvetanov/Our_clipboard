class Parser:
    def __init__(self, args_list):
        self.args_list = args_list

    def check_for_option(self, option):
        return option in self.args_list

    def get_option_value(self, option):
        if self.check_for_option(option):
            option_index = self.args_list.index(option)
            if option_index + 1 < len(self.args_list):
                return self.args_list[option_index + 1]
            else:
                return None
        else:
            return None
