#!/usr/bin/env python

import sys
import random

# reads the content of the input file and returns the list of genes with anc values
def readFile(fName) :
	fHand = open(fName, 'r')
	data = fHand.read().splitlines() # splits the lines
	geneList = {}
	for i in range(1,len(data)) :
		geneList[data[i].split()[0]] = data[i].split()[1:] # add the  list of ancestory values to the specific gene
	return geneList

# randomises the ancestory values for a gene and returns the randomised list
def shuffleGeneList(geneList) :
	originalList = geneList	
	geneList = random.sample(range(len(geneList)), len(geneList)) # randomises the indices of the observed list
	for i in range(len(geneList)) :
		geneList[i] = originalList[geneList[i]] # assigns the ancestory value based on the index at the observed list
	return geneList

# calculates the homozygosity for a particular list of genes
def calcHZ(geneList) :
	hzGeneCount = 0
	i = 0
	while i < len(geneList) :
		geneSub = geneList[i:i+2] # compare a pair of chromosomes for homozygosity
		if geneSub[0] == geneSub[1] :
			hzGeneCount += 1 # add the homozygous count
		i += 2 # skip to the next pair
	return ((hzGeneCount*2)/len(geneList))

# calculates the mean for a list
def calcMean(hzList) :
	return sum(hzList)/len(hzList)

# calculates the standard deviation for a list
def calcSD(hzList, hzMean) :
	hzSD = 0
	for item in hzList :
		hzSD += (item-hzMean)**2
	return (hzSD/len(hzList))**(0.5)

# prints the tab separated result to output.txt file
def printOut(fname, usContent) :
	sortedContent = []
	sortedContent.append("Gene\tObserved\tPermuted_mean\tPermuted_sd\n")
	for gene in usContent :
		sortedContent.append("{}\t{}\t{}\t{}\n".format(gene, usContent[gene][0], usContent[gene][1], usContent[gene][2]))
	with open(fname, 'w') as fWHand :
		fWHand.writelines(sortedContent)

# main function to handle functional operations
def main() :
	ipFileName = sys.argv[1] # gets the i/p file name
	opFileName = sys.argv[2] # gets the o/p file name
	seed = int(sys.argv[3]) # gets the seed value for randomising
	permNum = int(sys.argv[4]) # gets the number of permutations to be done for the sample
	random.seed(seed) # initiates the seed value for prg
	gList = readFile(ipFileName)
	hzObserved = {}
	gHZList = {}
	for gene in gList :
		hzObserved[gene] = calcHZ(gList[gene]) # calculates the hz for the observed values
		gHZList[gene] = []
		for i in range(permNum) :
			shuffledList = shuffleGeneList(gList[gene]) # generates the randomised list of ancestory
			hzShuffle = calcHZ(shuffledList) # calculate the hz
			gHZList[gene].append(hzShuffle) # add the hz to the gene list
		geneMean = calcMean(gHZList[gene]) # calculate the mean for the permutations
		geneSD = calcSD(gHZList[gene], geneMean) # calculate the sd for the permutations
		gHZList[gene] = [round(hzObserved[gene], 2), round(geneMean,2), round(geneSD,2)] # add the contents to a dictionary
	printOut(opFileName, gHZList)

main()
