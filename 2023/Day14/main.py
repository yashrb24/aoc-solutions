import bisect
import sys

# TODO: REWRITE PART1 USING TILT WRITTEN FOR PART2

def print_transformed_list(list_of_lists):
    for sublist in list_of_lists:
        transformed_sublist = [
            "0" if char == "." else "1" if char == "O" else "2" for char in sublist
        ]
        sys.stdout.write(" ".join(transformed_sublist))
        print()


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
    new_grid = list(map(list, zip(*grid)))
    m = len(new_grid[0])
    # print(m)
    score = 0

    for line in new_grid:
        for i, c in enumerate(line):
            if c == "O":
                score += m - i

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
    north_grid = list(map(list, zip(*grid)))
    north_grid_tilted = tilt(north_grid)
    north_grid_tilted_base = list(map(list, zip(*north_grid_tilted)))

    # tilt east
    east_grid = north_grid_tilted_base
    east_grid_tilted = tilt(east_grid)
    east_grid_tilted_base = east_grid_tilted

    # tilt south
    south_grid = [line[::-1] for line in list(map(list, zip(*east_grid_tilted_base)))]
    south_grid_tilted = tilt(south_grid)
    south_grid_tilted_base = list(
        map(list, zip(*[line[::-1] for line in south_grid_tilted]))
    )

    # tilt west
    west_grid = [line[::-1] for line in south_grid_tilted_base]
    west_grid_tilted = tilt(west_grid)
    west_grid_tilted_base = [line[::-1] for line in west_grid_tilted]

    return west_grid_tilted_base


def part2(grid):
    iteration = 0
    offset = 0
    grid_to_cycle = {}
    cycle_to_grid = {}

    while True:
        iteration += 1

        grid = cycle(grid)
        # print(f"After {iteration = }")
        # print_transformed_list(grid)
        # print("=============================================")

        hashed_grid = hash(tuple(map(tuple, grid)))
        if hashed_grid in grid_to_cycle:
            offset = grid_to_cycle[hashed_grid]
            break
        else:
            grid_to_cycle[hashed_grid] = iteration
            cycle_to_grid[iteration] = grid

    total = 1000000000
    cycle_length = iteration - offset
    cycle_count = (total - offset) // cycle_length
    remainder = total - cycle_count * cycle_length - offset

    final_grid = cycle_to_grid[offset + remainder]
    # print(final_grid)
    # print(
    #     f"{offset = } {iteration = } {remainder = } {total = } {offset + remainder = }"
    # )
    print(get_score(final_grid))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
