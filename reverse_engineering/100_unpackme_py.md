# unpackme.py

Author: David

## Description

Can you get the flag?
Reverse engineer this Python program.

## Solution

The code looks like this: 
```
payload = b'gAAAAABiMD1Ju5_eZeZy7C03K_YcWGDGXfvy5A9b5HzV-uZIYN8syTFGHgLwoRonYtCS0WcDrufxRRXlvNKtyEMqMS0AADLcRNr6VYpLLbKaETF37L22GEg1ok8NutHXK6gy47sBLmxmWWU729b86rzK6IMc2Kg-CR0bMm_fzrbRrWEYSk0WRNnKxy7Juuy-Ss2RjbACKgbwL7HNGATu3hYuPflf3PCKztLRFXCBxijKncKZgt68wYhGnPAzYvUVrdhhtMg9ra7ZKIirltPfKC8iX2DqmR9vVA=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())
```
We see it decrypts the payload, and then executes it as Python code. If we comment out the `exec()` line and `print(plain)` instead, we'll see the code that would execute.

```
b"\npw = input('What\\'s the password? ')\n\nif pw == 'batteryhorse':\n  print('picoCTF{175_chr157m45_616d21a3}')\nelse:\n  print('That password is incorrect.')\n\n"
```
The flag is stored in plaintext.

**Flag: picoCTF{175_chr157m45_616d21a3}**

