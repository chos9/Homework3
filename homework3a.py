#! /usr/bin/env python
#
#  Seongjin Cho (Josh)
#  Student Number: 1130690
#  Math 480A
#

def sum(n):
	"""
	Compute the sum of the squares of the positive integers up to n
	ex) sage: sum(5)
		55
	"""
	try:
		if not isinstance(n, (int, long, Integer)):
			raise TypeError("n must be an integer")
		elif n < 0:
			raise ValueError("n must not be negative")
		else:
			return n*(n+1)*(2*n+1)/6
	except:
		raise

