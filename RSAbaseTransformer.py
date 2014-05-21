#! /usr/bin/env python
def base10to2(var):
	
	s = 23
	temp = ''
	
	while s >= 0:
		temp = temp + str (var / (2 ** s))
		var = var % (2 ** s)
		s = s - 1
	return temp

def base2to10(temp):

	return int (temp, 2)