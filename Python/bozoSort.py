# -*- coding: utf-8 -*-
from commonFuncs import isSorted, swap
from random import randint

NAME = "Bozo Sort"
STABLE = False
IN_PLACE = True


def sort(list):
	while not isSorted(list):
		i1, i2 = randomIndexes(len(list)-1)
		swap(list, i1, i2)
	return list

def randomIndexes(max):
	i1 = i2 = None
	while i1 == i2:
		i1 = randint(0, max)
		i2 = randint(0, max)
	return (i1, i2)
