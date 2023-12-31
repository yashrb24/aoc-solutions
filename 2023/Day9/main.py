def part1(data):
    total = 0

    for line in data:
        nums = list(map(int, line.split()))
        arrays = [nums]
        
        while True:
            new_array = [arrays[-1][i+1] - arrays[-1][i] for i in range(len(arrays[-1]) - 1)]
            arrays.append(new_array)
            if all([x == 0 for x in new_array]):
                break

        for i in range(len(arrays) - 1, 0, -1):
            arrays[i-1].append(arrays[i][-1] + arrays[i-1][-1])

        total += arrays[0][-1]
        
    print(total)


def part2(data):
    total = 0
    for line in data:
        nums = list(map(int, line.split()))
        arrays = [nums[::-1]]
        
        while True:
            new_array = [arrays[-1][i+1] - arrays[-1][i] for i in range(len(arrays[-1]) - 1)]
            arrays.append(new_array)
            if all([x == 0 for x in new_array]):
                break

        for i in range(len(arrays) - 1, 0, -1):
            arrays[i-1].append(arrays[i][-1] + arrays[i-1][-1])

        total += arrays[0][-1]
        
    print(total)

        


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)