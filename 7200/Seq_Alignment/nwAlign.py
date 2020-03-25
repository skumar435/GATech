#!/bin/env python3

seq1 = input("Enter sequence 1: ") # get the sequence 1
seq2 = input("Enter sequence 2: ") # get the sequence 2

# extract length and use for scoring matrix
m = len(seq2) + 1
n = len(seq1) + 1

# creates the score matrix for the input sequences
def create_matrix(m, n) :
	scoreMatrixTemp = [ ['-'] * n for x in range(m) ] # generate empty matrix of m*n
	for i in range(m) :
		for j in range(n) :
			if i == 0 and j > 0 :
				scoreMatrixTemp[i][j] = scoreMatrixTemp[i][j-1] - 1 # first row initialisation
			elif j == 0 and i > 0 :
				scoreMatrixTemp[i][j] = scoreMatrixTemp[i-1][j] - 1 # first column initialisation
			elif i > 0 and j > 0 :
				if seq2[i-1] == seq1[j-1] :
					scoreMatrixTemp[i][j] = max(scoreMatrixTemp[i-1][j-1] + 1, scoreMatrixTemp[i-1][j] - 1, scoreMatrixTemp[i][j-1] - 1) # match case - max of (diagonal + 1, up - 1 and left - 1)
				else :
					scoreMatrixTemp[i][j] = max(scoreMatrixTemp[i-1][j-1] - 1, scoreMatrixTemp[i-1][j] - 1, scoreMatrixTemp[i][j-1] - 1) # mismatch case - max of (diagonal - 1, up - 1 and left - 1)
			else :
				scoreMatrixTemp[i][j] = 0 # first element in the matrix assigned 0
	return scoreMatrixTemp

scoreMatrix = create_matrix(m, n)

# trace back the path from the last element to return aligned sequences
def trace_back(scoreMatrix) :
	alSeq1 = [] # list for aligned sequence 1
	alSeq2 = [] # list for aligned sequence 2
	i = len(seq2)
	j = len(seq1)
	while i > 0 or j > 0 :
		if i > 0 and j > 0 :
			if seq1[j-1] == seq2[i-1] : # match scenario
				if scoreMatrix[i-1][j-1] + 1 >= scoreMatrix[i-1][j] - 1 and scoreMatrix[i-1][j-1] + 1 >= scoreMatrix[i][j-1] - 1:
					alSeq1.append(seq1[j-1]) # add nucl from seq1 to aligned seq1 for match
					alSeq2.append(seq2[i-1]) # add nucl from seq2 to aligned seq2 for match
					i -= 1 # move row up
					j -= 1 # move column left
			else : # mismatch scenario
				if scoreMatrix[i-1][j-1] - 1 >= scoreMatrix[i-1][j] - 1 and scoreMatrix[i-1][j-1] - 1 >= scoreMatrix[i][j-1] - 1:
					alSeq1.append(seq1[j-1]) # add nucl from seq1 to aligned seq1 if diagonal is highest
					alSeq2.append(seq2[i-1]) # add nucl from seq2 to aligned seq2 if diagonal is highest
					i -= 1 # move row up
					j -= 1 # move column left
				elif scoreMatrix[i-1][j] - 1 >= scoreMatrix[i][j-1] -1 :
					alSeq2.append(seq2[i-1]) # add nucl from seq2 to aligned seq2 if top is highest
					alSeq1.append("-") # add gap to aligned seq1 because of trace up
					i -= 1 # move row up
				else :
					alSeq1.append(seq1[j-1]) # add nucl from seq1 to aligned seq1 if left is highest
					alSeq2.append("-") # add gap to aligned seq2 because of trace left
					j -= 1 # move column left
		elif i == 0 :
			alSeq1.append(seq1[j-1]) # add nucl from seq1 to aligned seq1 if left is highest
			alSeq2.append("-") # add gap to aligned seq2 because of trace left
			j -= 1 # move column left
		else :
			alSeq2.append(seq2[i-1]) # add nucl from seq2 to aligned seq2 if top is highest
			alSeq1.append("-") # add gap to aligned seq1 because of trace up
			i -= 1 # move row up
	return alSeq1, alSeq2

revAlignSeq1, revAlignSeq2 = trace_back(scoreMatrix) # gets the aligned sequences from right to left

# prints the aligned sequences
def print_seq(revAlignSeq1, revAlignSeq2) :
	alignSeq1 = revAlignSeq1[::-1] # reverse the first aligned seq
	alignSeq2 = revAlignSeq2[::-1] # reverse the second aligned seq
	alignVertical = [] # list to indicate matches
	for i in range(len(alignSeq1)):
		if alignSeq1[i] == alignSeq2[i]:
			alignVertical.append("|") # if nucl match, then |
		else:
			alignVertical.append(" ") # if nucl not match, then blank
	print ("".join(alignSeq1))
	print ("".join(alignVertical))
	print ("".join(alignSeq2))

print_seq(revAlignSeq1, revAlignSeq2)