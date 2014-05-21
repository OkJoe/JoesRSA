#! /usr/bin/env python
import RSAprimeSearch, math
p = RSAprimeSearch.primeSearch()
q = RSAprimeSearch.primeSearch()
n = 1
PWpublish = 0
PWprivate = 0
while True:
	n = n + (p - 1) * (q - 1)
	i = int (math.sqrt (n)) - 1
	while i > 50:
		if n % i == 0:
			PWpublish = i
			PWprivate = n / i
			break
		i = i - 1
	if PWpublish != 0:
		break
print "PWpublish: ", PWpublish, "PWprivate: ", PWprivate, "Key: ", p * q