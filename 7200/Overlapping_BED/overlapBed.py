#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser(prog='Overlap', prefix_chars='-')
parser.add_argument('-i1', help="input file1")
parser.add_argument('-i2', help="input file2")
parser.add_argument('-m', help="minimum overlap")
parser.add_argument('-o', help="output file")
parser.add_argument('-j', help="print file2 content", action="store_true")
args = parser.parse_args()

file1 = args.i1
file2 = args.i2
outputFile = args.o
minOL = args.m
f2PrintFlag = args.j

f1Cont = ""
f2Cont = ""

with open(file1, 'r') as fh:
	f1Cont = fh.readlines()
with open(file2, 'r') as fh2:
	f2Cont = fh2.readlines()

f1Dict = {}
for line in f1Cont:
	chrD = line.split()
	if chrD[0] not in f1Dict:
		f1Dict[chrD[0]] = [[int(chrD[1]), int(chrD[2])]]
	else:
		f1Dict[chrD[0]].append([int(chrD[1]), int(chrD[2])])

f2Dict = {}
for line in f2Cont:
	chrD = line.split()
	if chrD[0] not in f2Dict:
		f2Dict[chrD[0]] = [[int(chrD[1]), int(chrD[2])]]
	else:
		f2Dict[chrD[0]].append([int(chrD[1]), int(chrD[2])])

outputW = []
for item in f1Dict:
	i= 0
	startJ = 0
	while i < len(f1Dict[item]):
		counter = 0
		j = startJ
		while j < len(f2Dict[item]):
			if f1Dict[item][i][1] >= f2Dict[item][j][0]:
				if f1Dict[item][i][0] >= f2Dict[item][j][1]:
					if counter == 0 and i < (len(f1Dict[item]) - 1) and f2Dict[item][j][1] >= f1Dict[item][i+1][0] and f2Dict[item][j][0] <= f1Dict[item][i+1][1]:
						startJ = j
						counter = 1
					j += 1
				else:
					overLap = (min(f1Dict[item][i][1], f2Dict[item][j][1]) - max(f1Dict[item][i][0], f2Dict[item][j][0]))*100/(f1Dict[item][i][1] - f1Dict[item][i][0] + 1)
					if overLap > float(minOL):
						if f2PrintFlag:
							apLine = "{}\t{}\t{}\t{}\t{}\t{}\n".format(item, f1Dict[item][i][0], f1Dict[item][i][1], item, f2Dict[item][i][0], f2Dict[item][i][1])
							outputW.append(apLine)
						else:
							apLine = "{}\t{}\t{}\n".format(item, f1Dict[item][i][0], f1Dict[item][i][1])
							if apLine not in outputW:
								outputW.append(apLine)
					if counter == 0 and i < (len(f1Dict[item]) - 1) and f2Dict[item][j][1] >= f1Dict[item][i+1][0] and f2Dict[item][j][0] <= f1Dict[item][i+1][1]:
						startJ = j
						counter = 1
					j += 1
			else:
				break
		i += 1


with open(outputFile, 'w') as fh3:
	fh3.writelines(outputW)