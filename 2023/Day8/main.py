import math


def part1(data):
    path = data[0]

    n = len(data)
    graph = {}

    for i in range(2, n):
        line = data[i]
        node, adj = line.split(" = ")
        left, right = adj[1:-1].split(", ")
        graph[node] = {"L": left, "R": right}

    curr = "AAA"
    idx = 0
    cnt = 0

    while curr != "ZZZ":
        move = path[idx]
        idx = (idx + 1) % len(path)
        curr = graph[curr][move]
        cnt += 1

    print(cnt)


def part2(data):
    path = data[0]
    n = len(data)
    graph = {}

    start_nodes = []

    for i in range(2, n):
        line = data[i]
        node, adj = line.split(" = ")
        left, right = adj[1:-1].split(", ")
        graph[node] = {"L": left, "R": right}

        if node[-1] == "A":
            start_nodes.append(node)

    # time taken to reach first end node -> offsets
    offsets = []
    p = len(path)

    for start_node in start_nodes:
        idx = 0
        cnt = 0

        while start_node[-1] != "Z":
            move = path[idx]
            start_node = graph[start_node][move]
            idx = (idx + 1) % p
            cnt += 1

        offsets.append(cnt)

    # this shouldn't have worked but input is constructed in that way apparently
    res = math.lcm(*offsets)
    print(res)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
