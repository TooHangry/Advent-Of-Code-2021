def get_output():
    file = open('input.txt', 'r')
    output = []
    for line in file:
        line = line[line.index(' | ') + len(' | '):].replace('\n', '').split(' ')
        output += line
    return output


def get_input():
    file = open('input.txt', 'r')
    input = []
    for line in file:
        line = line[0: line.index(' | ')].replace('\n', '').split(' ')
        input += line
    return input

def determine_number(word, mappings):
    # Start with 8
    if mappings['top'] in word and mappings['top_left'] in word and mappings['top_right'] in word and mappings['middle'] in word and mappings['bottom_left'] in word and mappings['bottom_right'] in word and mappings['bottom'] in word:
        return 8
    elif mappings['top'] in word and mappings['top_left'] in word and mappings['top_right'] in word and mappings['middle'] in word and mappings['bottom_right'] in word and mappings['bottom'] in word:
        return 9
    elif mappings['top'] in word and mappings['top_left'] in word and mappings['top_right'] in word and mappings['bottom_left'] in word and mappings['bottom_right'] in word and mappings['bottom'] in word:
        return 0
    elif mappings['top'] in word and mappings['top_left'] in word and mappings['middle'] in word and mappings['bottom_left'] in word and mappings['bottom_right'] in word and mappings['bottom'] in word:
        return 6
    elif mappings['top'] in word and mappings['top_left'] in word and mappings['middle'] in word and mappings['bottom_right'] in word and mappings['bottom'] in word:
        return 5
    elif mappings['top'] in word and mappings['top_right'] in word and mappings['middle'] in word and mappings['bottom_left'] in word and mappings['bottom'] in word:
        return 2
    elif mappings['top'] in word and mappings['top_right'] in word and mappings['middle'] in word and mappings['bottom_right'] in word and mappings['bottom'] in word:
        return 3
    elif mappings['top_left'] in word and mappings['top_right'] in word and mappings['middle'] in word and mappings['bottom_right'] in word:
        return 4
    elif mappings['top'] in word and mappings['top_right'] in word and mappings['bottom_right'] in word:
        return 7
    elif mappings['top_right'] in word and mappings['bottom_right'] in word:
        return 1

def determine_mappings():
    file = open('input.txt', 'r')
    input = []
    summation = 0
    for line in file:
        input = line[0: line.index(' | ')].replace('\n', '').split(' ')
        output = line[line.index(' | ') + len(' | '):].replace('\n', '').split(' ')

        # print(output)
        # Words 0 words, 1 words, 2 words, 3 words
        words = [
            list(filter(lambda x: len(x) == 0, input)),
            list(filter(lambda x: len(x) == 1, input)),
            list(filter(lambda x: len(x) == 2, input)),
            list(filter(lambda x: len(x) == 3, input)),
            list(filter(lambda x: len(x) == 4, input)),
            list(filter(lambda x: len(x) == 5, input)),
            list(filter(lambda x: len(x) == 6, input)),
            list(filter(lambda x: len(x) == 7, input)),
            list(filter(lambda x: len(x) == 8, input)),
        ]

        mappings = {
            'top': 'a',
            'top_left': 'b',
            'top_right': 'c',
            'middle': 'd',
            'bottom_left': 'e',
            'bottom_right': 'f',
            'bottom': 'g'
        }

        # Determine '1' contenders (all with length 2)
        # Determine contenders for '7' (length 3)
        # Determine contenders for '8' (length 7)
        # Determine contenders for '4' (length 4)
        contenders = [
            [],
            words[2][0],
            [],
            [],
            words[4][0],
            [],
            [],
            words[3][0],
            words[7][0],
        ]

        # '1' and '7' have the most overlap (1 has cf, 7 has acf)
        # This can be leveraged to solidify c and f
        one_chars = [c for c in contenders[1]]
        seven_chars = contenders[7]
        top_bar_char = ''
        for char in seven_chars:
            for letter in char:
                if letter not in one_chars:
                    top_bar_char = letter
        
        # Sets the top bar of the original mapping
        mappings['top'] = top_bar_char

        # We know the right upper and lower bars - chars in one_chars. Do not know the order.
        # Can get the middle bar by taking the 6 values and finding the value 
        # not in any of the five-segment numbers
        six_chars = []
        for word in words[6]:
            for c in word:
                six_chars.append(c)
        six_chars = list(filter(lambda x: six_chars.count(x) == 2, six_chars)) # List of values in 'gaps' (middle (0), top-right (6), bottom-left (9))


        five_chars = []
        # Add the five chars
        for word in words[5]:
            for char in word:
                five_chars.append(char)
        # Add the eight chars
        five_chars += [c for c in contenders[8]]

        four_chars = [c for c in contenders[4]]
        middle_bar_char = [c for c in six_chars if c not in one_chars and c in four_chars][0]
        mappings['middle'] = middle_bar_char

        bottom_left_char = [c for c in six_chars if c not in one_chars and c != middle_bar_char][0]
        mappings['bottom_left'] = bottom_left_char

        top_left_char = [c for c in four_chars if c not in one_chars and c != middle_bar_char][0]
        mappings['top_left'] = top_left_char

        bottom_bar_char = [c for c in contenders[8] if c not in one_chars and c != top_bar_char and c != top_left_char and c != bottom_left_char and c != middle_bar_char][0]
        mappings['bottom'] = bottom_bar_char

        current = [top_left_char, bottom_left_char, top_bar_char, middle_bar_char, bottom_bar_char]
        contenders_six = []
        for word in words[6]:
            for c in word:
                contenders_six.append(c)


        potentials = list(filter(lambda x: contenders_six.count(x) != 2, contenders_six))
        bottom_right_char = [c for c in potentials if c not in current][0]
        mappings['bottom_right'] = bottom_right_char
        
        top_right_char = [c for c in one_chars if c != bottom_right_char][0]
        mappings['top_right'] = top_right_char

        # Now, iterate through the output and determine the numbers
        start = 1000
        end = 0
        for word in output:
            end = end + determine_number(word, mappings)*start
            start = start / 10
        summation += end
        print(' '.join(output) + ": " + str(end))
    return summation


def run():
    # Part 2
    print(determine_mappings())



if __name__ == '__main__':
    run()
