#! /usr/bin/env python
import RSAbaseTransformer, RSAcore, string
ASCmy64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/', '[', ']', '\\']
PW = int (raw_input ("Please enter the public key. "))
key = int (raw_input ("Please enter the general key. "))
inf = raw_input ("Please enter the information. ")
cip = ''
if len (inf) % 3 != 0:
	i = len (inf) % 3
	while i < 3:
		inf = inf + '_'
		i = i + 1
i = 0
while i < len (inf):
	a = inf [i]
	b = inf [i + 1]
	c = inf [i + 2]
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
	temp = a * 64 * 64 + b * 64 + c
	temp = RSAcore.core (PW, key, temp)
	j = 0
	while j <= 3:
		cip = cip + ASCmy64 [temp / (64 ** (3 - j))]
		temp = temp % (64 ** (3 - j))
		j = j + 1
	i = i + 3
print "The code is: ", cip