import bisect

def part1(data):
    grid = [*zip(*data)]
    total = 0

    for line in grid:
        available = []
        rocks = []
        fixed = [0]

        for i, c in enumerate(line):
            if c == ".":
                available.append(i+1)
            elif c == "#":
                fixed.append(i+1)
            elif c == "O":
                rocks.append(i+1)
            else:
                return None

        
        for rock in rocks:
            idx = bisect.bisect(fixed, rock) - 1
            fixed_idx = bisect.bisect(available, fixed[idx])

            if fixed_idx == len(available) or available[fixed_idx] > rock:
                total += len(grid[0]) - rock + 1
                continue
            else:
                total += len(grid[0]) - available[fixed_idx]  + 1
                res = available.pop(fixed_idx)
                bisect.insort(available, rock)
            
    print(total)
            
def part2(data):
    pass


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
