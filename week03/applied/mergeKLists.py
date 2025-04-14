import heapq

def mergeKLists(lists: list[list[int]]):
	
	"""
	k lists of size n
	"""
	result = []
	
	minheap = [(lst[0], lst) for lst in lists]

	heapq.heapify(minheap)

	while minheap:
		_, minlist = heapq.heappop(minheap)

		result.append(minlist[0])
		minlist = minlist[1:]

		if (len(minlist) > 0):
			heapq.heappush(minheap, (minlist[0], minlist))

	return result


if __name__ == "__main__":

	lists = [
		[1, 5, 8],
		[2, 3, 9],
		[4, 6, 7]
	]

	print(mergeKLists(lists))

