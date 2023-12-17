import pprint


def part1(data):
    grid = [line.strip("\n") for line in data]
    n, m = len(grid), len(grid[0])

    symbol = [[(c != "." and not c.isalnum()) for c in line] for line in grid]
    valid = [[False for _ in range(m)] for _ in range(n)]

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for x in range(n):
        for y in range(m):
            if symbol[x][y]:
                for dx, dy in directions:
                    newx, newy = x + dx, y + dy

                    if (
                        newx < 0
                        or newx >= n
                        or newy < 0
                        or newy >= m
                        or valid[newx][newy]
                    ):
                        continue

                    if grid[newx][newy].isdigit():
                        valid[newx][newy] = True
                        left, right = -1, 1

                        while newy + left >= 0 and grid[newx][newy + left].isdigit():
                            valid[newx][newy + left] = True
                            left -= 1
                        while newy + right < m and grid[newx][newy + right].isdigit():
                            valid[newx][newy + right] = True
                            right += 1

    total = 0
    for i, line in enumerate(valid):
        idx = 0
        curr = 0
        while idx < m:
            if line[idx] == True:
                while idx < m and line[idx] == True:
                    curr = curr * 10 + int(grid[i][idx])
                    idx += 1
                total += curr
                curr = 0
            idx += 1

    print(total)


def part2(data):
    grid = [line.strip("\n") for line in data]
    n, m = len(grid), len(grid[0])

    valid = [[False for _ in range(m)] for _ in range(n)]

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    total = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y] == "*":
                count = 0
                dir_indices = []

                for j, (dx, dy) in enumerate(directions):
                    newx, newy = x + dx, y + dy

                    if newx < 0 or newx > n or newy < 0 or newy > m or valid[newx][newy]:
                        continue

                    if grid[newx][newy].isdigit():
                        valid[newx][newy] = True
                        count += 1
                        dir_indices.append(j)

                        left, right = -1, 1

                        while newy + left >= 0 and grid[newx][newy + left].isdigit():
                            valid[newx][newy + left] = True
                            left -= 1
                        while newy + right < m and grid[newx][newy + right].isdigit():
                            valid[newx][newy + right] = True
                            right += 1

                if count != 2:
                    continue

                prod = 1
                for dir_idx in dir_indices:
                    newx, newy = x + directions[dir_idx][0], y + directions[dir_idx][1]
                    left = 0

                    while newy + left > 0 and grid[newx][newy + left].isdigit():
                        left -= 1

                    newy += left 
                    if not grid[newx][newy].isdigit():
                        newy += 1

                    curr = 0
                    right = 0
                    while newy + right < m and grid[newx][newy + right].isdigit():
                        curr = curr * 10 + int(grid[newx][newy + right])
                        right += 1

                    prod *= curr

                total += prod

    print(total)    

if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
