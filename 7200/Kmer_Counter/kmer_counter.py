# Week 6
# Q1.
import sys

k = int(sys.argv[1])
seqFile = sys.argv[2]
seqFileHandle = open(seqFile, 'r')
seqLines = seqFileHandle.readlines()
kDict = {}

def kmerCount(seq) :
	i = 0
	while i+k <= len(seq) :
		if seq[i:i+k] in kDict :
			kDict[seq[i:i+k]] += 1
		else :
			kDict[seq[i:i+k]] = 1
		i += 1

def joinSeq() :
	fullSeq = ""
	for lineNum in range(1,len(seqLines)) :
		fullSeq += seqLines[lineNum].rstrip()
	return fullSeq
		
kmerCount(joinSeq())

for item in sorted(kDict) :
	print ("{}\t{}".format(item, kDict[item]))