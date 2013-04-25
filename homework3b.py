#! /usr/bin/env python
#
#  Seongjin Cho (Josh)
#  Student Number: 1130690
#  Math 480A
#  Homework 3, number 3
#

from math import sqrt

def prime_gen(n=10000):
	"""
	This is Prime number generator. It uses Sieve of Erastosthenes.
	ex) sage: prime_gen(100)
		[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
		 59, 61, 67, 71, 73, 79, 83, 89, 97]
	"""
	a = [1 for i in range(n+1)]
	for i in range(2,int(sqrt(n))+1):
		if a[i] == 1:
			for j in range(i**2,n+1,i):
				a[j] = 0
	return [i for i in range(2,n+1) if a[i] == 1]

