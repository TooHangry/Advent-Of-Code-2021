# Functions
def run():
    input = get_input()
    times_increased = 0
    last_value = input[0]
    for l in input:
        if l > last_value:
            print(str(l) + ' is bigger than ' + str(last_value))
            times_increased += 1
        last_value = l
    print(times_increased)

def get_input():
    file = open('input.txt', 'r')
    return [int(line.replace('\n', '')) for line in file.readlines()]


if __name__ == '__main__':
    run()
