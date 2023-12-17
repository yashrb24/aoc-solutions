def part1(data):
    total = 0

    allowed = {
        "red": 12, 
        "green": 13,
        "blue": 14
    }

    for line in data:
        game_id, game_results = line.strip("\n").split(": ")
        game_idx = int(game_id.split(" ")[1])

        valid = True
        
        results = game_results.split(";")
        for result in results:
            colour_results = result.split(", ")
            for colour_result in colour_results:
                num_colour, colour = colour_result.split()
                if int(num_colour) > allowed[colour]:
                    valid = False
                    break

        if valid:
            total += int(game_idx)

    print(total)

def part2(data):
    total = 0

    for line in data:
        _, game_results = line.strip('\n').split(": ")
        draws = {
            "red": [],
            "green": [],
            "blue":[]
        }

        results = game_results.split("; ")
        for result in results:
            colour_results = result.split(", ")
            for colour_result in colour_results:
                num_colour, colour = colour_result.split()
                draws[colour].append(int(num_colour))

        power = 1
        for vals in draws.values():
            power *= max(vals, default=1)

        total += power

    print(total)

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)