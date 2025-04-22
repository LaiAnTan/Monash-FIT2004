
def naiveCountInversions(arr: list[int]):
	"""
	The number of pairs of indices (i, j) s.t. i < j and V[i] > V[j]
	
	The time complexity for exhaustive search is O(n^2), as we check every
	possible combination of two numbers.
	"""

	inversions: list[tuple] = []

	for i in range(len(arr)):
		for j in range(len(arr)):
			if i < j and arr[i] > arr[j]:
				inversions.append((i, j))

	return len(inversions)

def merge(left: list, right: list, inversions: int) -> list:
	
	merged = []

	left_idx = 0
	right_idx = 0
	
	while left_idx != len(left) and right_idx != len(right):
		
		if left[left_idx] < right[right_idx]:
			merged.append(left[left_idx])
			left_idx += 1
		else:
			merged.append(right[right_idx])
			right_idx += 1
			inversions += 1
	
	for i in range(left_idx, len(left)):
		merged.append(left[i])
		
	for j in range(right_idx, len(right)):
		merged.append(right[j])

	return merged, inversions

def mergeSort(arr: list, inversions: int) -> list:
	"""
	The space complexity of this mergesort is not optimal, but that does not
	matter here
	"""
	
	if len(arr) <= 1:
		return arr, 0
	
	mid = len(arr) // 2
	
	left, i1 = mergeSort(arr[0:mid], inversions)
	right, i2 = mergeSort(arr[mid:len(arr)], inversions)
	
	return merge(left, right, i1 + i2)

def countInversions(arr: list[int]):
	"""
	Notice that the number of inversions =
	the number of 2-number swaps required to sort a list.

	We can use the fact that it is possible to count the number of 
	2-number swaps in O(n), by way of merge(left, right).
	This results the total time complexity being O(n log n), which is the same
	as mergesort.
	"""
	_, i = mergeSort(arr, 0)
	return i

if __name__ == "__main__":

	a1 = [2, 1, 5, 3, 4, 8, 6, 7]

	print(naiveCountInversions(a1))
	print(countInversions(a1))