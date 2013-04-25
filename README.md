Seongjin Cho
============

I had to edit this file after the midnight since the changes I made on online site
had rolled back after I uploaded files through command prompt....

Homework 3, number 1
====================

"Take whatever algorithm you implemented in assignment two, and make it faster"

I could not improve the program very much because
1. I could not use built in sage euler_phi function anymore after I changed the file into cython code.
So I had to use much larger bound for the last step which is $\sqrt(n)$ rather than $\sqrt(euler_phi(n))$.
2. I did not put much effort to change codes to make the implementation favors to the cython.
3. The algorithm itself is quite slow (and I did not implement it in fully optimized way also).
4. I will add some method for special prime numbers, and I will add some probablistic algorithm for the large number
(Well it will depends on the error bound..)

# Time Difference
- sage: n = next_prime(2^15)
- sage: %timeit isPrime1(n)	#original
- 5 loops, best of 3: 257 ms per loop
- sage: %timeit isPrime2(n)	#cythoned
- 5 loops, best of 3: 138 ms per loop

Homework 3, number 2
====================

"Compute the sum of the squares of the positive integers up to n
, where you may assume that n is at most 10000."

# Time Difference
- sage: load homework3a.py
- sage: %timeit sum(1000)
- 625 loops, best of 3: 15.1 µs per loop
- sage: load homework3a.pyx
- sage: %timeit sum(1000)
- 625 loops, best of 3: 1.23 µs per loop

Homework 3, number 3
====================

"Compute a list of all prime numbers up to 10000."

Uses Sieve of Erastosthenes.

# Time Difference
- sage: load homework3b.py
- sage: %timeit prime_gen()
- 625 loops, best of 3: 4.96 ms per loop
- sage: load homework3b.pyx
- sage: %timeit prime_gen()
- 625 loops, best of 3: 1.39 ms per loop


Homework 3, number 4
====================

"Compute the determinant of a 4x4 matrix of double precision floating point numbers."

Uses LU decomposition. Most of the codes are from "Rosetta Code". Also It has one
very Critical fault. It does not keep track of sign. I could not find a good
method in computing permutatin matrices into -1 or 1...

# Time Difference
- sage: load homework3c.py
- sage: a = [[round(random()*100,5) for i in range(10)] for i in range(10)]
- sage: %timeit det(a)
- 25 loops, best of 3: 10.1 ms per loop
- sage: load homework3c.pyx
- sage: %timeit det(a)
- 25 loops, best of 3: 8.88 ms per loop

Homework 4, number 5
====================

"Multiply a 4x4 matrix of double precision floating point numbers times another 4x4 matrix."

First started with Strassen Algorithem. However, I realized implementing that algorithm without using numpy or any other sophiscated library
with full generality takes quite a lot of time... So I just multiplied matrix term by term as it is only for the 4x4 matrices.

# Time Difference
- sage: a = [[round(random()*100,5) for i in range(10)] for i in range(10)]
- sage: b = [[round(random()*100,5) for i in range(10)] for i in range(10)]
- sage: load homework3da.py
- sage: %timeit multiply(a,b)
- 125 loops, best of 3: 1.77 ms per loop
- sage: load homework3da.pyx
- sage: %timeit multiply(a,b)
- 625 loops, best of 3: 1.26 ms per loop
