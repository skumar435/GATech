import sys
import os
import re
import subprocess

prot_tr = { "TTT": "F", "TCT": "S", "TAT": "Y", "TGT": "C",  
			"TTC": "F", "TCC": "S", "TAC": "Y", "TGC": "C",  
			"TTA": "L", "TCA": "S", "TAA": "*", "TGA": "*",  
			"TTG": "L", "TCG": "S", "TAG": "*", "TGG": "W",  

			"CTT": "L", "CCT": "P", "CAT": "H", "CGT": "R",  
			"CTC": "L", "CCC": "P", "CAC": "H", "CGC": "R",  
			"CTA": "L", "CCA": "P", "CAA": "Q", "CGA": "R",  
			"CTG": "L", "CCG": "P", "CAG": "Q", "CGG": "R",  

			"ATT": "I", "ACT": "T", "AAT": "N", "AGT": "S",  
			"ATC": "I", "ACC": "T", "AAC": "N", "AGC": "S",  
			"ATA": "I", "ACA": "T", "AAA": "K", "AGA": "R",  
			"ATG": "M", "ACG": "T", "AAG": "K", "AGG": "R",  

			"GTT": "V", "GCT": "A", "GAT": "D", "GGT": "G",  
			"GTC": "V", "GCC": "A", "GAC": "D", "GGC": "G",  
			"GTA": "V", "GCA": "A", "GAA": "E", "GGA": "G",  
			"GTG": "V", "GCG": "A", "GAG": "E", "GGG": "G" }

def generateGlimOP(argDir):
	contigFileNames = []
	for file in os.listdir(argDir):
		if os.path.isfile(argDir + file):
			contigFN = file.split(".")[0]
			subprocess.run(["glimmer3.02/scripts/g3-from-scratch.csh", argDir + file, contigFN])
			contigFileNames.append(contigFN + ".predict")
	subprocess.run(["mkdir", "-p", "./temp/"])
	for file in contigFileNames:
		subprocess.run(["mv", file, "./temp/"])
	return contigFileNames

def convertToGFF(content):
	header = ""
	formatted_content = []
	for line in content:
		if line.startswith(">"):
			header = line[1:].rstrip()
			formatted_content.append(line.replace(">", "#"))
		else:
			line_format = line.split()
			if int(line_format[2]) < int(line_format[1]):
				formatted_content.append("{}\tGLIMMER\tgene\t{}\t{}\t{}\t{}\t{}\tID={}\n".format(header,line_format[2],line_format[1],line_format[4],line_format[3][0],line_format[3][1:],line_format[0]))
			else:
				formatted_content.append("{}\tGLIMMER\tgene\t{}\t{}\t{}\t{}\t{}\tID={}\n".format(header,line_format[1],line_format[2],line_format[4],line_format[3][0],line_format[3][1:],line_format[0]))
	return formatted_content

def convertToFAA(content):
	formatted_content = []
	for line in content:
		if line.startswith(">"):
			formatted_content.append(line)
		else:
			i = 0
			prot_seq = ""
			while i < (len(line.rstrip()) - 3):
				prot_seq += prot_tr[line[i:i+3]]
				i = i + 3
				if prot_seq[-1] == "*":
					break
			formatted_content.append(prot_seq[:-1] + "\n")
	return formatted_content

def readWriteFile(fileName, isGFF):
	with open(fileName, 'r') as frh:
		pr_file_content = frh.readlines()
		new_content = ""
		writeFName = ""
		if isGFF:
			new_content = convertToGFF(pr_file_content)
			writeFName = fileName.split(".")[0] + ".gff"
		else:
			new_content = convertToFAA(pr_file_content)
			writeFName = fileName.split(".")[0] + ".faa"
		with open(writeFName, 'w') as fwh:
			fwh.writelines(new_content)

def convertAllToGFF(contNames):
	for file in contNames:
		readWriteFile("temp/" + file, True)

def convertAllToFAA(contNames):
	for file in contNames:
		readWriteFile("glim_out/" + file.split(".")[0] + ".fna", False)

def generateFNA(argDir):
	for file in os.listdir(argDir):
		if os.path.isfile(argDir + file):
			cFN = "glim_out/" + file.split(".")[0]
			subprocess.run(["bedtools", "getfasta", "-fi", argDir + file, "-bed", cFN + ".gff", "-fo", cFN + ".fna"])

def main():
	argDir = sys.argv[1]
	glim_files = generateGlimOP(argDir)
	subprocess.run(["mkdir", "-p", "./glim_out/"])
	convertAllToGFF(glim_files)
	generateFNA(argDir)
	convertAllToFAA(glim_files)

main()