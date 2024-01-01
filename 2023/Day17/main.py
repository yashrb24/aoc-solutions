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
 
    rows_prefix = [list(itertools.accumulate(x)) for x in data]
    rows_prefix_rev = [list(itertools.accumulate(reversed(x))) for x in data]
    cols_prefix = [
        list(itertools.accumulate([data[i][j] for i in range(len(data))]))
        for j in range(len(data[0]))
    ]
    cols_prefix_rev = [
        list(itertools.accumulate([data[i][j] for i in range(len(data) -1, -1, -1)]))
        for j in range(len(data[0]))
    ]

 
    movements = []
    for i in range(4, 11):
        movements.append((i, 0))
        movements.append((-i, 0))
        movements.append((0, i))
        movements.append((0, -i))
 
    heapq.heappush(pq, (0, 0, 0, 0))
    n, m = len(data), len(data[0])
 
    while len(pq) != 0:
        distance, curr_x, curr_y, direction = heapq.heappop(pq)
 
        for dx, dy in movements:
            new_x, new_y = curr_x + dx, curr_y + dy
 
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                continue
 
            # assign a direction to the movement
            new_direction = None
            if new_x > curr_x:
                new_direction = 1
            elif new_x < curr_x:
                new_direction = -1
            elif new_y > curr_y:
                new_direction = 2
            else:
                new_direction = -2
 
            # should not turn back or go ahead in the same direction
            if abs(new_direction) == abs(direction):
                continue
 
            # calculate the distance of the step
            step_dist = None
            if new_x > curr_x:
                step_dist = cols_prefix[new_y][new_x] - cols_prefix[new_y][curr_x]
            elif new_x < curr_x:
                step_dist = cols_prefix_rev[new_y][len(cols_prefix_rev[new_y]) - 1 - new_x] - cols_prefix_rev[new_y][len(cols_prefix_rev[new_y]) - 1 - curr_x]
            elif new_y > curr_y:
                step_dist = rows_prefix[new_x][new_y] - rows_prefix[new_x][curr_y]
            else:
                step_dist = rows_prefix_rev[new_x][len(rows_prefix_rev[new_x]) - 1 - new_y] - rows_prefix_rev[new_x][len(rows_prefix_rev[new_x]) - 1 - curr_y]

            # update the distance if it is shorter
            if dist[(new_x, new_y, new_direction)] > distance + step_dist:
                dist[(new_x, new_y, new_direction)] = distance + step_dist
 
                heapq.heappush(
                    pq,
                    (
                        dist[(new_x, new_y, new_direction)],
                        new_x,
                        new_y,
                        new_direction,
                    ),
                )
    

    answer = float("inf")
 
    for key in dist.keys():
        x, y, _ = key
        if x == n - 1 and y == m - 1:
            answer = min(answer, dist[key])
 
    print(answer)
 
 
if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)