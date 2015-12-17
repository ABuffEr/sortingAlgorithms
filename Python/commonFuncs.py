# -*- coding: utf-8 -*-
from contextlib import contextmanager
import time

def isSorted(list):
	for n in xrange(0,len(list)-1):
		if list[n] > list[n+1]:
			return False
	return True

def swap(list, i1, i2):
	list[i1],list[i2] = list[i2],list[i1]

# code from: https://stackoverflow.com/questions/889900/accurate-timing-of-functions-in-python

@contextmanager
def timeblock(label):
	start = time.clock()
	try:
		yield
	finally:
		end = time.clock()
		print ('{}: {}'.format(label, end-start))
