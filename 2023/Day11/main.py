from bisect import bisect_left, bisect_right

def part1(data: list[list[str]]):

    for i, line in enumerate(data):
        data[i] = list(line)

    empty_rows = []
    for i, row in enumerate(data):
        if row.count("#") == 0:
            empty_rows.append(i)

    empty_columns = []
    cols = len(data[0])
    for j in range(cols):
        for row in data:
            if row[j] == "#":
                break
        else:
            empty_columns.append(j)

    empty_row = ["." for _ in range(cols)]
    for i, row_no in enumerate(empty_rows):
        data.insert(i + row_no, empty_row)

    for j, col_no in enumerate(empty_columns):
        for row in data:
            row.insert(j + col_no, ".")

    nodes = []
    n = len(data)
    m = len(data[0])

    for x in range(n):
        for y in range(m):
            if data[x][y] == '#':
                nodes.append((x, y))

    total = 0
    k = len(nodes)
    for i in range(k):
        for j in range(i+1, k):
            total += abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1])

    print(total)


def part2(data):
    empty_rows = []
    for i, row in enumerate(data):
        if row.count("#") == 0:
            empty_rows.append(i)

    empty_columns = []
    cols = len(data[0])
    for j in range(cols):
        for row in data:
            if row[j] == "#":
                break
        else:
            empty_columns.append(j)

    n = len(data)
    m = len(data[0])
    nodes = []
    
    for x in range(n):
        for y in range(m):
            if data[x][y] == "#":
                nodes.append((x, y))

    k = len(nodes)
    multiplier = 1000000 - 1
    total = 0

    for i in range(k):
        for j in range(i+1, k):
            x1, y1 = nodes[i]
            x2, y2 = nodes[j]

            top_idx = bisect_left(empty_rows, min(x1, x2))
            bottom_idx = bisect_right(empty_rows, max(x1, x2))

            left_idx = bisect_left(empty_columns, min(y1, y2))
            right_idx = bisect_right(empty_columns, max(y1, y2))

            total += abs(x1 - x2) + abs(y1 - y2)
            total += multiplier * (bottom_idx - top_idx)
            total += multiplier * (right_idx - left_idx)


    print(total)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
