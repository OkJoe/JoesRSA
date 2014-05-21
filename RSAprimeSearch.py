#! /usr/bin/env python
import random
def primeSearch():
	i = random.randint(512, 2000)
	i = i * 2 - 1
	while True:
		i = i + 2
		prime = i
		j = 3
		while j <= i / 2:
			if i % j == 0:
				prime = 0
				break
			j = j + 2
		if prime != 0:
			break
	return prime