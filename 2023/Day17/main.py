import heapq
from collections import defaultdict
import itertools

def part1(data):
    dist = defaultdict(lambda: float("inf"))
    prev = {}
    pq = []

    heapq.heappush(pq, (0, 0, 0, 3, 0))

    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n, m = len(data), len(data[0])

    while len(pq) != 0:
        distance, curr_x, curr_y, direction, steps = heapq.heappop(pq)
        for dx, dy in movements:
            new_x, new_y = curr_x + dx, curr_y + dy

            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                continue

            new_direction = (new_x - curr_x) + 2 * (new_y - curr_y)

            new_steps = 1 if new_direction != direction else steps + 1

            if new_steps > 3 or new_direction == -direction:
                continue

            if dist[(new_x, new_y, new_direction, new_steps)] > distance + int(
                data[new_x][new_y]
            ):
                dist[(new_x, new_y, new_direction, new_steps)] = distance + int(
                    data[new_x][new_y]
                )

                prev[(new_x, new_y, new_direction, new_steps)] = (
                    curr_x,
                    curr_y,
                    direction,
                    steps,
                )

                heapq.heappush(
                    pq,
                    (
                        dist[(new_x, new_y, new_direction, new_steps)],
                        new_x,
                        new_y,
                        new_direction,
                        new_steps,
                    ),
                )

    answer = float("inf")

    for key in dist.keys():
        x, y, *_ = key
        if x == n - 1 and y == m - 1:
            if answer > dist[key]:
                answer = dist[key]

    print(answer)


def part2(data):
    data = [list(map(int, list(x))) for x in data]
    dist = defaultdict(lambda: float("inf"))
    pq = []
    prev = {}

    rows_prefix = [list(itertools.accumulate(x)) for x in data]
    cols_prefix = [
        list(itertools.accumulate([data[i][j] for i in range(len(data))]))
        for j in range(len(data[0]))
    ] 

    # for row in rows_prefix:
    #     print(row)

    # for col in cols_prefix:
    #     print(col)

    movements = []
    for i in range(4, 11):
        movements.append((i, 0))
        movements.append((-i, 0))
        movements.append((0, i))
        movements.append((0, -i))
    
    heapq.heappush(pq, (0, 0, 0, 0, 0))
    n, m = len(data), len(data[0])

    while len(pq) != 0:
        distance, curr_x, curr_y, direction, steps = heapq.heappop(pq)
        # print("current state", (curr_x, curr_y, direction, steps))

        for dx, dy in movements:
            new_x, new_y = curr_x + dx, curr_y + dy

            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                continue

            new_direction = None
            if new_x > curr_x:
                new_direction = 1
            elif new_x < curr_x:
                new_direction = -1
            elif new_y > curr_y:
                new_direction = 2
            else:
                new_direction = -2

            new_steps = (
                abs(dx + dy) if new_direction != direction else steps + abs(dx + dy)
            )

            if new_steps > 10 or new_direction == -direction:
                continue
            
            step_dist = None
            if new_y == curr_y:
                step_dist = abs(cols_prefix[new_y][new_x] - cols_prefix[new_y][curr_x])
            else:
                step_dist = abs(rows_prefix[new_x][new_y] - rows_prefix[new_x][curr_y])

            # print((curr_x, curr_y), (new_x, new_y), step_dist)

            if dist[(new_x, new_y, new_direction, new_steps)] > distance + step_dist:
                dist[(new_x, new_y, new_direction, new_steps)] = distance + step_dist

                heapq.heappush(
                    pq,
                    (
                        dist[(new_x, new_y, new_direction, new_steps)],
                        new_x,
                        new_y,
                        new_direction,
                        new_steps,
                    ),
                )

                prev[(new_x, new_y, new_direction, new_steps)] = (
                    curr_x,
                    curr_y,
                    direction,
                    steps,
                )

    answer = float("inf")
    curr = None

    for key in dist.keys():
        x, y, *_ = key
        if x == n - 1 and y == m - 1:
            if answer > dist[key]:
                answer = dist[key]
                curr = key

    while curr in prev:
        print(curr)
        curr = prev[curr]
    print(curr)
    print(answer)
        

if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    # part1(data)
    part2(data)
