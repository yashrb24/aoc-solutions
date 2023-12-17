import math


def part1(data):
    T = list(map(int, data[0].split()[1:]))
    X = list(map(int, data[1].split()[1:]))

    prod = 1
    for t, x in zip(T, X):
        left = (t - (t**2 - 4 * x) ** 0.5) / 2
        if int(left) == left:
            left += 1
        else:
            left = math.ceil(left)

        right = (t + (t**2 - 4 * x) ** 0.5) / 2
        if int(right) == right:
            right -= 1
        else:
            right = math.floor(right)

        prod *= right - left + 1

    print(prod)


def part2(data):
    t = int("".join(data[0].split()[1:]))
    x = int("".join(data[1].split()[1:]))

    left = (t - (t**2 - 4 * x) ** 0.5) / 2
    if int(left) == left:
        left += 1
    else:
        left = math.ceil(left)

    right = (t + (t**2 - 4 * x) ** 0.5) / 2
    if int(right) == right:
        right -= 1
    else:
        right = math.floor(right)

    print(right - left + 1)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
