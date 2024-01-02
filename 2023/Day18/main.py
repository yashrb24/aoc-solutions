import numpy as np
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
    x_coords, y_coords = [], []
    direction_dict = {"0": "R", "1": "U", "2": "L", "3": "D"}
    movements = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    curr_x, curr_y = 0, 0
    boundary_pts = 0

    for line in data:
        _, _, hex_code = line.split()
        steps = int(hex_code[2:-2], 16)
        direction = direction_dict[hex_code[-2]]

        x_steps, y_steps = movements[direction]

        curr_x = curr_x + x_steps * steps
        curr_y = curr_y + y_steps * steps
        boundary_pts += steps

        x_coords.append(curr_x)
        y_coords.append(curr_y)

    x_coords = np.array(x_coords)
    y_coords = np.array(y_coords)

    i = np.arange(len(x_coords))
    
    # shoelace formula
    area = np.abs(np.sum(x_coords[i-1] * y_coords[i] - x_coords[i] * y_coords[i-1]) * 0.5)

    # interior points
    interior_pts = area - boundary_pts * 0.5 + 1

    answer = boundary_pts + interior_pts

    print(int(answer))



if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
