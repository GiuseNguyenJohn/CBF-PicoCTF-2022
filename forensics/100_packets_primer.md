# Packets Primer
Author: John

## Description
Download the packet capture file and use packet analysis software to find the flag.

    Download packet capture

## Solution
Opening the packet capture in wireshark, we see that there are only a few packets. Selecting any of the first TCP packets and right-clicking -> Follow
-> TCP stream yields the flag in plaintext, separated by spaces.

**Flag: picoCTF{p4ck37_5h4rk_2edd7e58}**