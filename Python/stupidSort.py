# -*- coding: utf-8 -*-
from commonFuncs import isSorted, swap
from random import randint

NAME = "Stupid Sort (Bogosort, Blort/Bort/Monkey/Random/Stochastic/Drunk Man Sort)"
STABLE = False
IN_PLACE = True

def sort(list):
	while not isSorted(list):
		permutate(list)
	return list

def permutate(list):
	n = len(list)
	for i in xrange(n):
		rnd = randint(0, n-i-1)
		swap(list, rnd, i)
