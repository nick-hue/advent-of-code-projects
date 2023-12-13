from enum import Enum
from collections import defaultdict
import functools

class HandType(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1
    ERROR = -1

def get_hand_type(hand):
    chars = defaultdict(int)
    for char in hand:
        chars[char] += 1

    values = list(chars.values())
    if 5 in values:
        hand_type = HandType.FIVE_OF_A_KIND
    elif 4 in values:
        hand_type = HandType.FOUR_OF_A_KIND
    elif 3 in values and 2 in values:
        hand_type = HandType.FULL_HOUSE
    elif 3 in values:
        hand_type = HandType.THREE_OF_A_KIND
    elif values.count(2) == 2:
        hand_type = HandType.TWO_PAIR
    elif 2 in values:
        hand_type = HandType.ONE_PAIR
    else:
        hand_type = HandType.HIGH_CARD

    return hand_type

def split_deck(deck):
    result_deck = defaultdict(list)

    for hand in deck:
        result_deck[hand['type']].append(hand)

    return result_deck

def get_rankings(deck):
    splitted_deck = split_deck(deck)

    print(splitted_deck)

    sorted_by_cards = []
    for hand_type in splitted_deck.keys():
        sorted_hand_type = sorted(splitted_deck[hand_type], key=functools.cmp_to_key(compare))


        for item in sorted_hand_type:
            sorted_by_cards.append(item)

    for ranking, card in enumerate(sorted_by_cards):
        card['ranking'] = ranking+1
    return sorted_by_cards

def compare(hand1, hand2):
    for char1, char2 in zip(hand1['hand'], hand2['hand']):
        if POWER_DICT[char1] > POWER_DICT[char2]:
            return 1
        elif POWER_DICT[char1] < POWER_DICT[char2]:
            return -1
        else:
            continue
    return 0

with open("input.txt") as f:
    data = [item.strip("\n") for item in f.readlines()]

POWER_DICT = {
     'A':13,    'K':12,    'Q':11,    'J':10,    'T':9,    '9':8,    '8':7,    '7':6,    '6':5,    '5':4,    '4':3,    '3':2,    '2':1, 'J':0
    }

deck_info = []
for line in data:
    hand, bid = line.split(" ")
    print(f"Hand: {hand} | Bid: {bid}")

    current_type = get_hand_type(hand)

    results_dict = {
        'hand':hand,
        'bid':int(bid),
        'type':current_type,
        'ranking':0
    }
    deck_info.append(results_dict)

sorted_deck = sorted(deck_info, key=lambda x: x['type'].value)


deck_with_rankings = get_rankings(sorted_deck)

print(f"Sorted Cards: {deck_with_rankings}")
total = 0
for card in deck_with_rankings:
    total+=card['ranking']*card['bid']

print(total)

