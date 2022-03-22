# File types
Author: John
## Description
This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.
You can download the file from here.

## Solution

When we run `file` on the file, we get this output:
```
$ file Flag.pdf
Flag.pdf: shell archive text
```
Ok, so it's text of some sort. Let's `cat` the file and see what it is.
First part of output we see:
```
#!/bin/sh
# This is a shell archive (produced by GNU sharutils 4.15.2).
# To extract the files from this archive, save it to some FILE, remove
# everything before the '#!/bin/sh' line above, then type 'sh FILE'.
```
Awesome, straightforward instructions! Let's do it:
```
$ chmod +x Flag.pdf
$ sh Flag.pdf
x - created lock directory _sh00046.
x - extracting flag (text)
Flag.pdf: 119: uudecode: not found
restore of flag failed
flag: MD5 check failed
x - removed lock directory _sh00046.
```
So it didn't work. One line in particular stands out - `Flag.pdf: 119: uudecode: not found`.
Let's find out what uudecode is. Googling `uudecode download` and
choosing the first result, we find this from `access.redhat.com`:
```
The uuencode and uudecode command comes with sharutils package.
```
Ok, let's install `sharutils` and run it again.
```
$ sudo apt install sharutils
-- cut --
$ sh Flag.pdf
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.
$ ls
Flag.pdf  flag
$
```
It worked! Then just `cat flag` to view the flag.

```
$ cat flag
!<arch>
flag/           0           0     0     644     1024      `
4�4i�ѵ��F�DѣCC �M4hɦ�Sd��Y�6��"�������ש����5�h��{����������N��4���Ѡ2
0!�a�                    �0�6�2F����&���2&�� �
��y ڀ��
�^��r�e��L�ʿ��H"72�\U#f�*������qCa}�s6��
`�K�I�{Wx�#W5�+f�и-�#i���G�£vV�#��%
�G>.���Z8ѬL×��9�%)�`��1�CxyR��=��9nf�q�!��h����f우��T��6��      ��݆������F�&�ؘbB�uu�!�"`e9P�Q���K3F�Q�k�C���)8
                  ���
!��F5'(5��3�L�@�     ��H��,�hQ&�
 k��.Th2�D���`�>;<�����"�(HH�]���q
```

...or so I thought. According to `file`, it's a `ar` archive.
```
flag: current ar archive
```
By doing some research, we can use the `ar` utility to extract this archive.
```
$ ar x flag
$ file flag
flag: cpio archive
$
```
GAAAAHHH...another archive. Following the similar steps of researching, finding a tool,
and extracting, we finally get to the plaintext flag file. Here are the types of 
archives in order:
- cpio
- bzip2
- gzip
- lzip
- lz4
- lzma
- fiel
- lzop
- lzip
- XZ

After extracting them, there is a file with hex characters. Decode the hex for the flag.

**Flag: picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_278f1a18}**