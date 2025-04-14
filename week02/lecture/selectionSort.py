
def selectionSort(arr: list, key=lambda x: x) -> list:
	"""
	O(n^2)
	"""

	for i in range(len(arr) - 1):
		j = i + 1
		if key(arr[i]) < key(arr[j]):
			continue

		for s in range(j, len(arr)):
			if key(arr[s]) < key(arr[j]):
				j = s

		arr[i], arr[j] = arr[j], arr[i]
	
	return arr

if __name__ == "__main__":
	
	arr = [5, 2, 4, 3, 1, 6, 10, 8, 7, 9]
	arr2 = ["aaaa", "aaa", "a", "aaaaaa", "bbbb"]

	print(selectionSort(arr))
	print(selectionSort(arr2, key=lambda x: len(x)))