def get_crab_positions():
    file = open('input.txt', 'r')
    crabs = []
    for line in file.readlines():
        crabs += [int(f.strip()) for f in line.split(',')]
    return crabs

def get_closest_position(crabs, mid):
    return min(crabs, key=lambda x:abs(x-mid))

def create_buckets():
    crab_positions = get_crab_positions()
    buckets = dict()
    for position in crab_positions:
        if f'{position}' not in buckets:
            buckets.update({str(position): 0})
        buckets[str(position)] += 1
    
    return buckets

def get_fuel_for_position(crabs, position):
    fuel = 0
    for crab in crabs:
        fuel += abs(int(crab) - position)*crabs.get(crab)
    return fuel

def run():
    # Horizontal positions
    crab_positions = create_buckets()

    # Min and max bounds
    min_position = int(min(crab_positions))
    max_position = int(max(crab_positions))

    converged_position = 0
    fuel_required = -1
    for position in range(min_position, max_position + 1):
        fuel_for_position = get_fuel_for_position(crab_positions, position)

        if fuel_required == -1 or fuel_for_position < fuel_required:
            fuel_required = fuel_for_position
            converged_position = position

    print(f'The crabs can converge on the horizontal position {converged_position}')
    print(f'The manuver will cost {fuel_required} fuel')

    # # Determine the median?
    # crab_positions.sort()
    # median = sum(crab_positions) / len(crab_positions)
    # mid = get_closest_position(crab_positions, median)



if __name__ == '__main__':
    run()