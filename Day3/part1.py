def get_binary():
    file = open('input.txt', 'r')
    return [l.replace('\n', '') for l in file.readlines()]

def run():
    binary_strings = get_binary()
    gamma_bit_string = ''
    epsilon_bit_string = ''

    length = len(binary_strings[0])
    column_0s = [0] * length
    column_1s = [0] * length
    for string in binary_strings:
        for i in range(0, len(string)):
            digit_in_question = string[i]
            if digit_in_question == '1':
                column_1s[i] += 1
            else:
                column_0s[i] += 1

    for i in range(0, length):
        if column_0s[i] > column_1s[i]:
            gamma_bit_string += '0'
            epsilon_bit_string += '1'
        else:
            gamma_bit_string += '1'
            epsilon_bit_string += '0'

    gamma = int(gamma_bit_string, 2)
    epsilon = int(epsilon_bit_string, 2)
    print("Gamma: " + str(gamma))
    print("Epsilon: " + str(epsilon))
    print("Power: " + str(epsilon * gamma))


if __name__ == '__main__':
    run()
