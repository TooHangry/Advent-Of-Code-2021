class ThermalRange():
    def __init__(self, coords):
        self.points = []

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
            if x1 == x2:
                y1 = min(pair1[1], pair2[1])
                y2 = max(pair1[1], pair2[1])
                while y2 >= y1:
                    self.points.append((x1, y1))
                    y1 += 1
            elif y2 == y1:
                x1 = min(pair1[0], pair2[0])
                x2 = max(pair1[0], pair2[0])

                while x2 >= x1:
                    self.points.append((x1, y1))
                    x1 += 1
            print(self.points)
        else:
            # get diagonal
            should_decrement_x = x1 > x2
            should_decrement_y = y1 > y2
            while x1 != x2 and y1 != y2:
                self.points.append((x1, y1))
                x1 = x1 - 1 if should_decrement_x else x1 + 1
                y1 = y1 - 1 if should_decrement_y else y1 + 1
            self.points.append((x1, y1))

    def get_max_x(self):
        max = 0
        if len(self.points) > 0:
            for tup in self.points:
                if tup[0] > max:
                    max = tup[0]
        return max

    def get_max_y(self):
        max = 0
        if len(self.points) > 0:
            for tup in self.points:
                if tup[1] > max:
                    max = tup[1]
        return max

    def get_points(self):
        return self.points


class Grid():
    def __init__(self, columns, rows):
        self.grid_column_count = columns
        self.grid_rows = [[0 for i in range(columns)] for j in range(rows)]

    def display(self):
        for row in self.grid_rows:
            print(''.join([str(item) for item in row]).replace('0', '.'))
        print('\n')

    def detect(self, points):
        print(points)
        for point in points:
            self.grid_rows[point[1]][point[0]] += 1

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
        grid.detect(r.get_points())

    grid.display()

    print(grid.get_overlapping_lines())


if __name__ == '__main__':
    run()
