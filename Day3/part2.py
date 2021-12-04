def get_binary():
    # return [
    #     '00100',
    #     '11110',
    #     '10110',
    #     '10111',
    #     '10101',
    #     '01111',
    #     '00111',
    #     '11100',
    #     '10000',
    #     '11001',
    #     '00010',
    #     '01010'
    # ]
    file = open('input.txt', 'r')
    return [l.replace('\n', '') for l in file.readlines()]


def get_gamma(binary_strings):
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
        elif column_0s[i] == column_1s[i]:
            gamma_bit_string += 'r'
            epsilon_bit_string += 'r'
        else:
            gamma_bit_string += '1'
            epsilon_bit_string += '0'

    return gamma_bit_string, epsilon_bit_string


def run():
    binary_strings = get_binary()
    res = get_gamma(binary_strings)
    gamma_bit_string = res[0]
    epsilon_bit_string = res[1]

    starting_gamma_string = ''
    flag = False
    i = 0
    while (not flag and len(gamma_bit_string) > 0):
        # Gamma
        gamma_next = gamma_bit_string[i]
        starting_gamma_string += '1' if gamma_next == 'r' else gamma_next
        i += 1

        binary_strings = [
            b for b in binary_strings if b.startswith(starting_gamma_string)]

        if len(binary_strings) == 1:
            flag = True
        if(len(binary_strings) > 0):
            gamma_bit_string = get_gamma(binary_strings)[0]
    oxygen_rating = int(binary_strings[0], 2)

    starting_epsilon_string = ''
    binary_strings = get_binary()
    print(epsilon_bit_string)
    flag = False
    i = 0
    while (not flag and len(epsilon_bit_string) > 0):
        # Epsilon
        epsilon_next = epsilon_bit_string[i]
        starting_epsilon_string += '0' if epsilon_next == 'r' else epsilon_next
        i += 1

        binary_strings = [b for b in binary_strings if b.startswith(
            starting_epsilon_string)]

        if len(binary_strings) == 1:
            flag = True
        if(len(binary_strings) > 0):
            epsilon_bit_string = get_gamma(binary_strings)[1]
    C02_scrubber_rating = int(binary_strings[0], 2)

    print('Oxygen Generator Rating: ' + str(oxygen_rating))
    print('C02 Scrubber Rating: ' + str(C02_scrubber_rating))
    print('Life Support Rating: ' + str(C02_scrubber_rating * oxygen_rating))


if __name__ == '__main__':
    run()
