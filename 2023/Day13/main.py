def find_horizontal_reflection(grid):
    rows = len(grid)

    for row in range(rows - 1):
        max_dist = min(row + 1, rows - row - 1)
        valid = True
        for i in range(max_dist):
            if grid[row - i] != grid[row + i + 1]:
                valid = False
                break

        if valid:
            return row + 1

    return 0


def find_vertical_reflection(grid):
    new_grid = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]
    result = find_horizontal_reflection(new_grid)
    return result


def part1(data):
    grid = []
    total = 0

    for line in data:
        if line == "":
            horizontal = find_horizontal_reflection(grid)
            vertical = 0
            if horizontal == 0:
                vertical = find_vertical_reflection(grid)
            total += horizontal * 100 + vertical
            grid = []
        else:
            grid.append(line)

    horizontal = find_horizontal_reflection(grid)
    vertical = 0
    if horizontal == 0:
        vertical = find_vertical_reflection(grid)
    total += horizontal * 100 + vertical

    print(total)


def part2(data):
    pass


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
