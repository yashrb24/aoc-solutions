def find_horizontal_reflection(grid):
    # print("checking horizontal")
    rows = len(grid)
    # print(f"{rows = }")
    for row in range(1, rows - 1):
        max_dist = min(row + 1, rows - row - 1)
        valid = True
        # print(f"{row = } and {max_dist = }")

        for i in range(max_dist):
            # print(row - i, row + 1 + i)
            if grid[row - i] != grid[row + i + 1]:
                valid = False
                break

        if valid:
            # print(f"{grid = }")
            # print(f"Valid found at {row + 1}")
            return row + 1

    return 0

def find_vertical_from_horizontal(grid):
    new_grid = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]
    result = find_horizontal_reflection(new_grid)
    return result


def find_vertical_reflection(grid):
    cols = len(grid[0])
    for col in range(1, cols - 1):
        max_dist = min(col + 1, cols - col - 1)
        valid = True

        for grid_line in grid:
            if (
                grid_line[col - max_dist+ 1: col + 1][::-1]
                != grid_line[col + 1 : col + 1 + max_dist]
            ):
                valid = False
                break

        if valid:
            # print(f"{grid = }")
            # print(f"Valid column is {col + 1}")
            return col + 1

    return 0


def part1(data):
    grid = []
    total = 0

    for line in data:
        if line == "":
            horizontal = find_horizontal_reflection(grid)
            vertical = 0
            if horizontal == 0:
                vertical = find_vertical_from_horizontal(grid)
            total += horizontal * 100 + vertical
            grid = []
        else:
            grid.append(line)
    
    horizontal = find_horizontal_reflection(grid)
    vertical = 0
    if horizontal == 0:
        vertical = find_vertical_from_horizontal(grid)
    total += horizontal * 100 + vertical

    print(total)


def part2(data):
    pass


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
