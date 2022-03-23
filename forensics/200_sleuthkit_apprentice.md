# Sleuthkit Apprentice
Author: John

## Description
Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

    Download compressed disk image

## Solution
After downloading the disk image and decompressing with `gzip -d`, we can
run `autopsy` to analyze the image with the command `sudo autopsy`. Visit
the url given in the command output and follow these steps:
1. Click `New Case`
2. Name the case (I just did "sleuth apprentice")
3. Click `Add Host`
4. Click `Add Host` at the bottom
5. Click `Add Image` (a lot of clicking, I know)
6. Click `Add Image File`
7. Enter the location of the image (I `cd`-ed into the directory with
the image, ran `pwd`, and pasted the path and filename in the box)
8. Click `Next`
9. Click `Add` at the bottom (almost there!)
10. Click `Ok`
11. Select the third partition (`/3/`) and click `Analyze`
12. At the top, click `File Analysis`

Finally, we can begin our search. My first thought was to enter `flag` into the 
file name search box on the left, and I got these results:
```
Deleted     Type  		File Name 				   			Written Time 	   				Access Time		 	  			Change Time 				Size 	UID 	GID 	   	Meta 	  
						dir / in	   	
[x]			r / r	   	/3/root/my_folder/flag.txt	   	2021-09-29 11:10:02 (PDT)	   	2021-09-29 11:10:02 (PDT)	   	2021-09-29 11:10:02 (PDT)	   	42	   	101	   	100	   	2082 (realloc)
			r / r	   	/3/root/my_folder/flag.uni.txt	2021-09-29 11:08:48 (PDT)	   	2021-09-29 11:08:29 (PDT)	   	2021-09-29 11:08:48 (PDT)	   	60	   	0	   	0	   	2371
```

As the check mark shows, the first file was deleted, and if we try to click on it
and display the contents, we can't see anything useful:
```
Contents Of File: /3/root/my_folder/flag.txt


            3.449677            13.056403
```

However, there is another file, and clicking on this one reveals the flag!
```
Contents Of File: /3/root/my_folder/flag.uni.txt


�p�i�c�o�C�T�F�{�b�y�7�3�_�5�u�r�f�3�r�_�2�5�b�0�d�0�c�0�}�
```

**Flag: picoCTF{by73_5urf3r_25b0d0c0}**