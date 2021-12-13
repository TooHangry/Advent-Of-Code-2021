def get_matrix():
    file = open('original_input.txt')
    matrix = []
    for line in file:
        temp = []
        for char in line:
            if char != '\n':
                temp.append(int(char))
        matrix.append(temp)
    return matrix


def run():
    matrix = get_matrix()
    row_length = len(matrix[0])
    height = len(matrix)

    low_spots = []

    pockets = [[]]*height

    for i in range(0, height):
        current = matrix[i]

        length_of_pocket = 0
        last = 0
        print(current)

        j = 0
        while j < len(current):
            
            # Start of a pocket
            if (current[j] != 9):
                start = j
                while(current[j] != 9 and j < len(current)):
                    j += 1
                end = j
                print("Pocket from " + str(start) + " to " + str(end))
            
            j += 1


        # for j in range(0, len(current)):
        #     if current[j] == 9:
        #         print("Pocket at x = " + str(last) + ", y = " + str(i) + " for length " + str(length_of_pocket))
        #         length_of_pocket = 0
        #         last = j
        #         while current[j] == 9:
        #             j += 1
        #     else:
        #         length_of_pocket += 1


        row = ''.join([str(c) for c in current]).replace('9', ',')

        vals = row.split(',')
        pockets[i] = [val for val in vals if len(val) > 0]
    print(pockets)

    deepest_checked = 0
    rightest_checked = 0
    for pocket in pockets:
        length = len(pocket)


        print(length)
        
    
    risk_points = [spot + 1 for spot in low_spots]
    tally = 0
    for spot in risk_points:
        tally += spot

    print("The sum of the low spot risk levels is " + str(tally))



if __name__ == '__main__':
    run()