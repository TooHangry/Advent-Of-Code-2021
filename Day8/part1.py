def get_output():
    file = open('input.txt', 'r')
    output = []
    for line in file:
        line = line[line.index(' | ') + len(' | '):].replace('\n', '').split(' ')
        output += line
    return output


def determine_mappings(digits):
    output = get_output()
    # print(output)
    # Words 0 words, 1 words, 2 words, 3 words
    words = [
        list(filter(lambda x: len(x) == 0, output)),
        list(filter(lambda x: len(x) == 1, output)),
        list(filter(lambda x: len(x) == 2, output)),
        list(filter(lambda x: len(x) == 3, output)),
        list(filter(lambda x: len(x) == 4, output)),
        list(filter(lambda x: len(x) == 5, output)),
        list(filter(lambda x: len(x) == 6, output)),
        list(filter(lambda x: len(x) == 7, output)),
    ]

    mappings = {
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'd': 'd',
        'e': 'e',
        'f': 'f'
    }

    # Determine '1' contenders (all with length 2)
    # Determine contenders for '7' (length 3)
    # Determine contenders for '8' (length 7)
    # Determine contenders for '4' (length 4)
    contenders = [
        [],
        words[2],
        [],
        [],
        words[4],
        [],
        [],
        words[3],
        words[7],
        []
    ]

    # '1' and '7' have the most overlap (1 has cf, 7 has acf)
    # This can be leveraged to solidify c and f
    unique_ones_in_seven = []
    unique_ones_in_four = []
    unique_ones_in_eight = []
    for word in contenders[1]:
        for contender in contenders[7]:
            if word in contender:
                if word not in unique_ones_in_seven:
                    unique_ones_in_seven.append(word)
        for contender in contenders[4]:
            if word in contender:
                if word not in unique_ones_in_four:
                    unique_ones_in_four.append(word)
        for contender in contenders[8]:
            if word in contender:
                if word not in unique_ones_in_eight:
                    unique_ones_in_eight.append(word)
                print(word, contender)

    ones = len(contenders[1])
    fours = len(contenders[4])
    sevens = len(contenders[7])
    eights = len(contenders[8])
    print('Ones: ' + str(ones))
    print('Fours: ' + str(fours))
    print('Sevens: ' + str(sevens))
    print('Eights: ' + str(eights))

    print('Sum: ' + str(ones + fours + sevens + eights))

    print(unique_ones_in_seven, unique_ones_in_four, unique_ones_in_eight)



def run():
    digits = [
        {
            'digit': 0,
            'chars': ['a', 'b', 'c', 'e', 'f', 'g'],
            'count': 6
        },
        {
            'digit': 1,
            'chars': ['c', 'f'],
            'count': 2
        },
        {
            'digit': 2,
            'chars': ['a', 'c', 'd', 'e', 'g'],
            'count': 5
        },
        {
            'digit': 3,
            'chars': ['a', 'c', 'd', 'f', 'g'],
            'count': 5
        },
        {
            'digit': 4,
            'chars': ['b', 'c', 'd', 'f'],
            'count': 4
        },
        {
            'digit': 5,
            'chars': ['a', 'b', 'd', 'f', 'g'],
            'count': 5
        },
        {
            'digit': 6,
            'chars': ['a', 'b', 'd', 'e', 'f', 'g'],
            'count': 6
        },
        {
            'digit': 7,
            'chars': ['a', 'c', 'f'],
            'count': 3
        },
        {
            'digit': 8,
            'chars': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
            'count': 7
        },
        {
            'digit': 9,
            'chars': ['a', 'b', 'c', 'd', 'f', 'g'],
            'count': 6
        }
    ]

    # Part one
    determine_mappings(digits)


if __name__ == '__main__':
    run()
