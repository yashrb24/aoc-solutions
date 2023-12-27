from collections import OrderedDict

def custom_hash(label):
    curr = 0
    for c in label:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr


def part1(data):
    strings = data[0].split(",")
    total = sum(custom_hash(string) for string in strings)

    print(total)

def part2(data):
    boxes = {i: OrderedDict() for i in range(256)}
    boxes_available = {i: set() for i in range(256)}

    strings = data[0].split(",")

    for string in strings:

        if "-" in string:
            label = string[:-1]
            box_value = custom_hash(label)
            if label in boxes_available[box_value]:
                boxes_available[box_value].remove(label)
                boxes[box_value].pop(label)
        
        else:
            label, focal_length = string.split("=")
            box_value = custom_hash(label)

            boxes_available[box_value].add(label)
            boxes[box_value][label] = focal_length

    total = 0
    for box_idx, box in boxes.items():
        for i, focal_length in enumerate(box.values(), start=1):
            total += int(focal_length) * i * (box_idx + 1)

    print(total)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
