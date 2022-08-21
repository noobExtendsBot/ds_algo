"""
Binary Search implementation for first and last occurance of an element,
when in descending order
"""


def binary_search_first(cards, query):
    # Arr is in descending order
    # using linear search
    # for index, item in enumerate(cards):
    # 	if query == item:
    # 		return index
    # return -1

    # Binary Search with first occurance
    start, end, result = 0, len(cards) - 1, -1
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == query:
            result = mid
            # make the array short to check for first occurance
            end = mid - 1
        elif cards[mid] > query:
            start = mid + 1
        else:
            end = mid - 1
    return result


def binary_search_last(cards, query):
    # Arr is in descending order
    # Binary Search with last occurance
    start, end, result = 0, len(cards) - 1, -1
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == query:
            result = mid
            # make the array short to check for first occurance
            start = mid + 1
        elif cards[mid] > query:
            start = mid + 1
        else:
            end = mid - 1
    return result


tests_first_index = [
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
    {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
    {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
    {'input': {'cards': [6], 'query': 6}, 'output': 0},
    {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
    {'input': {'cards': [], 'query': 7}, 'output': -1},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 2}
]

tests_last_index = [
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
    {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
    {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
    {'input': {'cards': [6], 'query': 6}, 'output': 0},
    {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
    {'input': {'cards': [], 'query': 7}, 'output': -1},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 7}
]

for test in tests_first_index:
    result = binary_search_first(**test['input'])
    print(result, test['output'])
    assert result == test['output']

print("""Test for last index starting!!!""")

for test in tests_last_index:
    result = binary_search_last(**test['input'])
    print(result, test['output'])
    assert result == test['output']
