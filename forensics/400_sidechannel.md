# Sidechannel
Author: John

## Description
There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag?
Download the PIN checker program here pin_checker
Once you've figured out the PIN (and gotten the checker program to accept it), connect to the master server using nc saturn.picoctf.net 53932 and provide it the PIN to get your flag.

## Solution
While researching the first hint (Read about "timing-based side-channel attacks."),
I came accross this gold mine of a resource.

> "Let us assume that the correct password is 5263987149, and the attacker starts guessing from the first digit (beginning from 0000000000). He measures that the system returns false after x seconds. After getting the same response time x for the first five guesses (i.e., from 0000000000 to 4000000000), he notices that the system takes a slightly longer time to respond ( x + ∆ x) when he tries 5000000000. This is because the for loop during its first iteration doesn’t return false since the first digit of the user input and the stored password is equal. Hence, the loop runs another iteration, thereby taking more time (∆x). Therefore, the attacker knows that the first digit he tried now is correct. He can repeat the same procedure to guess the remaining digits by observing the pattern of ∆x. In this way, it would take the attacker only 10*10 guesses at the maximum to find the correct password, compared to 10¹⁰ possible combinations while trying to brute force it…" (Source: https://medium.com/spidernitt/introduction-to-timing-attacks-4e1e8c84b32b)

Ok, the theory is pretty simple and I understand
it, so how do I put this into practice?
My answer to this question was to look up `side channel attack` in Github.

```python
def get_response_delay(config, data):
	request = urllib2.Request(config["url"])
	request = set_headers(config, request)

	start = 0
	try:
		if config["verbose"]:
			print "[VERBOSE***] Sending the following data: %s" % (config["data"] % urllib.quote(data))
		
		start = time.time()
		response = urllib2.urlopen(request, (config["data"] % urllib.quote(data)))
	except:
		delay = time.time() - start
		if config["verbose"]:
			print "[VERBOSE***] Exception was raised: %s" % sys.exc_info()[0]
		return delay
	
	delay = time.time() - start	
	
	if config["verbose"]:
		print "[VERBOSE***] HTTP response for %s" % data
		print response.read()
		
	return delay
```
(Source: https://github.com/Mr-Un1k0d3r/SideChannelAttack/blob/master/sidechannel.py)

As you can see in this code snippet I found, 