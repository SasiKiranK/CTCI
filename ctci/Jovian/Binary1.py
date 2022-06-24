def locate_cards2(cards, query):
    # Leniar search
    # if cards is empty list
    if len(cards) == 0:
        # print('s')
        return -1

    # create variable with position 0
    positio = 0
    while True:

        if cards[positio] == query:
            return positio

        # increment the possition
        positio += 1

        # if query not found in the cards
        if positio == len(cards):
            return -1


def locate_cards_linear(cards, query):
    # Leniar search
    # create variable with position 0
    positio = 0
    while positio < len(cards):

        if cards[positio] == query:
            return positio

        # increment the possition
        positio += 1

        # if query not found in the cards
        if positio == len(cards):
            return -1
    return -1


def locate_cards(cards, query):
    # storing starting and ending of card size
    low, high = 0, len(cards) - 1

    # till check if low and high matches
    while low <= high:
        # finding the middle of cards
        mid = (low + high) // 2
        mid_card = cards[mid]
        print(cards, query, low, high, mid, cards[mid])
        result = test_positions(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'right':
            low = mid + 1
        elif result == 'left':
            high = mid - 1

    # if not found
    return -1


def test_positions(cards, query, mid):
    if cards[mid] == query and cards[mid - 1] != query:
        return 'found'
    elif cards[mid] > query:
        return 'right'
    else:
        return 'left'


tests = []
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}
)
tests.append({
    'input': {
        'cards': [33, 11, 10, 7, 4, 3, 1, 0],
        'query': 33
    },
    'output': 0
}
)

tests.append({
    'input': {
        'cards': [15, 11, 10, 7, 4, 3, 1, 0],
        'query': 0
    },
    'output': 7
}
)

tests.append({
    'input': {
        'cards': [22, 11, 10, 7, 4, 3, 1, 0],
        'query': 8
    },
    'output': -1
}
)

tests.append({
    'input': {
        'cards': [22, 11, 10, 7, 7, 7, 7, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}
)

tests.append({
    'input': {
        'cards': [7, 7, 7, 7, 7, 7, 7, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 0
}
)

tests.append({
    'input': {
        'cards': '',
        'query': 2
    },
    'output': -1
}
)

for test in tests:
    print(locate_cards(**test['input']) == test['output'])
