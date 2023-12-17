def part1(data):
    total = 0
    for line in data:
        digits = [el for el in line if el.isdigit()]
        if len(digits) == 1:
            digits.append(digits[0])
        total += int(digits[0]) * 10 + int(digits[-1])

    print(total)


def part2(data):
    total = 0

    names = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    numbers = list(names.keys())
    numbers.extend(names.values())

    for line in data:
        min_idx = float("inf")
        max_idx = -1
        min_var = None
        max_var = None

        for var in numbers:
            if var not in line:
                continue

            l_index = line.index(var)
            r_index = line.rindex(var)

            if r_index > max_idx:
                max_idx = r_index
                max_var = var if var.isdigit() else names[var]
            if l_index < min_idx:
                min_idx = l_index
                min_var = var if var.isdigit() else names[var]

        curr = int(min_var) * 10 + int(max_var)
        total += curr

    print(total)


if __name__ == "__main__":
    with open("input.txt") as input_file:
        data = input_file.readlines()

    part1(data)
    part2(data)


