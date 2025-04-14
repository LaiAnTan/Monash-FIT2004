"""
For simplicity,
We define a key and a lock to be integers.

A key and a lock 'match' if they are equal.

When we 'try' a key with a lock, we compare them for equality.
"""

from random import randint

def tryKeyWithLock(key: int, lock: int) -> int:

	if (key < lock):
		return (-1)
	if (key > lock):
		return (1)

	return (0)


def keyLockMatchingAux(keys: list[int], locks: list[int], size: int, pairs: list[tuple[int, int]]):

	"""
	Average time complexity: O(n log n)
	"""

	def partition(list: list[int], pivot: int):
		
		"""
		Out of place partitioning because i dont care about auxiliary space
		right now

		Time complexity: O(n)
		"""

		left_items = []
		right_items = []

		for item in list:
			
			if tryKeyWithLock(item, pivot) == -1:
				left_items.append(item)
			elif tryKeyWithLock(item, pivot) == 1:
				right_items.append(item)

		print(f"Partitioned: {left_items}, {right_items}")

		return left_items, right_items

	if (size == 0):
		return

	pivot_idx = randint(0, size - 1)
	pivot_value = keys[pivot_idx]

	# partition the keys based on the lock picked as pivot
	left_keys, right_keys = partition(keys, pivot_value)
	# partition the locks based on the key paired with the lock, which is now in position
	left_locks, right_locks = partition(locks, pivot_value)

	# the key lock pair we picked as pivot is matched
	pairs.append((pivot_value, pivot_value))

	if (len(left_keys) >= 1):
		keyLockMatchingAux(left_keys, left_locks, len(left_keys), pairs)
	if (len(right_keys) >= 1):
		keyLockMatchingAux(right_keys, right_locks, len(right_keys), pairs)

def keyLockMatching(keys: list[int], locks: list[int]) -> list[tuple[int, int]]:

	"""
	Prerequisites:

	Each key only matches one lock and vice versa.

	We will not compare keys with keys or locks with locks.
	"""
	pairs = []
	keyLockMatchingAux(keys, locks, len(keys), pairs)
	return (pairs)

if __name__ == "__main__":

	keys = [5, 2, 3, 1, 4, 6]
	locks = [1, 4, 2, 3, 5, 6]

	print(keyLockMatching(keys, locks))
	