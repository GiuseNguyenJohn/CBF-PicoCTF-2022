# Lookey here

## Description
Attackers have hidden information in a very large mass of data in
the past, maybe they are still doing it. Download the data here.

## Solution
Given the low point value of the challenge and the fact that the data
is in plaintext, we can deduce that the flag is somewhere in the plaintext
file, and we can just use `grep` to find the flag.

```
$ cat anthem.flag.txt | grep picoCTF
      we think that the men of picoCTF{gr3p_15_@w3s0m3_c91a291d}
$
```
Flag: picoCTF{gr3p_15_@w3s0m3_c91a291d}

