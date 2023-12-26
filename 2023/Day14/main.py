import bisect
from pprint import pprint as print


def part1(data):
    grid = [*zip(*data)]
    total = 0

    for line in grid:
        available = []
        rocks = []
        fixed = [0]

        for i, c in enumerate(line):
            if c == ".":
                available.append(i + 1)
            elif c == "#":
                fixed.append(i + 1)
            elif c == "O":
                rocks.append(i + 1)
            else:
                return None

        for rock in rocks:
            # print(f"{available = }")
            # print(f"{rocks = } and current {rock = }")
            # print(f"{fixed = }")

            idx = bisect.bisect(fixed, rock) - 1
            fixed_idx = bisect.bisect(available, fixed[idx])

            if fixed_idx == len(available) or available[fixed_idx] > rock:
                total += len(grid[0]) - rock + 1
                continue
            else:
                total += len(grid[0]) - available[fixed_idx] + 1
                res = available.pop(fixed_idx)
                bisect.insort(available, rock)

    print(total)


def get_score(grid):
    score = 0
    m = len(grid[0])

    for line in grid:
        for i, c in enumerate(line):
            if c == "O":
                score += m + 1 - i

    return score


def reconstruct(a_list, r_list, f_list):
    n = len(a_list)
    grid = [[] for _ in range(n)]

    for line, a, r, f in zip(grid, a_list, r_list, f_list):
        # print(f"{a = }")
        # print(f"{r = }")
        # print(f"{f = }")
        # print("\n\n")
        m = max(max(a, default=0), max(r, default=0), max(f, default=0))

        for j in range(1, m + 1):
            if j in a:
                line.append(".")
            elif j in r:
                line.append("O")
            elif j in f:
                line.append("#")
        # print(f"{line = }")
    return grid


def tilt(grid):
    available_list = []
    rocks_list = []
    fixed_list = []

    for line in grid:
        available = []
        rocks = []
        fixed = [0]

        for i, c in enumerate(line):
            if c == ".":
                available.append(i + 1)
            elif c == "#":
                fixed.append(i + 1)
            elif c == "O":
                rocks.append(i + 1)
            else:
                return None

        new_rocks = []
        for rock in rocks:
            # print(f"{available = }")
            # print(f"{fixed = }")
            # print(f"{rocks = } and {new_rocks = } and current {rock = }")
            # print("")

            idx = bisect.bisect(fixed, rock) - 1
            fixed_idx = bisect.bisect(available, fixed[idx])

            if fixed_idx == len(available) or available[fixed_idx] > rock:
                new_rocks.append(rock)
                continue
            else:
                # rocks.remove(rock)
                res = available.pop(fixed_idx)
                new_rocks.append(res)
                bisect.insort(available, rock)

        available_list.append(set(available))
        rocks_list.append(set(new_rocks))
        fixed_list.append(set(fixed))

    grid = reconstruct(available_list, rocks_list, fixed_list)
    # print(grid)
    return grid


def cycle(grid):
    # tilt north
    north_grid = list(map(list, zip(*curr)))
    north_grid_tilted = tilt(north_grid)
    north_grid_tilted_base = list(map(list, zip(*north_grid_tilted)))

    # tilt east
    east_grid = north_grid_tilted_base
    east_grid_tilted = tilt(east_grid)
    east_grid_tilted_base = east_grid_tilted

    # tilt south
    south_grid = [line[::-1] for line in list(map(list, zip(*east_grid_tilted_base)))]
    south_grid_tilted = tilt(south_grid)
    south_grid_tilted_base = list(map(list, zip(*[line[::-1] for line in south_grid_tilted])))

    # tilt west
    west_grid = [line[::-1] for line in south_grid_tilted_base]
    west_grid_tilted = tilt(west_grid)
    west_grid_tilted_base = [line[::-1] for line in west_grid_tilted]

    return west_grid_tilted_base

def part2(grid):
    prev = grid
    curr = grid

    cycle = 0

    print(curr)
    print("")
    while True:
        # tilt north
        north_grid = list(map(list, zip(*curr)))
        north_grid_tilted = tilt(north_grid)
        north_grid_tilted_base = list(map(list, zip(*north_grid_tilted)))
        # print(north_grid_tilted_base)
        # print("")
        # print("")
        # print("")

        # tilt east
        east_grid = north_grid_tilted_base
        east_grid_tilted = tilt(east_grid)
        east_grid_tilted_base = east_grid_tilted
        # print(east_grid_tilted_base)
        # print("")
        # print("")
        # print("")

        # tilt south
        south_grid = [line[::-1] for line in list(map(list, zip(*east_grid_tilted_base)))]
        south_grid_tilted = tilt(south_grid)
        # south_grid_tilted_base = [*zip(*[line[::-1] for line in south_grid_tilted])]
        south_grid_tilted_base = list(map(list, zip(*[line[::-1] for line in south_grid_tilted])))
        # print(south_grid_tilted_base)
        # print("")
        # print("")
        # print("")


        # tilt west
        west_grid = [line[::-1] for line in south_grid_tilted_base]
        west_grid_tilted = tilt(west_grid)
        west_grid_tilted_base = [line[::-1] for line in west_grid_tilted]
        # print(west_grid_tilted_base)
        # print("")
        # print("")
        # print("")

        
        curr = west_grid_tilted_base

        # print("========================================================================")
        if curr == prev:
            break

        cycle += 1
        print(f"{cycle = }")
        prev = curr

    print(get_score(curr))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    # part1(data)
    part2(data)
