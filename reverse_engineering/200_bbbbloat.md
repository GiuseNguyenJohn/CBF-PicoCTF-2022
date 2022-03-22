# Bbbbloat
Author: David

## Description
Can you get the flag?
Reverse engineer this binary.

## Solution
Upon running the program, it asks for it's favorite number:
```
$ ./bbbbloat 
What's my favorite number? aaaaaa
Sorry, that's not it!
```

Open the program in Ghidra. In the symbol tree window, open the Functions folder and then double click to open FUN_00101307 and view the decompilation. The following lines of code are important:
```
  if (local_48 == 0x86187) {
    __s = (char *)FUN_00101249(0,&local_38);
    fputs(__s,stdout);
    putchar(10);
    free(__s);
```
This compares the number we input against 0x86187, which is 549255 in decimal. Enter 549255 as program input to receive the flag.
```
./bbbbloat 
What's my favorite number? 549255
picoCTF{cu7_7h3_bl047_cbc074c0}
```
**Flag: picoCTF{cu7_7h3_bl047_cbc074c0}**
