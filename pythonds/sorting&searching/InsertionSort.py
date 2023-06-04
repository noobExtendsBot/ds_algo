"""
Insertion Sort Algorithm: The Idea is that left side of the array will always be sorted. 
So, compare new element with each element of the left side of the list and insert it at its correct position. 
"""




def insertion_sort():
	arr = [89,12,43,12,0,1]
	for i, _ in enumerate(arr):
		j = i
		while j > 0 and arr[j-1] > arr[j]:
			arr[j-1], arr[j] = arr[j], arr[j-1]
			j -= 1
	return arr
	
if __name__ == "__main__":
	print(insertion_sort())