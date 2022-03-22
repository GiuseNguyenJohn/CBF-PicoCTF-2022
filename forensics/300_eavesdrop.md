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
* Stream 1 is an HTTP GET request, but it isn't important.
* Stream 2 is the file that was mentioned in the conversation. "Show data as" should be set to "Raw" to view the hexdump of the file. Click "Save as..." in the lower-right hand corner of the TCP stream window to extract the file. Save that file as "file.des3" in a directory where you can access it.
```
474554202f20485454502f312e310d0a486f73743a20636f6e6e65637469766974792d636865636b2e7562756e74752e636f6d0d0a4163636570743a202a2f2a0d0a436f6e6e656374696f6e3a20636c6f73650d0a0d0a
485454502f312e3120323034204e6f20436f6e74656e740d0a446174653a204d6f6e2c203034204f637420323032312031383a30383a353220474d540d0a5365727665723a204170616368652f322e342e313820285562756e7475290d0a582d4e6574776f726b4d616e616765722d5374617475733a206f6e6c696e650d0a436f6e6e656374696f6e3a20636c6f73650d0a0d0a
```

Navigate to that directory, and run the command mentioned in the conversation:
    `openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123`
Then, `cat file.txt` to print the flag.

**Flag: picoCTF{nc_73115_411_91361db5}**
