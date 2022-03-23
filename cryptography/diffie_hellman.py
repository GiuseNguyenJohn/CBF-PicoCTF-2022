#!/usr/bin/python3

# p = 13 (n = 13)
# g = 5
# alice chose 7
# bob chose 3

n = 13
g = 5
a = 7
b = 3

# Both keys below are the same.
alice_public = (g ** a) % n
bob_public = (g ** b) % n

# All shared keys should be the same.
shared_key = (g ** (a*b)) % n
shared_key_2 = (alice_public ** b) % n
shared_key_3 = (bob_public ** a) % n

# print(alice_public)
# print(bob_public)
# print(shared_key_2)
# print(shared_key_3)

# This is the shift value
print(shared_key)
