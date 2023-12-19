
def part1(data):
    path = data[0]
    
    n = len(data)
    graph = {}

    for i in range(2, n):
        line = data[i]
        node, adj = line.split(' = ')
        left, right = adj[1:-1].split(', ')
        graph[node] = {'L': left, 'R': right}

    curr = 'AAA'
    idx = 0
    cnt = 0
    
    while (curr != 'ZZZ'):
        move = path[idx]
        idx = (idx + 1) % len(path)
        curr = graph[curr][move]
        cnt += 1
    
    print(cnt)


def part2(data):
    pass


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)