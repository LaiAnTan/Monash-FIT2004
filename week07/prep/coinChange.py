from math import inf

def coinChangeBottomUp(target: int, coins: list[int]):

	memo = [inf] * (target + 1)
	memo[0] = 0

	decision = [-1] * (target + 1)
	decision[0] = None

	for i in range(1, target + 1):

		for coin in coins:

			if i - coin < 0:
				continue

			c = 1 + memo[i - coin]

			if c < memo[i]:
				memo[i] = c
				decision[i] = coin

	if memo[target] == inf:
		return -1, []

	# backtrack decision array
	used = []
	i = target
	while i > 0:
		used.append(decision[i])
		i -= decision[i]

	return memo[target], used

def coinChangeTopDownAux(target: int, coins: list[int],
	memo: list[int], decision: list[int]):

	if memo[target] != inf:
		return memo[target]
	
	for coin in coins:

		if target - coin < 0:
			continue
		
		c = 1 + coinChangeTopDownAux(target - coin, coins, memo, decision)
		if c < memo[target]:
			memo[target] = c
			decision[target] = coin
	
	return memo[target]

def coinChangeTopDown(target: int, coins: list[int]):

	memo = [inf] * (target + 1)
	memo[0] = 0

	decision = [-1] * (target + 1)
	decision[0] = None

	coinChangeTopDownAux(target, coins, memo, decision)

	# backtrack decision array
	used = []
	i = target
	while i > 0:
		used.append(decision[i])
		i -= decision[i]

	return memo[target], used



if __name__ == "__main__":

	print(coinChangeBottomUp(12, [1, 5, 6, 9]))
	print(coinChangeTopDown(12, [1, 5, 6, 9]))

	print(coinChangeBottomUp(3, [2]))