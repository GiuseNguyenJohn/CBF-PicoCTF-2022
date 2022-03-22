#!/usr/bin/python3

import primefac
import gmpy2
from Crypto.Util.number import long_to_bytes, inverse

n = 0xe77c4035292375af4c45536b3b35c201daa5db099f90af0e87fedc480450873715cffd53fc8fe5db9ac9960867bd9881e2f0931ffe0cea4399b26107cc6d8d36ab1564c8b95775487100310f11c13c85234709644a1d8616768abe46a8909c932bc548e23c70ffc0091e2ed9a120fe549583b74d7263d94629346051154dad56f2693ad6e101be0e9644a84467121dab1b204dbf21fa39c9bd8583af4e5b7ebd9e02c862c43a426e0750242c30547be70115337ce86990f891f2ad3228feea9e3dcd1266950fa8861411981ce2eebb2901e428cfe81e87e415758bf245f66002c61060b2e1860382b2e6b5d7af0b4a350f0920e6d514eb9eac7f24a933c64a89
c = 0x671028df2e2d255962dd8685d711e815cbea334115c30ea2005cf193a1b972e275c163de8cfb3d0145a453fec0b837802244ccde0faf832dc3422f56d6a384fbcb3bfd969188d6cd4e1ca5b8bc48beca966f309f52ff3fc3153cccaec90d8477fd24dfedc3d4ae492769a6afefbbf50108594f18963ab06ba82e955cafc54a978dd08971c6bf735b347ac92e50fe8e209c65f946f96bd0f0c909f34e90d67a4d12ebe61743b438ccdbcfdf3a566071ea495daf77e7650f73a7f4509b64b9af2dd8a9e33b6bd863b889a69f903ffef425ea52ba1a293645cbac48875c42220ec0b37051ecc91daaf492abe0aaaf561ffb0c2b093dcdabd7863b1929f0411891f5
e = 0x10001

p = primefac.pollard_pm1(n)
q = int(gmpy2.c_div(n, p))


# ### sanity checking ###
# n_duplicate = gmpy2.mpz(p * q)
# print("Is p * q = n?:")
# print(n_duplicate == n)

# print("Are p and q both prime?")
# print("p: ")
# print(primefac.isprime(p))
# print("q: ")
# print(primefac.isprime(q))

# print(f"{n_duplicate = }")
# print(f"{n = }")
# print(f"{p = }")
# print(f"{q = }")
#########################

# Start general RSA stuff
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)

# Convert m (plaintext in numbers) to text
plaintext = long_to_bytes(m)
print(plaintext.decode())
