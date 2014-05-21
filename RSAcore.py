#! /usr/bin/env python
import RSAbaseTransformer, math
def core (PW, key, inf):
	PW2 = RSAbaseTransformer.base10to2 (PW)
	mod = inf
	cip = 1
	i = 0
	while i <= 23:
		cip = (cip * mod ** int (PW2 [23 - i])) % key
		mod = (mod * mod) % key
		i = i + 1
	return cip