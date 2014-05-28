#! /usr/bin/env python
import RSAbaseTransformer, RSAcore, string
ASCmy64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/', '[', ']', ' ']
print "MAKE SURE THE INFORMATION IS ALL IN CAPITALS! "
PW = int (raw_input ("Please enter the public key. "))
key = int (raw_input ("Please enter the general key. "))
textcip = open ("EncryptedMessage.txt", "r+")
textinf = open ("PlainText.txt.txt", "r+")
inf = textinf.read ()
infn = []
cip = ''
condition = ''
if len (inf) % 3 != 0:
	i = len (inf) % 3
	while i < 3:
		inf = inf + ' '
		i = i + 1
i = 0
while i < len (inf):
	j = 0
	while j < 64:
		if ASCmy64 [j] == inf [i]:
			infn.append (j)
			break
		j = j + 1
	if j == 64:
		condition = 'ERROR'
	i = i + 1
if condition != 'ERROR':
	i = 0
	while i < len (inf):
		temp = infn [i] * 64 * 64 + infn [i + 1] * 64 + infn [i + 2]
		temp = RSAcore.core (PW, key, temp)
		j = 0
		while j <= 3:
			cip = cip + ASCmy64 [temp / (64 ** (3 - j))]
			temp = temp % (64 ** (3 - j))
			j = j + 1
		i = i + 3
if condition != 'ERROR':
	textcip.write ("\n" + cip)
else:
	textcip.write ("\n" + "ERROR: INVALID INPUT! ")
textcip.close ()
textinf.close ()