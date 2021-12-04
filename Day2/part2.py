from direction import Direction


def get_commands():
    file = open('input.txt')
    return [Direction(l) for l in file.readlines()]


def run():
    horizontal = 0
    depth = 0
    aim = 0

    command_list = get_commands()

    for command in command_list:
        if command.command_arg == 'forward':
            horizontal += command.units
            depth += aim * command.units
        elif command.command_arg == 'down':
            aim += command.units
        else:
            aim -= command.units

    print('Horizontal: ' + str(horizontal))
    print('Depth: ' + str(depth))
    print('Aim: ' + str(aim))
    print('Product: ' + str(horizontal * depth))


if __name__ == '__main__':
    run()
