

def encode(long_url):
	counter+=1
	digits = "0123456789abcdefghijklmnopqrstuvwxyzABCEDGHIJKLMNOPQRSTUVWXYZ-_"
	digitlist = []

	curr = counter
	while curr > 64:
		quotient = curr / 64
		remainder = curr % 64
		digitlist.append(digits[remainder])
		curr = quotient

	if curr > 0 :
		digitlist.append(digits[curr])
	digits.reverse()
	short_url = "".join(digitlist)
	hashmap[short_url] = long_url
	return "http://bit.ly/" + short_url


def decode(short_url):
	#clip out the front half
	return hashmap[backhalf]


"""

1. Counter method

Pros:
Unique number is generated each time

Cons:
Predictable

2. Generate random or unpredectible urls using hash

	- Generate random string
	- Timestamp
	- Apply Cryptographic hash function to 
			- Long URL
			- Timestamp / Counter Value
			- Combination of these

Hash functions are deterministic - that means they are psuedo random and cannot be always random but by combining it with timestamps/unique counter
the complete value might be unique
If hash output is not as short as wanted then we take prefix or suffix or portion of it and if collisions happen we can retry 
Best way to design this hash function is use some cryptographic hash function like MD5 / SHA-1 to minimize the number of collisions  

3. Pre generate the short urls offline ("Key Generation Service")

Downside : Need extra space to store all pregenerated short URLs
"""