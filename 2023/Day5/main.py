class Mapper:
    def __init__(self):
        self.src_to_length = {}
        self.src_to_dest = {}

    def add_range(self, dest, src, length):
        self.src_to_length[src] = length
        self.src_to_dest[src] = dest

    def lookup(self, num):
        for k, v in self.src_to_length.items():
            if k <= num < k + v:
                return self.src_to_dest[k] + (num - k)
        return num


def part1(data):
    data = list(filter(lambda x: x != "", data))
    _, nums = data[0].split(": ")
    seeds = list(map(int, nums.split()))

    n = len(data)
    mappers = []
    curr = Mapper()
    for i in range(2, n):
        if "map" in data[i]:
            mappers.append(curr)
            curr = Mapper()
        else:
            dest, src, length = map(int, data[i].split())
            curr.add_range(dest, src, length)

    mappers.append(curr)

    min_location = float("inf")
    for seed in seeds:
        curr = seed
        for mp in mappers:
            curr = mp.lookup(curr)
        min_location = min(curr, min_location)

    print(min_location)


def part2(data):
    data = list(filter(lambda x: x != "", data))
    _, nums = data[0].split(": ")
    seed_info = list(map(int, nums.split()))

    n = len(data)
    mappers = []  # list of inverse mapper objects
    inv_mappers = []

    curr = Mapper()
    inv_curr = Mapper()

    for i in range(2, n):
        if "map" in data[i]:
            mappers.append(curr)
            inv_mappers.append(inv_curr)
            curr = Mapper()
            inv_curr = Mapper()
        else:
            dest, src, length = map(int, data[i].split())
            curr.add_range(dest, src, length)
            inv_curr.add_range(src, dest, length)

    mappers.append(curr)
    inv_mappers.append(inv_curr)

    inv_mappers = inv_mappers[
        ::-1
    ]  # inverting the list from location -> humidity -> ... -> seed

    curr_endpoints, temp_endpoints = set(), set()
    curr_endpoints.add(0)
    curr_endpoints.add(float("inf"))

    for inv_mp, mp in zip(inv_mappers, reversed(mappers)):
        for k, v in mp.src_to_length.items():
            temp_endpoints.add(k)
            temp_endpoints.add(k + v - 1)

        temp_endpoints.add(max(min(temp_endpoints) - 1, 0))
        temp_endpoints.add(max(temp_endpoints) + 1)

        for curr_ep in curr_endpoints:
            temp_endpoints.add(inv_mp.lookup(curr_ep))

        curr_endpoints = temp_endpoints
        temp_endpoints = set()

    seeds = list(curr_endpoints)

    # find valid seeds
    m = len(seed_info)
    valid_seeds = []
    for seed in seeds:
        found = False
        for i in range(0, m, 2):
            seed_start = seed_info[i]
            seed_length = seed_info[i + 1]

            if seed_start <= seed < seed_start + seed_length:
                found = True
                break

        if found:
            valid_seeds.append(seed)

    location = float("inf")
    for seed in valid_seeds:
        curr = seed
        for mp in mappers:
            curr = mp.lookup(curr)

        location = min(location, curr)

    print(location)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
