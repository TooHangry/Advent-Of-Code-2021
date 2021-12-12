
def get_latern_fish():
    file = open('input.txt', 'r')
    fish = []
    for line in file.readlines():
        fish += [int(f.strip()) for f in line.split(',')]
    return fish


def run():
    # Fish list is essentially day 0
    fish_list = get_latern_fish()
    DAYS = 256

    # Each day, decrement the list, adding an '8' onto the end if a fish dies (0)
    for current_day in range(1, DAYS + 1):
        print("After day " + str(current_day) + ": ")
        to_add = []
        for i in range(0, len(fish_list)):
            if fish_list[i] > 0:
                fish_list[i] -= 1
            elif fish_list[i] == 0:
                fish_list[i] = 6
                to_add.append(8)

        fish_list = fish_list + to_add
        # print(','.join([str(f) for f in fish_list]))
        print(len(fish_list))


if __name__ == '__main__':
    run()
