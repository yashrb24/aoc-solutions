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
        print(f"{a = }")
        print(f"{r = }")
        print(f"{f = }")
        print("\n\n")
        m = max(max(a, default=0), max(r, default=0), max(f, default=0))
        
        for j in range(1, m + 1):
            if j in a:
                line.append(".")
            elif j in r:
                line.append("O")
            elif j in f:
                line.append("#")
            else:
                AssertionError()
        print(f"{line = }")
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

        for rock in rocks:
            idx = bisect.bisect(fixed, rock) - 1
            fixed_idx = bisect.bisect(available, fixed[idx])

            if fixed_idx == len(available) or available[fixed_idx] > rock:
                continue
            else:
                rocks.remove(rock)
                available.pop(fixed_idx)
                bisect.insort(available, rock)

        available_list.append(set(available))
        rocks_list.append(set(rocks))
        fixed_list.append(set(fixed))

    grid = reconstruct(available_list, rocks_list, fixed_list)
    return grid


def part2(grid):
    prev = grid
    curr = grid

    cycle = 0

    while True:
        # tilt north
        north_grid = [*zip(*curr)]
        north_grid_tilted = tilt(north_grid)
        north_grid_tilted_base = [*zip(*north_grid_tilted)]

        # tilt west
        west_grid = [line[::-1] for line in north_grid_tilted_base]
        west_grid_tilted = tilt(west_grid)
        west_grid_tilted_base = [line[::-1] for line in west_grid_tilted]

        # tilt south
        south_grid = [line[::-1] for line in [*zip(*west_grid_tilted_base)]]
        south_grid_tilted = tilt(south_grid)
        south_grid_tilted_base = [*zip(*[line[::-1] for line in south_grid_tilted])]

        # tilt east
        curr = tilt(south_grid_tilted_base)
        print(curr)
        print("")
        if curr == prev:
            break

        cycle += 1
        prev = curr

    print(get_score(curr))

if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    # part2(data)
