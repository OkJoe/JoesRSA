#! /usr/bin/env python
import RSAbaseTransformer, RSAcore, string
ASCmy64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/', '[', ']', '\\']
PW = int (raw_input ("Please enter the private key. "))
key = int (raw_input ("Please enter the general key. "))
cip = raw_input ("Please enter the code. ")
inf = ''
i = 0
while i < len (cip):
	a = cip [i]
	b = cip [i + 1]
	c = cip [i + 2]
	d = cip [i + 3]
	j = 0
	while j < 64:
		if ASCmy64[j] == a:
			a = j
		j = j + 1
	j = 0
	while j < 64:
		if ASCmy64[j] == b:
			b = j
		j = j + 1
	j = 0
	while j < 64:
		if ASCmy64[j] == c:
			c = j
		j = j + 1
	j = 0
	while j < 64:
		if ASCmy64[j] == d:
			d = j
		j = j + 1
	temp = a * 64 * 64 * 64 + b * 64 * 64 + c * 64 + d
	temp = RSAcore.core (PW, key, temp)
	j = 0
	while j <= 2:
		inf = inf + ASCmy64 [temp / (64 ** (2 - j))]
		temp = temp % (64 ** (2 - j))
		j = j + 1
	i = i + 4
print "The information is: ", inf