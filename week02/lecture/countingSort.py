

def unstableCountingSort(arr: list[int], k: int):
	"""
	O(n + k), where n is the number of elements int the array,
	k is the size of the count array, i.e. the largest key in the input.
	
	"""
	
	counts = [0] * (k + 1)
	out = []

	for elem in arr:
		counts[elem] += 1

	for i, count in enumerate(counts):
		out += [i] * count

	return out


if __name__ == "__main__":

	arr = [5, 2, 4, 3, 1, 6, 10, 8, 7, 9]
	print(unstableCountingSort(arr, max(arr)))
