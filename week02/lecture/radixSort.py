import math

def countingSort(arr: list[int], key: lambda x: x):
	pass

def radixSort(arr: list[int]):

	m = max(arr)
	max_bits = (math.log(m) / math.log(2)) + 1

	for shift in range(0, max_bits):

		arr = insertionSort()

		lsb = (lsb >> shift) & 1

	return arr

if __name__ == "__main__":
	pass
