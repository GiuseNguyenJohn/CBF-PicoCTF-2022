# patchme.py

Author: David

## Description

Can you get the flag?
Run this Python program in the same directory as this encrypted flag.

## Solution

This function checks the password against an unecrypted string.
```
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")
```

Put that string together to get the password: `ak98-=90adfjhgj321sleuth9000`

Run the program from the command line with `python3 patchme.py`, and then enter the password.

**Flag: picoCTF{p47ch1ng_l1f3_h4ck_e40c120e}**

