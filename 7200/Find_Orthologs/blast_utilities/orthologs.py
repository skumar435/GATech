#!/usr/bin/env python3

'''
Module to find reciprocal hits in a blast search.
'''
import sys
import os
import subprocess
import blast_utilities.blast_wrapper as blast_wrapper

def readFiles(intFile1, intFile2):
	f1Content = f2Content = ""
	with open(intFile1, 'r') as fRead1:
		f1Content = fRead1.readlines()
	with open(intFile2, 'r') as fRead2:
		f2Content = fRead2.readlines()
	
	return f1Content, f2Content

def getHits(f1Con, f2Con):
	alignDict1 = {}
	alignDict2 = {}
	for line in f1Con:
		data = line.split()
		alignDict1[data[0]] = data[1]

	for line in f2Con:
		data = line.split()
		alignDict2[data[0]] = data[1]

	return alignDict1, alignDict2

def genOrth(dict1, dict2):
	orth_list = []
	for key in dict1:
			if dict1[key] in dict2:
				if dict2[dict1[key]] == key:
					orth_list.append("{}\t{}".format(key, dict1[key]))
	return orth_list

def removeInt(file1, file2, intF1, intF2):
	file1dbreg = file1+"."+"*"
	file2dbreg = file2+"."+"*"
	cmd = "rm {} {} {} {}".format(file1dbreg, file2dbreg, intF1, intF2)
	subprocess.call(cmd, shell=True)

def get_reciprocal_hits(f1, f2, seqtype):
	blast_wrapper.genBlastDB(f1, f2, seqtype)
	intF1, intF2 = blast_wrapper.runBlast(f1, f2, seqtype)
	f1Cont, f2Cont = readFiles(intF1, intF2)
	alignDict1, alignDict2 = getHits(f1Cont, f2Cont)
	ortho_list = []

	if len(alignDict1) >= len(alignDict2):
		ortho_list = genOrth(alignDict1, alignDict2)
	else:
		ortho_list = genOrth(alignDict2, alignDict1)

	removeInt(f1, f2, intF1, intF2)
	return ortho_list