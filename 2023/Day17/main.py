import heapq
from collections import defaultdict


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
    pass


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
