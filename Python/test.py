# -*- coding: utf-8 -*-
from random import randint
import glob
import os
from commonFuncs import timeblock

def map():
	curPath = os.path.dirname(__file__)
	algList = []
	for file in glob.glob(os.path.join(curPath, "*Sort.py")):
		module = file.split("\\")[-1].rsplit(".", 1)[0]
		alg = __import__(module)
		algList.append((alg.NAME, file))
		del alg
	return dict(zip(range(len(algList)),algList))

def printChoices():
	d = map()
	for (k,v) in d.items():
		print "%d: %s"%(k,v[0])

def run(algInd, maxValue, maxLength):
	d = map()
	algName = d[algInd][0]
	algFile = d[algInd][1]
	print "Your choice: %s"%algName
	algModule = algFile.split("\\")[-1].rsplit(".", 1)[0]
	alg = __import__(algModule)
	list = [randint(0,maxValue) for n in xrange(maxLength)]
	print "Unsorted list:",list
	with timeblock("%s executed in"%algName):
		alg.sort(list)
	print "Sorted list:",list

if __name__ == "__main__":
	input = maxValue = maxLength = None
	paramsOk = False
	while not paramsOk:
		maxValue = raw_input("Digit max value for single list item (i.g.: 999): ")
		maxLength = raw_input("Digit max length of list to process: ")
		if maxValue.isdigit() and maxLength.isdigit():
			paramsOk = True
		else:
			print "Invalid inputs!"
	print "Write number to choose algorithm, 'list' to get available algorithms, 'exit' to close."
	print "Available algorithms:"
	printChoices()
	while input != "exit":
		input = raw_input("Digit your choice: ")
		if input == "list":
			printChoices()
		elif input != "exit":
			if not input.isdigit():
				print "Invalid input!"
			else:
				args = [int(x) for x in [input, maxValue, maxLength]]
				run(*args)
