class Direction:
    command_arg = ''
    units = 0

    def __init__(self, command_string):
        command_parts = command_string.split(' ')
        self.command_arg = command_parts[0]
        self.units = int(command_parts[1])


    def display(self):
        print(self.command_arg + ' ' + str(self.units))
