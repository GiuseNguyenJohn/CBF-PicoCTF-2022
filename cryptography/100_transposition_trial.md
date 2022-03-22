# transposition-trial

Author: David

## Description

Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.
Download the corrupted message here.

## Solution

The original message looks like this:
* `heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V8450214}1`

In the challenge description, there's a subtle hint to split this into blocks of three. Upon doing that, and printing each group one after another we see the following message on the right. It may not be obvious at first, but the last column is simply shifted down by one position.
```
heT
fl 
g a
s i
icp
CTo
{7F
4NR
P05
1N5
_16
_35
P3X
51N
3_V
845
021
4}1
```
Here's a non-reusable script that works only for this specific use case to do that:

[decrypt_transposition.py](scripts/decrypt_transposition.py)

Running it, we see the correct message:
`The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_58410214}`

**Flag: picoCTF{7R4N5P051N6_15_3XP3N51V3_58410214}**
