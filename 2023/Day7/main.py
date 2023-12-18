from collections import Counter
from functools import cmp_to_key


def comparator(hand1, hand2):
    hand1_type = tuple(sorted(list(Counter(hand1).values()), reverse=True))
    pow1 = hand_powers[hand1_type]

    hand2_type = tuple(sorted(list(Counter(hand2).values()), reverse=True))
    pow2 = hand_powers[hand2_type]

    if pow1 > pow2:
        return 1
    elif pow1 < pow2:
        return -1
    else:
        for c1, c2 in zip(hand1, hand2):
            if card_powers[c1] > card_powers[c2]:
                return 1
            elif card_powers[c1] < card_powers[c2]:
                return -1
            else:
                continue


def part1(data):
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
    card_powers = {c: i for i, c in enumerate(reversed(cards))}
    hand_powers = {
        (5,): 6,  # five of a kind
        (4, 1): 5,  # four of a kind
        (3, 2): 4,  # full house
        (3, 1, 1): 3,  # three of a kind
        (2, 2, 1): 2,  # two pair
        (2, 1, 1, 1): 1,  # one pair
        (1, 1, 1, 1, 1): 0,  # high card
    }

    bids = {}
    hands = []
    for line in data:
        hand, bet = line.split()
        bids[hand] = int(bet)
        hands.append(hand)

    sorted_hands = sorted(hands, key=cmp_to_key(comparator))

    total = 0
    for i, hand in enumerate(sorted_hands):
        total += (i + 1) * bids[hand]

    print(total)


def part2(data):
    pass


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
