#!/usr/bin/env python3

import sys
import os
import re
import subprocess
import argparse
from scripts.prodigal_script import prodigal
from scripts.genemarkS2 import genemarkS2
from scripts.RNAsearch import RNApredict

# creates the output directories for the output of prodigal
def createProdOutDirs():
	if not os.path.exists(os.getcwd()+"/output/"):
		os.makedirs(os.getcwd()+"/output")
	if not os.path.exists(os.getcwd()+"/output/out_prod/"):
		os.makedirs(os.getcwd()+"/output/out_prod")
	if not os.path.exists(os.getcwd()+"/output/out_prod/prot"):
		os.makedirs(os.getcwd()+"/output/out_prod/prot")
	if not os.path.exists(os.getcwd()+"/output/out_prod/nucl"):
		os.makedirs(os.getcwd()+"/output/out_prod/nucl")

# creates the op dirs for output of gene mark s2
def createGMOutDirs():
	if not os.path.exists(os.getcwd()+"/output/out_gms2/"):
		os.makedirs(os.getcwd()+"/output/out_gms2")
	if not os.path.exists(os.getcwd()+"/output/out_gms2/prot"):
		os.makedirs(os.getcwd()+"/output/out_gms2/prot")
	if not os.path.exists(os.getcwd()+"/output/out_gms2/nucl"):
		os.makedirs(os.getcwd()+"/output/out_gms2/nucl")

# get the intersection genes from prodigal output
# def getProdIntGene(argDir):
# 	gm_out_dir = "./output/out_gms2/"
# 	prod_out_dir = "./output/out_prod/"
# 	for file in argDir:
# 		fName = file.split(".")[0] + ".gff"
# 		nFName = file.split(".")[0] + "_int1" + ".gff"
# 		oFName = file.split(".")[0] + "_int2" + ".gff"
# 		subprocess.run(['bedtools', 'intersect', '-f', '1.0', '-r', '-v', '-wa', '-a', prod_out_dir+fName, '-b', gm_out_dir+fName, '>', prod_out_dir+nFName])
# 		subprocess.run(['bedtools', 'intersect', '-f', '1.0', '-r', '-wa', '-a', prod_out_dir+fName, '-b', gm_out_dir+fName, '>', prod_out_dir+oFName])

# get intersection genes from genemark op
def getGMIntGene(argDir):
	gm_out_dir = "./output/out_gms2/"
	prod_out_dir = "./output/out_prod/"
	for file in os.listdir(argDir):
		fName = file.split(".")[0] + ".gff"
		nFName = file.split(".")[0] + "_int" + ".gff"
		subprocess.run(['bedtools', 'intersect', '-f', '1.0', '-r', '-v', '-wa', '-a', gm_out_dir+fName, '-b', prod_out_dir+fName, '>', gm_out_dir+nFName])

# gets the union of the genes from prodigal and gene mark
def mergeGFF(argDir):
	out_dir = "./output/"
	gm_out_dir = "./output/out_gms2/"
	prod_out_dir = "./output/out_prod/"
	for file in os.listdir(argDir):
		fName = out_dir + file.split(".")[0] + "_cds" + ".gff"
		fName1 = gm_out_dir + file.split(".")[0] + "_int" + ".gff"
		fName2 = prod_out_dir + file.split(".")[0] + ".gff"
		# fName3 = prod_out_dir + file.split(".")[0] + "_int2" + ".gff"
		subprocess.run(['cat', fName1, fName2, '>', fName])

# merges the genes with the rna content generated
def mergeRNAGFF(argDir, isGeneMark):
	if isGeneMark:
		subprocess.run(['./scripts/gene_pred_merge.sh', '-g', '-i', argDir])
	else:
		subprocess.run(['./scripts/gene_pred_merge.sh', '-i', argDir])

def main():
	parser = argparse.ArgumentParser(description='Gene Prediction tool')
	parser.add_argument('-i', '--input',  help='Directory containing input genomes files (.fasta)', type=str, required=True)
	parser.add_argument('-f', '--format', help='Output Format (gff, gbk, sqn, sco)', default='gff', type=str)
	parser.add_argument('-g', '--genemark', help='Optional arg for using genemark', action='store_true')
	parser.add_argument('-q', '--quiet', help='Flag to suppress verbose out for individual programs', action='store_true')
	parser.add_argument('-v', '--verbose', help='Flag to display verbose for pipeline', action='store_true')
	args = parser.parse_args()
	# output dir for the rna results
	out_dir_RNA = "./output/out_rna/"
	#if gene mark need to be run on the contigs
	if args.genemark:
		if args.verbose:
			print("Creating directories for GMS2 output")
		createGMOutDirs()
		if args.verbose:
			print("Creating directories for Prodigal output")
		createProdOutDirs()
		gm_out_dir = "./output/out_gms2/"
		prod_out_dir = "./output/out_prod/"
		for file in os.listdir(args.input):
			if os.path.isfile(args.input + file):
				if args.verbose:
					print("Starting GMS2 for {}".format(file))
				genemarkS2(args.input + file, gm_out_dir+file.split(".")[0], gm_out_dir+"nucl/"+file.split(".")[0], gm_out_dir+"prot/"+file.split(".")[0], args.quiet)
				if args.verbose:
					print("Starting Prodigal for {}".format(file))
				prodigal(args.input + file, prod_out_dir+file.split(".")[0], prod_out_dir+"nucl/"+file.split(".")[0], prod_out_dir+"prot/"+file.split(".")[0], args.quiet)
		# if args.verbose:
		# 	print("Getting prodigal gene intersects")
		# getProdIntGene(args.input)
		# if args.verbose:
		# 	print("Getting gene mark gene intersects")
		# getGMIntGene(args.input)
		# if args.verbose:
		# 	print("Generating gene's union")
		# mergeGFF(args.input)
	else:
		if args.verbose:
			print("Creating directories for Prodigal output")
		createProdOutDirs()
		prod_out_dir = "./output/out_prod/"
		for file in os.listdir(args.input):
			if os.path.isfile(args.input + file):
				if args.verbose:
					print("Starting Prodigal for {}".format(file))
				prodigal(args.input + file, prod_out_dir+file.split(".")[0], prod_out_dir+"nucl/"+file.split(".")[0], prod_out_dir+"prot/"+file.split(".")[0], args.quiet)
	if args.verbose:
		print("Generating RNA files")
	RNApredict(args.input)
	if args.verbose:
		print("Merging RNA and CDS results")
	mergeRNAGFF(args.input, args.genemark)

if __name__ == "__main__":
	main()