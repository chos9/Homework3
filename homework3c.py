#! /usr/bin/env python
#
#  Seongjin Cho (Josh)
#  Student Number: 1130690
#  Math 480A
#  Homework 3, number 4
#

def det(a):
	"""
	Calculate determinant of the matrix
	"""
	b = lu(a)
	c = b[0]
	d = b[1]
	det = 1
	for i in range(len(c)):
		for j in range(len(c)):
			if i == j:
				det *= c[i][i]
	return det
	
def matrixMul(a, b):
	tb = zip(*b)
	return [[sum(c*d for c,d in zip(i,j)) for j in tb] for i in a]
   
def pivot(m):
	"""Creates the pivoting matrix for m."""
	n = len(m)
	i = [[float(i == j) for i in xrange(n)] for j in xrange(n)]
	for j in xrange(n):
		for k in range()
		row = max(xrange(j, n), key=lambda i: m[i][j])
		if j != row:
			i[j], i[row] = i[row], i[j]
	return i

def lu(a):
	"""Decomposes a nxn matrix A by PA=LU and returns L, U and P."""
	n = len(a)
	l = [[0.0] * n for i in xrange(n)]
	u = [[0.0] * n for i in xrange(n)]
	p = pivot(a)
	a2 = matrixMul(p, a)
	for j in xrange(n):
		l[j][j] = 1.0
		for i in xrange(j+1):
			s1 = sum(u[k][j] * l[i][k] for k in xrange(i))
			u[i][j] = a2[i][j] - s1
		for i in xrange(j, n):
			s2 = sum(u[k][j] * l[i][k] for k in xrange(j))
			l[i][j] = (a2[i][j] - s2) / u[j][j]
	return (u, p)
