from collections import OrderedDict

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


def custom_hash(label):
    curr = 0
    for c in label:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr

def part2(data):
    boxes = {i: [] for i in range(5)}
    boxes_available = {i: set() for i in range(5)}
    boxes_label_last = {i : dict() for i in range(5)}

    strings = data[0].split(",")
    
    for string in strings:
        if "-" in string:
            label = string[:-1]
            box_value = custom_hash(label)
            if label in boxes_available[box_value]:
                boxes_available[box_value].remove(label)
                boxes_label_last[box_value].pop(label)

        else:
            label, focal_length = string.split("=")
            box_value = custom_hash(label)

            if label not in boxes_available[box_value]:
                boxes_available[box_value].add(label)

            boxes_label_last[box_value][label] = focal_length
            boxes[box_value].append((label, focal_length))

    # prune the entries not required
    final_boxes = {i: [] for i in range(5)}
    for box_idx, strings in boxes.items():
        for label, focal_length in strings:
            if label in boxes_available[box_idx] and focal_length == boxes_label_last[box_idx][label]:
                final_boxes[box_idx].append((label, focal_length))

    print(final_boxes)




if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)