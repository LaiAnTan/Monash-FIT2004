from math import floor, log10

def digits(n):
	if n < 0:
		n = abs(n)
	return int(log10(n)) + 1 if n > 0 else 1

def split_num(n, r_digits):
	right = 0
	for i in range(r_digits):

		right += (n % 10) * (10 ** i)
		n //= 10
	left = n
	return left, right

def karatsuba(n1, n2):

	"""
	Divide and conquer multiplication algorithm.

	:approach:

	The formula for Karatsuba's multiplication algorithm is constructed as follows:

	n1 * n2 = ((l1 * 10 ^ (n / 2)) + r1) * ((l2 * 10 ^ (n / 2)) + r2)
			= (l1 * l2 * 10 ^ n) + (l1 * r2 * 10 ^ (n / 2)) + (l2 * r1 * 10 ^ (n / 2)) + (r1 + r2)
			= (l1 * l2 * 10 ^ n) + (((l1 * r2) + (l2 * r1)) * 10 ^ (n / 2)) + (r1 + r2)

	Simplify to use only 3 multiplications instead of 4.

	By Gauss' method of multiplying complex numbers, notice that
	(((l1 * r2) + (l2 * r1)) * 10 ^ (n / 2))
	can be calculated with 3 multiplications, 2 of which we have already calculated.

	let c = (l1 * r2) + (r1 * l2)

	(l1 + r1)(l2 + r2)	= (l1 * l2) + (l1 * r2) + (r1 * l2) + (r1 * r2)
						= c + (l1 * l2) + (r1 * r2)

	c = (l1 * r2) + (r1 * l2) - (l1 * l2) - (r1 * r2)
	c = (l1 + r1 * l2 + r2) - (l1 * l2) - (r1 * r2)
	
	let m1 = l1 * l2, m2 = r1 * r2, m3 = (l1 + r1 * l2 + r2)
	
	Therefore,
	n1 * n2 = (m1 * 10 ^ n) + ((m3 - m2 - m1) * 10 ^ (n / 2)) + m2

	Which only requires 3 multiplications of 2 different numbers instead of 4.

	:time complexity: O(n ^ 1.59)
	"""

	if n1 < 10 or n2 < 10:
		return n1 * n2
	
	# max between the number of digits of n1 and n2
	# if one of the numbers has less digits, it will be left-padded with zeroes
	# eg: 123 * 5 -> 123 * 005
	n_digits = max(digits(n1), digits(n2))

	# we divide by 2 and floor it to represent the number of places the
	# significant halves (l1, l2) need to be shifted by
	half_n_digits = floor(n_digits / 2)

	l1, r1 = split_num(n1, half_n_digits)
	l2, r2 = split_num(n2, half_n_digits)

	mul1 = karatsuba(l1, l2)
	mul2 = karatsuba(r1, r2)
	mul3 = karatsuba(l1 + r1, l2 + r2)

	return (mul1 * 10 ** (half_n_digits * 2)) + \
		((mul3 - mul2 - mul1) * 10 ** half_n_digits) + mul2