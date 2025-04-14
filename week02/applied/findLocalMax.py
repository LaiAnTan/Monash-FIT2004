
def is_local_max(x: int, y: int, matrix: list[list[int]]):
	"""
	O(n)
	"""
	
	left = matrix[y][x - 1] if x - 1 >= 0 else None
	right = matrix[y][x + 1] if x + 1 < len(matrix[0]) else None
	up = matrix[y - 1][x] if y - 1 >= 0 else None
	down = matrix[y + 1][x] if y + 1 < len(matrix) else None

	for adj in [left, right, up, down]:
		if adj is None:
			continue
		if matrix[y][x] <= adj:
			return False
	
	return True

def naive_find_local_max(matrix: list[list[int]]):

	for y in range(len(matrix)):
		for x in range(len(matrix[0])):
			if is_local_max(x, y, matrix):
				print(f"Local maximum {matrix[y][x]} found at {x}, {y}")
				return x, y
	
	return None, None

def find_local_max_2(matrix: list[list[int]]):
	pass

def find_local_max_3(matrix: list[list[int]]):
	pass

if __name__ == "__main__":

	matrix = [
		[1, 2, 27, 28, 29, 30, 49],
		[3, 4, 25, 26, 31, 32, 48],
		[5, 6, 23, 24, 33, 34, 47],
		[7, 8, 21, 22, 35, 36, 46],
		[9, 10, 19, 20, 37, 38, 45],
		[11, 12, 17, 18, 39, 40, 44],
		[13, 14, 15, 16, 41, 42, 43]
	]

	print(naive_find_local_max(matrix))