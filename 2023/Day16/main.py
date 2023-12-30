import sys
sys.setrecursionlimit(100000000)

visited = set()
visited_directions = set()

def dfs(x, y, grid, direction):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x, y, direction) in visited_directions:
        return

    visited.add((x, y))
    visited_directions.add((x, y, direction))
    # print((x, y))

    tile = grid[x][y]
    if direction == "right":
        # print(x, y, "right")
        if tile == "." or tile == "-":
            dfs(x, y + 1, grid, "right")
        elif tile == "/":
            dfs(x - 1, y, grid, "up")
        elif tile == "\\":
            dfs(x + 1, y, grid, "down")
        elif tile == "|":
            dfs(x + 1, y, grid, "down")
            dfs(x - 1, y, grid, "up")

    elif direction == "left":
        # print(x, y, "left")
        if tile == "." or tile == "-":
            dfs(x, y - 1, grid, "left")
        elif tile == "/":
            dfs(x + 1, y, grid, "down")
        elif tile == "\\":
            dfs(x - 1, y, grid, "up")
        elif tile == "|":
            dfs(x + 1, y, grid, "down")
            dfs(x - 1, y, grid, "up")

    elif direction == "up":
        # print(x, y, "up")
        if tile == "." or tile == "|":
            dfs(x - 1, y, grid, "up")
        elif tile == "/":
            dfs(x, y + 1, grid, "right")
        elif tile == "\\":
            dfs(x, y - 1, grid, "left")
        elif tile == "-":
            dfs(x, y + 1, grid, "right")
            dfs(x, y - 1, grid, "left")

    elif direction == "down":
        # print(x, y, "down")

        if tile == "." or tile == "|":
            dfs(x + 1, y, grid, "down")
        elif tile == "/":
            dfs(x, y - 1, grid, "left")
        elif tile == "\\":
            dfs(x, y + 1, grid, "right")
        elif tile == "-":
            dfs(x, y + 1, grid, "right")
            dfs(x, y - 1, grid, "left")


def part1(data):
    dfs(0, 0, data, "right")
    print(len(visited))

def part2(data):
    global visited, visited_directions
    answer = -1

    for y in range(len(data[0])):
        visited = set()
        visited_directions = set()
        dfs(0, y, data, "down")
        answer = max(answer, len(visited))

    print(answer)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    # part1(data)
    part2(data)
