import collections
import functools

cards1 = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cards2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

card_powers1 = {c: i for i, c in enumerate(reversed(cards1))}
card_powers2 = {c: i for i, c in enumerate(reversed(cards2))}

hand_powers = {
    (5,): 6,  # five of a kind
    (4, 1): 5,  # four of a kind
    (3, 2): 4,  # full house
    (3, 1, 1): 3,  # three of a kind
    (2, 2, 1): 2,  # two pair
    (2, 1, 1, 1): 1,  # one pair
    (1, 1, 1, 1, 1): 0,  # high card
}


def get_max_power(hand):
    if "J" not in hand:
        hand_type = tuple(
            sorted(list(collections.Counter(hand).values()), reverse=True)
        )
        pow = hand_powers[hand_type]
        return pow
    else:
        j_cnt = hand.count("J")

        hand = list(filter(lambda x: x != "J", list(hand)))
        hand = "".join(hand)

        if hand == "":
            counts = [
                5,
            ]
        else:
            counts = sorted(list(collections.Counter(hand).values()), reverse=True)
            counts[0] += j_cnt

        return hand_powers[tuple(counts)]


def comparator1(hand1, hand2):
    hand1_type = tuple(sorted(list(collections.Counter(hand1).values()), reverse=True))
    pow1 = hand_powers[hand1_type]

    hand2_type = tuple(sorted(list(collections.Counter(hand2).values()), reverse=True))
    pow2 = hand_powers[hand2_type]

    if pow1 > pow2:
        return 1
    elif pow1 < pow2:
        return -1
    else:
        for c1, c2 in zip(hand1, hand2):
            if card_powers1[c1] > card_powers1[c2]:
                return 1
            elif card_powers1[c1] < card_powers1[c2]:
                return -1
            else:
                continue


def comparator2(hand1, hand2):
    pow1 = get_max_power(hand1)
    pow2 = get_max_power(hand2)

    if pow1 > pow2:
        return 1
    elif pow1 < pow2:
        return -1
    else:
        for c1, c2 in zip(hand1, hand2):
            if card_powers2[c1] > card_powers2[c2]:
                return 1
            elif card_powers2[c1] < card_powers2[c2]:
                return -1
            else:
                continue


def part1(data):
    bids = {}
    hands = []
    for line in data:
        hand, bet = line.split()
        bids[hand] = int(bet)
        hands.append(hand)

    sorted_hands = sorted(hands, key=functools.cmp_to_key(comparator1))

    total = 0
    for i, hand in enumerate(sorted_hands):
        total += (i + 1) * bids[hand]

    print(total)


def part2(data):
    bids = {}
    hands = []
    for line in data:
        hand, bet = line.split()
        bids[hand] = int(bet)
        hands.append(hand)

    sorted_hands = sorted(hands, key=functools.cmp_to_key(comparator2))

    total = 0
    for i, hand in enumerate(sorted_hands):
        total += (i + 1) * bids[hand]

    print(total)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
