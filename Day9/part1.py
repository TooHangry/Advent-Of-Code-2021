def get_matrix():
    file = open('input.txt')
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
    for i in range(0, height):
        # For each row, determine next and previous rows
        next_row = matrix[i + 1] if i < height - 1 else None
        previous_row = matrix[i - 1] if i > 0 else None
        current_row = matrix[i]

        for j in range(0, row_length):
            current_value = current_row[j]

            is_down_higher = next_row is None or (next_row is not None and current_value < next_row[j])
            is_up_higher = previous_row is None or (previous_row is not None and current_value < previous_row[j])
            is_left_higher = (j - 1) < 0 or ((j - 1) > -1 and current_value < current_row[j - 1])
            is_right_higher = ((j + 1) > row_length - 1)  or ((j + 1) < row_length and current_value < current_row[j + 1])

            if is_down_higher and is_up_higher and is_left_higher and is_right_higher:
                low_spots.append(current_value)
    
    risk_points = [spot + 1 for spot in low_spots]
    tally = 0
    for spot in risk_points:
        tally += spot

    print("The sum of the low spot risk levels is " + str(tally))



if __name__ == '__main__':
    run()