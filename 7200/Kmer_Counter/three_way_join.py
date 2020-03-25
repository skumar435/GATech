# Week 6
# Q2.
import sys

knownGeneFile = sys.argv[1]
refFile = sys.argv[2]
ifDiseaseFile = sys.argv[3]
kgFileHandle = open(knownGeneFile, 'r')
refFileHandle = open(refFile, 'r')
idFileHandle = open(ifDiseaseFile, 'r')
idGenes = idFileHandle.readlines()[1:]
geneID = {}
geneData = []
refID = refFileHandle.readlines()

def getID() :
	for iGene in idGenes :
		i = 0
		while i< len(refID) :
			if iGene.rstrip() == refID[i].split("\t")[4] :
				geneID[iGene.rstrip()] = refID[i].partition("\t")[0]
				break
			i += 1

getID()

knownGeneData = kgFileHandle.readlines()

def getDetails() :
	for geneName in geneID :
		i = 0
		while i < len(knownGeneData) :
			if geneID[geneName] == knownGeneData[i].partition("\t")[0] :
				geneData.append([geneName,knownGeneData[i].split("\t")[1],knownGeneData[i].split("\t")[3],knownGeneData[i].split("\t")[4]])
				break
			i += 1

getDetails()

def printDetails() :
	print ("Gene\tChr\tStart\tStop")
	for geneDet in geneData :
		print ("{}\t{}\t{}\t{}".format(geneDet[0],geneDet[1],geneDet[2],geneDet[3]))

printDetails()