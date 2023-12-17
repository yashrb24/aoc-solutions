from pprint import pprint as print


def part1(data):
    total = 0
    for game in data:
        _, numbers = game.split(": ")
        winning, current = numbers.split(" | ")

        winning = set(map(int, winning.split()))
        current = set(map(int, current.split()))

        common = len(winning.intersection(current))

        if common != 0:
            total += 1 << (common - 1)

    print(total)


def part2(data):
    n = len(data)
    copies = {i: 0 for i in range(n)}

    for i, game in enumerate(data):
        _, numbers = game.split(": ")
        winning, current = numbers.split(" | ")

        winning = set(map(int, winning.split()))
        current = set(map(int, current.split()))

        common = len(winning.intersection(current))

        for j in range(i + 1, min(i + 1 + common, len(data))):
            copies[j] += 1 + copies[i]

    total = n

    for v in copies.values():
        total += v

    print(total)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    # part1(data)
    part2(data)
