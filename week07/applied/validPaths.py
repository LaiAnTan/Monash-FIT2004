
from pprint import pprint

def numValidPaths(
	maze: list[list[int]],
	start: tuple[int, int],
	end: tuple[int, int],
	memo: list[list[int]]
	):

	if end[0] < 0 or end[0] >= len(maze) or \
			end[1] < 0 or end[1] >= len(maze[0]) or \
			maze[end[0]][end[1]] == 1:
		return 0

	if memo[end[0]][end[1]]:
		return memo[end[0]][end[1]]

	left = (end[0], end[1] - 1)
	bottom = (end[0] + 1, end[1])

	paths = numValidPaths(maze, start, left, memo) + \
		numValidPaths(maze, start, bottom, memo)

	if paths > memo[end[0]][end[1]]:
		memo[end[0]][end[1]] = paths

	return memo[end[0]][end[1]]

if __name__ == "__main__":

	grid = [
		[1, 1, 0, 0, 1, 1, 0],
		[1, 1, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 0],
		[0, 0, 0, 0, 1, 0, 0],
		[0, 1, 0, 0, 0, 0, 0],
		[0, 1, 1, 0, 0, 1, 1],
		[0, 0, 0, 0, 0, 1, 0]
	]

	memo = [
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 0, 0],
	]

	print(numValidPaths(grid, (6, 0), (0, 6), memo))
	pprint(memo)