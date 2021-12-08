class BingoBoard:
    def __init__(self, board_string):
        self.board = []
        while(len(board_string) > 0):
            row = board_string[0:board_string.find('\n')]
            board_string = board_string[board_string.find('\n') + 1:]
            vals = row.split(' ')

            sanitized = []
            for val in vals:
                if len(val) > 0:
                    sanitized.append({ 'val': int(val), 'marked': False})
            
            self.board.append(sanitized)
            
    def mark(self, number):
        # Mark items on a per-row basis
        for row in self.board:
            for entry in row:
                if entry['val'] == number:
                    entry['marked'] = True

    def has_bingo(self):
        row_counts = [0]*len(self.board)
        column_counts = [0]*len(self.board)
        
        j = 0
        for row in self.board:
            valid = ''

            for i in range(0, len(row)):
                entry = row[i]
                if entry['marked']:

                    row_counts[j] += 1
                    column_counts[i] += 1
            j += 1
            for entry in row:
                valid += ' 0 ' if not entry['marked'] else ' ' +str(entry['val']) + ' '

        for r in row_counts:
            if r >= len(self.board):
                return True
        for c in column_counts:
            if c >= len(self.board):
                return True
    
    def get_sum_of_unmarked_spots(self):
        sum = 0
        for r in self.board:
            for e in r:
                if not e['marked']:
                    sum += e['val']
        return sum

    def display(self):
        for line in self.board:
            print(line)
        print("\n")

def get_boards():
    file = open('input.txt', 'r')
    current = ''
    boards = []
    for line in file:
        current += line.replace('\n', '') + '\n' if len(line) > 1 else ''
        if len(line) < 2:
            boards.append(BingoBoard(current))
            current = ''
    return boards

def get_drawings():
    file = open('drawings.txt', 'r')
    drawings = []
    for line in file:
        words = line.split(',')
        for d in words:
            drawings.append(int(d.strip()))
    return drawings
    


def run():
    boards = get_boards()
    drawings = get_drawings()

    d = ''
    last_call = 0
    for drawing in drawings:
        # Mark and check all boards
        last_call = drawing
        d += str(drawing) + ' '
        for b in boards:
            b.mark(drawing)
            if b.has_bingo():
                print(d)
                b.display()
                unmarked = b.get_sum_of_unmarked_spots()
                print(unmarked * last_call)
                return
    

if __name__ == '__main__':
    run()