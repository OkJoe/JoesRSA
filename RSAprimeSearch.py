#! /usr/bin/env python
import random
def primeSearch():
	i = random.randint(512, 2000)
	i = i * 2 + 1
	while i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 11 == 0 or i % 13 == 0 or i % 15 == 0 or i % 17 == 0 or i % 19 == 0 or i % 23 == 0 or i % 29 == 0 or i % 31 == 0:
		i = i + 2
	return i