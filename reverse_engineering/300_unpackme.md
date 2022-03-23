# unpackme
Author: David

## Description

Can you get the flag?
Reverse engineer this binary.

## Solution

Download the latest version of `upx` from here:
[UPX](https://upx.github.io/)

Unzip the tarball with `tar zxvf` and then the file name, and then use the full path to the upx binary to unpack the file. Once the binary has been unpacked, open it in Ghidra and go to the main function. User input is compared against 0xb83cb (which is 754635 in decimal). Run the program and send in "754635" as input to receive the flag.

**Flag: picoCTF{up><_m3_f7w_a6870b23}**
