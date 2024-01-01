import sys

sys.setrecursionlimit(1000000)
import queue


def bfs(x, y, visited):
    movements = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    q = queue.Queue()
    q.put((x, y))
    while not q.empty():
        x, y = q.get()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in movements:
            q.put((x + dx, y + dy))


def part1(data):
    movements = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    conjugate = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

    visited = set()
    candidates = set()

    curr_x, curr_y = 0, 0
    for line in data:
        direction, step, _ = line.split()
        step = int(step)

        dx, dy = movements[direction]
        conj_dx, conj_dy = conjugate[direction]

        for _ in range(step):
            curr_x += dx
            curr_y += dy
            visited.add((curr_x, curr_y))
            candidates.add((curr_x + conj_dx, curr_y + conj_dy))

    candidates = candidates.difference(visited)

    for x, y in candidates:
        if (x, y) not in visited:
            bfs(x, y, visited)

    print(len(visited))


def part2(data):
    pass


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
