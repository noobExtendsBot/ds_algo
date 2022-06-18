"""
basic Binary Search implementation
"""


def binary_search(cards, query):
    # descending order
    # using linear search
    # for index, item in enumerate(cards):
    # 	if query == item:
    # 		return index
    # return -1

    # now optimise the solution [Binary Search without first or last occurance]
    start, end = 0, len(cards) - 1
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            end = mid - 1
        else:
            start = mid + 1
    return -1


tests = [
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
    {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
    {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
    {'input': {'cards': [6], 'query': 6}, 'output': 0},
    {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
    {'input': {'cards': [], 'query': 7}, 'output': -1},
]

for test in tests:
    result = binary_search(**test['input'])
    print(result, test['output'])
    assert result == test['output']
