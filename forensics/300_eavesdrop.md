# Eavesdrop

Author: David

## Description

Download this packet capture and find the flag.

## Solution

Open the pcap file with `wireshark`. Right click any packet that has "TCP" in the Protocol field, hover over "Follow" and click "Analyze TCP Stream." 
Use the stream toggle in the lower right-hand corner (above "Find Next") to navigate the TCP streams. Also, use the "Show data as" dropdown menu to display the data in various formats.
* Stream 0 is the conversation. View this in ASCII.
```
Hey, how do you decrypt this file again?
You're serious?
Yeah, I'm serious
*sigh* openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
Ok, great, thanks.
Let's use Discord next time, it's more secure.
C'mon, no one knows we use this program like this!
Whatever.
Hey.
Yeah?
Could you transfer the file to me again?
Oh great. Ok, over 9002?
Yeah, listening.
Sent it
Got it.
You're unbelievable
```
* Stream 1 is an HTTP GET request, but it isn't important for now.
* Stream 2 is the file that was mentioned in the conversation. "Show data as" should be set to "Raw" to view the hexdump of the file. Click "Save as..." in the lower-right hand corner of the TCP stream window to extract the file. Save that file as "file.des3" in a directory where you can access it.

Navigate to that directory, and run the command mentioned in the conversation:
    `openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123`
Then, `cat file.txt` to print the flag.

**Flag: picoCTF{nc_73115_411_91361db5}**
