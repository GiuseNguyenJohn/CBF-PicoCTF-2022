# Sum-O-Primes

Author: David

## Description

We have so much faith in RSA we give you not just the product of the primes, but their sum as well!

## Solution

From what I've learned so far, at the heart of an RSA challenge is obtaining n, e, p and q, and using those to decrypt c.
Before we continue, general some notes about RSA:
* c is the ciphertext
* p and q are (very large) primes
* n is the product of p and q
* e is almost always 65537 (0x10001) 

Here, looking at the script used to generate the ciphertext, as well its output, we see we're given n and e. However, we're also given the sum of p and q. Odd...

Research on Google brings about the following Stack Exchange page: 
[Relation between factors and their sum on RSA](https://crypto.stackexchange.com/questions/87308/relation-between-factors-and-their-sum-on-rsa)

In short, the quadratic equation can be used. If we know that `x = p + q` and `n = p * q`, then
* Let `delta = sqrt(x ** 2 - 4n)`.
* Let `p = (x + delta) / 2`.
* Let `q = (x - delta) / 2`.

With p and q, we can perform general RSA decryption to print the flag. To better understand this concept, watch John Hammond's handful of videos on decrypting RSA from CTF challenges.

Here's part of the important stuff for classic decryption.

* Notes on imports
    * `import gmpy2` for some better handling of all the large numbers in Python.
    * `from Crypto.Util.number import inverse, long_to_bytes` to print plaintext easily.

```
# Start general RSA stuff
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)

# Convert m (plaintext in numbers) to text
plaintext = long_to_bytes(m)
print(plaintext.decode())
```
[sum_of_primes_reverse_gen.py](scripts/sum_of_primes_reverse_gen.py)

**Flag: picoCTF{126a94ab}**
