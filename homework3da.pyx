#! /usr/bin/env python
#
#  Seongjin Cho (Josh)
#  Student Number: 1130690
#  Math 480A
#  Homework 3, number 5
#

def multiply(a,b):
	"""	Multiply matrices """
	cdef int i, j, c, d
	tb = zip(*b)
	return [[sum(c*d for c,d in zip(i,j)) for j in tb] for i in a]
