#! /usr/bin/env python
import RSAbaseTransformer, RSAcore, string
ASCmy64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/', '[', ']', ' ']
PW = int (raw_input ("Please enter the private key. "))
key = int (raw_input ("Please enter the general key. "))
text = open ("text.txt", "r+")
cip = text.read ()
cipn = []
inf = ''
condition = ''
if len (cip) % 4 != 0:
	condition = 'ERROR'
i = 0
while i < len (cip):
	j = 0
	while j < 64:
		if ASCmy64 [j] == cip [i]:
			cipn.append (j)
			break
		j = j + 1
	if j == 64:
		condition = 'ERROR'
	i = i + 1
if condition != 'ERROR':
	i = 0
	while i < len (cip):
		temp = cipn [i] * 64 * 64 * 64 + cipn [i + 1] * 64 * 64 + cipn [i + 2] * 64 + cipn [i + 3]
		temp = RSAcore.core (PW, key, temp)
		j = 0
		while j <= 2:
			inf = inf + ASCmy64 [temp / (64 ** (2 - j))]
			temp = temp % (64 ** (2 - j))
			j = j + 1
		i = i + 4
if condition != 'ERROR':
	text.write ("\n" + inf)
else:
	text.write ("\n" + "ERROR: INVALID INPUT! ")
text.close ()