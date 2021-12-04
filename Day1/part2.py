
def run():
    input = get_input()

    previous_sum = None
    times_increased = 0
    
    while(len(input) > 2):
        first_value = input.pop(0)
        second_value = input[0]
        third_value = input[1]

        current = first_value + second_value + third_value
        

        if (previous_sum and current > previous_sum):
            times_increased += 1

        previous_sum = current
    print(times_increased)

# Gets input from file, strips newlines, converts to int
def get_input():
    file = open('input.txt', 'r')
    return [int(line.replace('\n', '')) for line in file.readlines()]

if __name__ == '__main__':
    run()