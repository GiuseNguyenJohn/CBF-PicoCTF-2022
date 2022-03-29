# Operation Orchid
Author: John

## Description
Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

    Download compressed disk image


## Solution
Ok, we don't gain any clues from the challenge description. Let's open
the disk image in `autopsy` and search for `flag`.
Basics on autopsy [here](200_sleuthkit_apprentice.md).

We get two hits, `/3/root/flag.txt` and `/3/root/flag.txt.enc`. Both
files are in `/root`, so let's navigate there. Viewing the `.ash_history`
file there, we can tell what the challenge creator did from the commands
used.
```
Contents Of File: /3/root/.ash_history


touch flag.txt
nano flag.txt 
apk get nano
apk --help
apk add nano
nano flag.txt 
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt
```

The creator made a flag file, made an encrypted copy, and shredded the
plaintext copy. However, we can download the encrypted copy and run the
same `openssl` command they used with the `-d` option to decrypt
the file. The flag is then revealed.

```
$ openssl aes256 -d -salt -in vol4-3.root.flag.txt.enc  -out flag.txt -k unbreakablepassword1234567 
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
140586448766336:error:06065064:digital envelope routines:EVP_DecryptFinal_ex:bad decrypt:../crypto/evp/evp_enc.c:610:
$ cat flag.txt
picoCTF{h4un71ng_p457_cc87abb6}
$
```

**Flag: picoCTF{h4un71ng_p457_cc87abb6}**
