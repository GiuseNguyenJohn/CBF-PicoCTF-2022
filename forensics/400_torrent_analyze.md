# Torrent Analyze

Author: David

## Description

SOS, someone is torrenting on our network.
One of your colleagues has been using torrent to download some files on the company’s network. Can you identify the file(s) that were downloaded? The file name will be the flag, like `picoCTF{filename}`.

## Solution

Open the file in Wireshark. As suggested by the challenge hint, go to "Analyze" > "Enabled Protocols" and enable all BT or BitTorrent protocols that aren't already enabled.

This writeup addresses only what is needed to obtain the flag. For a more thorough understanding of how torrent traffic is analyzed and examined, view this webpage that I came across in my research:
[Examining Torrent Traffic](https://www.malware-traffic-analysis.net/2013/09/14/index.html)

To find the name of the file that was torrented over the network, we need to know the hash of the file. We can find that in Wireshark.

The filter `bittorrent.info_hash` did not work, so I resorted to searching for "info_hash" in the packet details. To do this, press Ctrl+F, set the first field to "Packet details," the second field to "Narrow & Wide", turn case sensitive off, and set the last field to "String".

In Wireshark's folder structure for packet details, the info hash can be found in "BitTorrent DHT Protocol" > "Request arguments" > "Value" > "info_hash".

From packet 51080 onward, the info hash is "e2467cbf021192c241367b892230dc1e05c0580e".

The first Google search result yields this file name: "ubuntu-19.10-desktop-amd64.iso"

And we'll wrap that in flag format to get the flag.


**Flag: picoCTF{ubuntu-19.10-desktop-amd64.iso}**
