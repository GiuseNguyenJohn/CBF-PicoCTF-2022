# Operation Oni
Author: John

## Description
Description

Download this disk image, find the key and log into the remote machine. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

    Download disk image
    Remote machine: ssh -i key_file -p 55271 ctf-player@saturn.picoctf.net

## Solution
Ok, so from the description we can tell that we are searching for an ssh
private key. Let's open the disk image in `autopsy` and search for `ssh`.
Basics on autopsy [here](200_sleuthkit_apprentice.md).

One of the results when we search is `/2/root/.ssh`. This looks promising, if the ssh key is in the `/root` directory, then it must be important!
When we go to that directory in autopsy, we see a `id_ed25519` file and a `id_ed25519.pub` file.

```
Contents Of File: /2/root/.sshid_ed25519


-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
```

These are the keys! We only want the private key, though, so let's select
the private key file, click `Export` to download the file, use 
`chmod 700 <filename>` to set the correct permissions, then run the
command in the challenge description to log in. Finally, cat
the flag!

```
ctf-player@challenge:~$ ls
flag.txt
ctf-player@challenge:~$ cat flag.txt 
picoCTF{k3y_5l3u7h_339601ed}ctf-player@challenge:~$
```

**Flag: picoCTF{k3y_5l3u7h_339601ed}**