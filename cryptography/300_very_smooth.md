# Very Smooth

Author: David

## Description

Forget safe primes... Here, we like to live life dangerously... >:)

## Solution

As with the previous RSA challenge, the goal here is to find p and q by exploiting some weakness in this particular n value for RSA.

The challenge description and title refer to a "smooth" prime, and the hint references "Mr. Pollard". All of this information suggests to use Pollard's p-1 algorithm for efficiently finding smooth prime factors of a large number. 

### Notes on imports
* `import primefac` to use it's Python algorithm for Pollard's p-1
* `import gmpy2` to handle operations with large numbers
* `from Crypto.Util.number import inverse, long_to_bytes` to easily handle RSA stuff.

With n, p, q, e, and c all defined, we can complete the formulaic RSA description method below. Watch John Hammond's videos on RSA for a more thorough explanation.

```
# Start general RSA stuff
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)

# Convert m (plaintext in numbers) to text
plaintext = long_to_bytes(m)
print(plaintext.decode())
```

View the full script below.

[very_smooth_reverse_gen.py](scripts/very_smooth_reverse_gen.py)

**Flag: picoCTF{94287e17}**
