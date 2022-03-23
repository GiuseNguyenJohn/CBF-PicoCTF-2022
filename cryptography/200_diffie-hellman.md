# diffie-hellman

Author: David

## Description

Alice and Bob wanted to exchange information secretly. The two of them agreed to use the Diffie-Hellman key exchange algorithm, using p = 13 and g = 5. They both chose numbers secretly where Alice chose 7 and Bob chose 3. Then, Alice sent Bob some encoded text (with both letters and digits) using the generated key as the shift amount for a Caesar cipher over the alphabet and the decimal digits. Can you figure out the contents of the message?
Download the message here.
Wrap your decrypted message in the picoCTF flag format like: `picoCTF{decrypted_message}`

## Solution

We have a Caesar Cipher without a key that's been explicitly stated. To complete this challenge the intended way, we need to find the shared key. Ultimately, this is done by taking g, raising it to (a*b), and then finding the result of that value mod p.

Here's an annotated script to do that:
[diffie_hellman.py](scripts/diffie_hellman.py)

View this video from Computerphile for more on the mathematics behind Diffie-Hellman.

[Diffie Hellman -the Mathematics bit- Computerphile](https://www.youtube.com/watch?v=Yjrfm_oRO0w)

The result is 5, and this was the *encrypt* value. We need to *decrypt* it, so the shift will be -5. Use a tool like Cryptii to shift the encoded flag, and then wrap it in flag format. Don't forget change the shift alphabet to include numbers!
* Alphabet should be "abcdefghijklmnopqrstuvwxyz0123456789"

**Flag: picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_7609EC61}**
