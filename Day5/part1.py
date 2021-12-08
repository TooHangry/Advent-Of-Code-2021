class ThermalRange():
    def __init__(self, coords):
        self.x_range = []
        self.y_range = []
        self.is_valid = False
        pair1 = [int(coord)
                 for coord in coords[0:coords.index(' -> ')].split(',')]
        pair2 = [int(coord) for coord in coords[coords.index(
            ' -> ')+len(' -> '):].split(',')]

        x1 = pair1[0]
        x2 = pair2[0]
        y1 = pair1[1]
        y2 = pair2[1]

        if x1 == x2 or y1 == y2:
            self.is_valid = True
            for i in range(min(x1, x2), max(x1, x2) + 1):
                self.x_range.append(i)

            for i in range(min(y1, y2), max(y1, y2) + 1):
                self.y_range.append(i)

    def get_max_x(self):
        if len(self.x_range) > 0:
            return self.x_range[len(self.x_range) - 1]
        return 0

    def get_max_y(self):
        if len(self.y_range) > 0:
            return self.y_range[len(self.y_range) - 1]
        return 0

    def get_x_range(self):
        return self.x_range

    def get_y_range(self):
        return self.y_range

    def get_is_valid(self):
        return self.is_valid


class Grid():
    def __init__(self, columns, rows):
        self.grid_column_count = columns
        self.grid_rows = [[0 for i in range(columns)] for j in range(rows)]

    def display(self):
        for row in self.grid_rows:
            print(''.join([str(item) for item in row]).replace('0', '.'))
        print('\n')

    def detect(self, x_vals, y_vals):
        # Iterate y value
        for y in y_vals:
            # Iterate x value
            for x in x_vals:
                self.grid_rows[y][x] += 1
    
    def get_overlapping_lines(self):
        safe_zone = 0
        # Iterate y value
        for y in range(0, len(self.grid_rows)):
            # Iterate x value
            for x in range(0, self.grid_column_count):
                if self.grid_rows[y][x] > 1:
                    safe_zone += 1
        
        return safe_zone


def max(one, two):
    return one if one > two else two


def min(one, two):
    return one if one < two else two


def run():
    # Get ranges
    file = open('input.txt', 'r')
    # ranges = [ThermalRange('0,9 -> 5,9')]
    ranges = []
    for line in file:
        ranges.append(ThermalRange(line))

    # Initialize grid
    max_x = 0
    max_y = 0
    for r in ranges:
        r_x = r.get_max_x()
        r_y = r.get_max_y()

        if r_x > max_x:
            max_x = r_x
        if r_y > max_y:
            max_y = r_y
    grid = Grid(max_x + 1, max_y + 1)
    grid.display()

    # Apply Ranges
    for r in ranges:
        if r.get_is_valid():
            grid.detect(r.get_x_range(), r.get_y_range())

    grid.display()

    print(grid.get_overlapping_lines())


if __name__ == '__main__':
    run()
