


def longestIncreasingSubsequence(seq: list[int], memo):

	for i in range(0, len(seq)):
		for j in range(0, len(seq)):
			if seq[j] < seq[i]:
				memo[i] = max(memo[i], 1 + memo[j])
	
	print(memo)

	return max(memo)

def longestIncreasingSubsequence2(seq: list[int], memo):

	pass

	


if __name__ == "__main__":

	seq = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
	
	memo = [0] * (len(seq) + 1)

	memo[0] = 1
	
	print(longestIncreasingSubsequence(seq, memo))
