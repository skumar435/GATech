#!/usr/bin/env python
 
import sys
import re

emblRe = re.compile(r"^ID") # regex to identify embl format file
gbRe = re.compile(r"^LOCUS") # regex to identify gb format file
fastqRe = re.compile(r"^@") # regex to identify fastq format file
megaRe = re.compile(r"^#") # regex to identify mega format file

# function to read the file contents
def readFile() :
	with open(sys.argv[1], 'r') as fileHandler :
		fileContent = fileHandler.readlines()
	return fileContent

# function to convert the sequences info from embl and gb to fasta format
def toFasta(sequences, fileContent) :
	fastaContent = []
	# loops through the sequence information retrieved from gb or embl files
	for seq in sequences :
		fastaContent.append(seq) # appends the sequence start line
		for lines in range(sequences[seq][0], sequences[seq][1]) :
			fastaContent.append(re.sub("[\s*\d]", "", fileContent[lines].upper())) # appends the sequence from the start to end line while substituting spaces and digits
			fastaContent.append("\n")
	return fastaContent

# retrieves info from embl file for sequences
def convertEmbl(fileContent) :
	seqIDIndices = {}
	seqID = ""
	seqVer = 0
	seqDef = ""
	startIndex = 0
	stopIndex = 0
	for line in fileContent :
		if re.match(emblRe, line) :
			seqID = line.rstrip().split()[1][:-1] # splits the ID line and gets the ID
			if re.match(r".*SV", line) :
				seqVer = re.search(r"SV(.+?);", line).group(1).lstrip() # searches for the Sequence version and gets it
		elif re.match(r"^DE", line) :
			seqDef = line.rstrip().split(maxsplit = 1)[1] # gets the definition part
		elif re.match(r"^SQ", line) :
			startIndex = fileContent.index(line) + 1 # gets the start line index for sequence
		elif re.match(r"^//", line) :
			stopIndex = fileContent.index(line) # gets the stop line index for sequence
			seqIDIndices[">ENA|{}|{}.{} {}\n".format(seqID, seqID, seqVer, seqDef)] = [startIndex, stopIndex] # adds to dictionary with seq info in fasta format
	return toFasta(seqIDIndices, fileContent)

# retrieves info from gb file for sequences
def convertGb(fileContent) :
	seqIDIndices = {}
	seqID = ""
	seqDef = ""
	startIndex = 0
	stopIndex = 0
	line = 0
	while line < len(fileContent) :
		if re.match(r"^VERSION", fileContent[line]) :
			# splits the version line and gets the version
			seqID = fileContent[line].rstrip().split()[1]
		elif re.match(r"^DEFINITION", fileContent[line]) :
			# gets the definition part
			seqDef = fileContent[line].rstrip().split(maxsplit = 1)[1]
		elif re.match(r"^ORIGIN", fileContent[line]) :
			# gets the start line index for sequence
			startIndex = line + 1
		elif re.match(r"^//", fileContent[line]) :
			# gets the stop line index for sequence
			stopIndex = line
			seqIDIndices[">{} {}\n".format(seqID, seqDef)] = [startIndex, stopIndex] # adds to dictionary with seq info in fasta format
		line += 1
	return toFasta(seqIDIndices, fileContent)

# converts the fastq content to fasta
def convertFastq(fileContent) :
	fastaContent = []
	lineNum = 0
	# iterates through the file looking for start of sequences
	while lineNum < len(fileContent) :
		if re.match(fastqRe, fileContent[lineNum]) :
			fastaContent.append(re.sub("@", ">", fileContent[lineNum])) # replaces the @ with > and appends to fasta content
			fastaContent.append(fileContent[lineNum+1]) # gets the next line and appends the seq to content
			lineNum += 2 # skips 2 current lines to look for next sequence as they have been covered
		else :
			lineNum += 1 # skips one line in case new sequence not encountered
	return fastaContent

# converts the mega sequential content to fasta
def convMegaSeq(fileContent) :
	fastaContent = []
	seqID = ""
	for line in fileContent :
		if re.match(r"^#(?!mega|MEGA)", line) :
			fastaContent.append(re.sub("#", ">", line)) # in case of a sequence start replace the # with >
			seqID = re.sub("#", "", line.rstrip()) # store to associate seq with id
		else :
			if seqID :
				fastaContent.append(line) # if current seq id is being parsed, add the next lines to the sequence data
	return fastaContent

# converts the mega interleaved data to fasta
def convMegaIL(fileContent) :
	fastaContent = []
	seqID = {} # dictionary to store the seqid and sequences
	for line in fileContent :
		if re.match(r"^#(?!mega|MEGA)", line) :
			seq = line[1:].split()
			if seq[0] not in seqID :
				seqID[seq[0]] = [seq[1]+"\n"] # add the new seqid encountered with the first line of sequence
			else :
				seqID[seq[0]].append(seq[1]+"\n") # if seqid already encountered, add the sequence lines to existing list of sequences
	for item in seqID :
		fastaContent.append(">"+item+"\n") # convert to fasta start line with > append and add to content
		fastaContent.extend(seqID[item]) # add all the lines for a particular id to the content
	return fastaContent

# retrieves the fasta content for mega file
def convertMega(fileContent) :
	for line in fileContent :
		if re.match(r"^#(?!mega|MEGA)", line) :
			if re.match(r"^#(?!mega|MEGA)", fileContent[fileContent.index(line)+1]) :
				return convMegaIL(fileContent) # checks for interleaved data and calls the apt function
			else :
				return convMegaSeq(fileContent) # checks for sequential or noninterleaved data and calls the apt function

# determines the format f the input file based on the start line format
def determineFormat(fileContent) :
	if re.match(emblRe, fileContent[0]) :
		return convertEmbl(fileContent)
	elif re.match(gbRe, fileContent[0]) :
		return convertGb(fileContent)
	elif re.match(fastqRe, fileContent[0]) :
		return convertFastq(fileContent)
	elif re.match(megaRe, fileContent[0]) :
		return convertMega(fileContent)
	else :
		print ("Format not recognised!")

# writes the fasta content retrieved for each file type to a new file
def writeToFile(fastaCont, fileName) :
	with open(fileName, 'w') as fastaFile :
		fastaFile.writelines(fastaCont)

# main fucntion to handle all functions
def main() :
	content = readFile() # reads the content of input file
	writableContent = determineFormat(content) # retrieves the content to be written to output
	fileWithExt = sys.argv[1].split(".") # splits the input filename to get extension, if any
	if re.match(r"^[ACGTNacgtn]+$", writableContent[1].rstrip()) :
		if len(fileWithExt) != 1 :
			fileWithExt[-1] = "fna" # replace with fna if extension present for nucleotide sequences
		else :
			fileWithExt.append("fna") # add fna if extension not present for nucleotide sequences
	else :
		if len(fileWithExt) != 1 :
			fileWithExt[-1] = "faa" # replace with faa if extension present for amino acid sequences
		else :
			fileWithExt.append("faa") # add faa if extension not present for amino acid sequences
	writeToFile(writableContent, ".".join(fileWithExt)) # write the file contents to apt output file

main()