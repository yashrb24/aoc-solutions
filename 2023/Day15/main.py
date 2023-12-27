def part1(data):
    strings = data[0].split(",")
    total = 0
    
    for string in strings:
        curr = 0
        for c in string:
            curr += ord(c)
            curr *= 17
            curr %= 256
        total += curr

    print(total)


def part2(data):
    pass


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)