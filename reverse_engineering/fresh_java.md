# Fresh Java

Author: David

## Description

Can you get the flag?
Reverse engineer this Java program.

## Solution

Download the CFR Java decompiler:
[CFR](https://www.benf.org/other/cfr/)

Run the Java decompiler on the program (specify your version of the file though): `java -jar cfr-0.152.jar KeygenMe.class`

Here's a sample of the output:
```
        if (string.length() != 34) {
            System.out.println("Invalid key");
            return;
        }
        if (string.charAt(33) != '}') {
            System.out.println("Invalid key");
            return;
        }
        if (string.charAt(32) != '4') {
            System.out.println("Invalid key");
            return;
        }
        if (string.charAt(31) != 'a') {
            System.out.println("Invalid key");
            return;
```

Read through the output and build the flag.

**Flag: picoCTF{700l1ng_r3qu1r3d_0c3de6a4}**
