Seongjin Cho
============



Homework 3, number 2
"Compute the sum of the squares of the positive integers up to n
, where you may assume that n is at most 10000."

Uses the 

sage: load homework3a.py
sage: %timeit sum(1000)
625 loops, best of 3: 15.1 µs per loop

sage: load homework3a.pyx
sage: %timeit sum(1000)
625 loops, best of 3: 1.23 µs per loop
