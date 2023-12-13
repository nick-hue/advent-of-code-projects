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
        if char == "J":
            continue
        chars[char] += 1

    j_count = hand.count("J")
    
    keys = list(chars.keys())
    values = list(chars.values())
    card_count = sorted(values, reverse=True)
    print(f"Card count: {card_count}")
    print(f"Chars: {chars}")
    print(f"Keys: {keys}\nValues: {values}")
    
    if not card_count:
        return HandType.FIVE_OF_A_KIND

    if card_count[0] + j_count == 5:
        hand_type = HandType.FIVE_OF_A_KIND
    elif card_count[0] + j_count == 4:
        hand_type = HandType.FOUR_OF_A_KIND
    elif card_count[0] + j_count == 3 and card_count[1] == 2:     # O JUL; TP CLATACHRE
        hand_type = HandType.FULL_HOUSE
    elif card_count[0] + j_count == 3:
        hand_type = HandType.THREE_OF_A_KIND
    elif values.count(2) == 2 or (2 in values and j_count==1):
        hand_type = HandType.TWO_PAIR
    elif card_count[0] == 2 or j_count == 1:           
        hand_type = HandType.ONE_PAIR
    else:
        hand_type = HandType.HIGH_CARD
    print(f"Hand: {hand} is {hand_type}\n")

    return hand_type

def split_deck(deck):
    result_deck = defaultdict(list)

    for hand in deck:
        result_deck[hand['type']].append(hand)

    return result_deck

def get_rankings(deck):
    splitted_deck = split_deck(deck)

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
print(deck_with_rankings)

total = 0
for hand in deck_with_rankings:
    #print(f"{hand['hand']} has {hand['ranking']}")
    total += hand['ranking'] * hand['bid']

print(total)

