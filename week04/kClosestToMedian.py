
import random

def medianOfMedians(list):

	"""
	Returns the median of medians selected.
	"""

	partitions = []

	for i in range(0, len(list), 5):
		partitions.append(list[i:i+5])

	# because we are running quickSelect on lists of size 5,
	# this is not O(n^2)
	medians = [quickSelect(p, len(p) // 2) for p in partitions]

	return quickSelect(medians, len(medians) // 2)

def naivePartitioning(list: list[int], pivot: int):

	left = []
	right = []
	middle = []

	for elem in list:
		if elem < pivot:
			left.append(elem)
		elif elem > pivot:
			right.append(elem)
		else:
			middle.append(elem)
	
	return left + middle + right, len(left) + len(middle) // 2


def quickSelect(list: list[int], k: int) -> int:

	"""
	Once again i will be performing a shitty partitioning

	Returns the k-th smallest element in the list.
	"""
	
	# pivot = medianOfMedians(list)

	pivot = random.randint(0, len(list) - 1)
	partitioned, mid = naivePartitioning(list, pivot)

	print(partitioned, mid)

	if k < mid:
		return quickSelect(partitioned[0:mid], k)
	elif k > mid:
		return quickSelect(partitioned[mid+1:], k)
	else:
		return pivot



def kClosestToMedian(list: list[int], k: int) -> list[int]:

	median = quickSelect()

	abs_diff = [(elem, abs(elem - median)) for elem in list]

if __name__ == "__main__":

	l = [2, 5, 3, 4, 1, 5, 6, 7, 8, 9, 12, 11, 10, 6]

	print(quickSelect(l, len(l) // 2))

	# print(medianOfMedians([2, 5, 3, 4, 1, 5, 6, 7, 8, 9, 12, 11, 10, 6]))