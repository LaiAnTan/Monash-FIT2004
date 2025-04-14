
import heapq

def minKElements(list: list[int], k: int):

	heapq.heapify(list)

	minK = []

	for _ in range(k):
		minK.append(heapq.heappop(list))
	
	return (minK)

if __name__ == "__main__":

	list = [1]

	print(minKElements(list, 1))

	list += [5, 4, 3, 2]

	print(minKElements(list, 3))
