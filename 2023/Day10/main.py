from math import ceil
from sys import setrecursionlimit

setrecursionlimit(10**9)

def part1(data):
    movements = {
        "|": [(1, 0), (-1, 0)],
        "-": [(0, 1), (0, -1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
        "S": [(0, 1), (0, -1), (1, 0), (-1, 0)],
        ".": []
    }

    startx, starty = None, None

    for x in range(len(data)):
        found = False
        for y in range(len(data[0])):
            if data[x][y] == "S":
                startx = x
                starty = y
                found = True
                break

        if found:
            break
    
    distances = {}
    stack = set()
    
    cycle_length = -1
    def dfs(x, y, curr_len, parent):
        nonlocal cycle_length
        # print(x,y, curr_len, parent)

        if x < 0 or x > len(data) or y < 0 or y > len(data[0]) or data[x][y] == '.':
            return
        
        stack.add((x, y))
        curr_symbol = data[x][y]
        distances[(x, y)] = curr_len

        for dx, dy in movements[curr_symbol]:
            newx, newy = x + dx, y + dy
            if (newx, newy) == parent:
                continue
            if (newx, newy) in stack:
                cycle_length = max(cycle_length, curr_len + 1 - distances[(newx, newy)])
                return
            
            dfs(newx, newy, curr_len+1, (x, y))

        stack.remove((x, y))

    dfs(startx, starty, 1, (startx, starty))

    print(ceil(cycle_length / 2))


def part2(data):
    


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
