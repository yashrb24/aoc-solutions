from functools import cache


@cache
def dp(string_index, group_index, string, group):
    # base case
    if string_index == len(string):
        return group_index == len(group)
    
    if group_index == len(group):
        return "#" not in string[string_index:]

    # recursive case
    if string[string_index] == ".":
        return dp(string_index + 1, group_index, string, group)

    if string[string_index] == "#":
        for _ in range(group[group_index]):
            if string_index == len(string) or string[string_index] not in ["#", "?"]:
                return 0

            string_index += 1

        if string_index == len(string) or string[string_index] != "#":
            return dp(string_index + 1, group_index + 1, string, group)
        else:
            return 0

    if string[string_index] == "?":
        cnt = 0

        cnt += dp(string_index + 1, group_index, string, group)

        found = False
        for _ in range(group[group_index]):
            if string_index == len(string) or string[string_index] == ".":
                found = True
                break
            string_index += 1

        if not found:
            if string_index == len(string) or string[string_index] != "#":
                cnt += dp(string_index + 1, group_index + 1, string, group)

        return cnt


def part1(data):
    total = 0
    for line in data:
        cfg, runs = line.split()
        runs = tuple(map(int, runs.split(",")))
        cfg += ".."
        ans = dp(0, 0, cfg, runs)
        total += ans

    print(total)


def part2(data):
    pass


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
