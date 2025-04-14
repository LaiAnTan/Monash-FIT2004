class Item:

	def __init__(self, weight, value):
		self.weight = weight
		self.value = value

def unboundedKnapsack(capacity: int, items: list[Item]):

	memo = [0] * (capacity + 1)
	memo[0] = 0

	for i in range(1, capacity + 1):

		for item in items:

			if i - item.weight < 0:
				continue
		
			memo[i] = max(memo[i], item.value + memo[i - item.weight])

	print(memo)

	return memo[capacity]

if __name__ == "__main__":

	print(unboundedKnapsack(15, [
		Item(2, 120),
		Item(3, 200),
		Item(5, 250),
		Item(7, 450),
		Item(10, 750)
	]))