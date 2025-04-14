


def removeDuplicates(list: list[int]):

	# assume this performs an O(n log n) in-place sorting
	s = sorted(list)

	i = 1
	j = len(list) - 1
	
	while i < j:

		if s[i - 1] == s[i]:
			s[i - 1], s[j] = s[j], s[i - 1]
			j -= 1

		i += 1

	return s[:i]





if __name__ == "__main__":

	list = [1, 2, 3, 5, 4, 2, 1, 3, 5, 6, 9]

	print(removeDuplicates(list))


