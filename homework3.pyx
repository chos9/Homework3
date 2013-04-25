#! /usr/bin/env python
"""
  Seongjin Cho (Josh)
  Student Number: 1130690
  Math 480A

  This is an implementation of algorithm that determines whether
  an imput number is prime number of not. Manindra Angrawal, Neeraj
  Kayal, and Nitin Saxena first published the algorithm. The algorithm
  It has two usable method: isPrime(n) and test().
"""

from fractions import gcd

cdef extern from "math.h":
    cdef long round(double)
    cdef double log(long)
    cdef long ceil(double)
    cdef long floor(double)
    cdef double sqrt(long)

def isPrime(long n):
    result1 = step1(n)
    if result1 == "Possibly Prime":
        r = step2(n)
        result2 = step3(n,r)
        if result2 == "Possibly Prime":
            return step4(n,r)
        else:
            return result2
    else:
        return result1

cdef step1(long n):
    cdef long i
    if n == 2:
        return "Prime"
    elif n%2 == 0:
        return "Composite"
    else:
        # Now we only have odd integers
        for i in xrange(2, round(log(n)/log(3)) + 1):
            if  round(n**(1.0/i))**i == n:
                return "Composite"
        return "Possibly Prime"

cdef step2(long n):
    cdef long r, k
    for r in xrange(2, ceil(log(n)/log(2)**5) + 1):
        if gcd(r,n) == 1:
            for k in xrange(1, floor(log(n)/log(2)**2) + 1):
                if n**k % r == 1:
                    break
            else:
                return r

cdef step3(long n, long r):
    cdef long a
    for a in xrange(2,r+1):
        if gcd(a,n) > 1 and gcd(a,n) < n:
            return "Composite"
    else:
        if n <= r:
            return "Prime"
        else:
            return "Possibly Prime"
            
cdef step4(n, long r):
    cdef long a
    for a in xrange(1, floor(sqrt(r)*log(n)/log(2)) +1):
        if a**n % n != a:
            return "Composite"
    else:
        return "Prime"
