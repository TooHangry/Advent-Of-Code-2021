def get_latern_fish():
    file = open('input.txt', 'r')
    fish = []
    for line in file.readlines():
        fish += [int(f.strip()) for f in line.split(',')]
    return fish


def get_sum(buckets: dict):
    return sum([buckets.get(val) for val in buckets])


def run():
    # Fish list is essentially day 0
    fish_list = get_latern_fish()
    DAYS = 256

    buckets = {
        '0': fish_list.count(0),
        '1': fish_list.count(1),
        '2': fish_list.count(2),
        '3': fish_list.count(3),
        '4': fish_list.count(4),
        '5': fish_list.count(5),
        '6': fish_list.count(6),
        '7': fish_list.count(7),
        '8': fish_list.count(8),
    }

    # Each day, decrement the list, adding an '8' onto the end if a fish dies (0)
    for current_day in range(1, DAYS + 1):
        # for i in range(0, 9):
        to_become_sixes = buckets['0']  # Previous 0s
        buckets['0'] = buckets['1']  # Decrement 1s
        buckets['1'] = buckets['2']  # Decrement 2s
        buckets['2'] = buckets['3']  # Decrement 3s
        buckets['3'] = buckets['4']  # Decrement 4s
        buckets['4'] = buckets['5']  # Decrement 5s
        buckets['5'] = buckets['6']  # Decrement 6s
        buckets['6'] = buckets['7']  # Decrement 7s
        buckets['7'] = buckets['8']  # Decrement 8s
        buckets['6'] += to_become_sixes  # Add the dead ones back
        buckets['8'] = to_become_sixes  # Spawn new fish
    print(get_sum(buckets))


if __name__ == '__main__':
    run()
