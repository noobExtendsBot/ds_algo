"""
basic Binary Search implementation
"""
def find_card(cards, query):
	# linear search
	# for index, item in enumerate(cards):
	# 	if query == item:
	# 		return index
	# return -1

	# now optimise the solution
	start, end = 0, len(cards)-1
	while start<end:
		mid = (start+end)//2
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
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 2}
 ]
for test in tests:
	result = find_card(test['input']['cards'], test['input']['query'])
	assert result == test['output']