#!/bin/bash

# Place your gatech userame in the below export
export NAME="skumar435"

print_usage () {
echo "The following specifies the usage for the command:
Options --
-a : specifies the first reads filepath
-b : specifies the second reads filepath
-r : specifies the reference filepath
-f : specifies the mills filepath
-o : specifies the output filename without extension
Flags --
-e : realignment steps to be executed
-i : indexing step to be executed
-z : output file needs to be unzipped
-v : verbose is set on
-h : shows the usage of the command
Example : snp_pipeline.bash -a reads1 -b reads2 -r ref -f millsFile -o outputFN -ez"
}

get_input () {
	# Function for doing your getopts
    reads1="" # variable to read reads1 file path
    reads2="" # variable to read reads2 file path
    ref="" # variable to read ref file path
    output="" # variable to read output file name
    millsFile="" # variable to read mills file path
    realign="" # variable to set realignment flag
    gunzip="" # variable to set gunzip flag
    v="" # variable to set verbose flag
    index="" # variable to set index flag
    answer="" # variable to read user input
    im_file_path="" # variable to store intermediary file path
	extngz="vcf.gz" # variable to hold extension of output
	extnvcf="vcf" # variable to hold extension of unzipped output
	
	# Input: Getopts array
	# reads the command line for options and flags and executes the condition when a particular option/flag is encountered
    while getopts "a:b:r:o:f:ezvih" comOpt
	do
		case $comOpt in
			v) v=1;;
			a) reads1="$OPTARG";;
			b) reads2="$OPTARG";;
			r) ref="$OPTARG";;
			o) output="$OPTARG";;
			f) millsFile="$OPTARG";;
			e) realign=1;;
			z) gunzip=1;;
			i) index=1;;
			h) print_usage; exit 0;;
			*) exit 1;;
		esac
    done
}

check_files () {
	# Function for checking for presence of input files, reference genome,
	# and the output VCF file
	#
	# Input: File locations (string)
    # Output: True, if checks pass; False, if checks fail (bool)
	# condition to check for presence of all arguments
	if [[ $v -eq 1 ]]; then
		echo "checking for the valid filepaths..."
	fi
    if [ ! -z "$reads1" ] && [ -f "$reads1" ] && [ ! -z "$reads2" ] && [ -f "$reads2" ] && [ ! -z "$ref" ] && [ -f "$ref" ] && [ ! -z "$millsFile" ] && [ -f "$millsFile" ] && [ ! -z "$output" ]; then
		if [ -f "$output.$extngz" ] || [ -f "$output.$extnvcf" ]; then
			echo "The file exists! Do you want overwrite? [Y/n]:"
			read answer
			if [[ $answer != "Y" ]]; then
				exit 1
			fi
		fi
	return 0
    fi
    error_msg="" # variable to store all the missing file messages
	# checks for the reads1 file
    if [ -z "$reads1" ] || [ ! -f "$reads1" ]; then
		error_msg="$error_msg\nreads1 file is missing"
		#echo "reads1 file is missing"
		#exit 1
	fi
    # checks for the reads2 file
	if [ -z "$reads2" ] || [ ! -f "$reads2" ]; then
		error_msg="$error_msg\nreads2 file is missing"
		#echo "reads2 file is missing"
		#exit 1
    fi
	# checks for the ref file
    if [ -z "$ref" ] || [ ! -f "$ref" ]; then
		error_msg="$error_msg\nref file is missing"
		#echo "ref file is missing"
		#exit 1
    fi
	# checks for the mills file
    if [ -z "$millsFile" ] || [ ! -f "$millsFile" ]; then
		error_msg="$error_msg\nmills file is missing"
		#echo "mills file is missing"
		#exit 1
    fi
	# checks for the output file
    if [ -z "$output" ]; then
		echo "No output filename provided! Do you want to use default? [Y/n]:"
		read answer
		if [[ $answer != "Y" ]]; then
			error_msg="$error_msg\noutput file not provided"
		else
			output="default"
			return 0
		fi
    fi
	#checks if error_msg is null
	if [ ! -z "$error_msg" ]; then
		printf "$error_msg\n"
		exit 1
	fi
}

prepare_temp () {
	# Preparing your temporary directory
	# checks for tmp and makes it
    # checks for tmp/lane_temp and makes it
    if [[ $v -eq 1 ]]; then
		echo "creating the temp directories..."
	fi
	mkdir -p tmp/
    mkdir -p tmp/lane_temp/
}


mapping () {
	# Function for the mapping step of the SNP-calling pipeline
	#
	# Input: File locations (string), Verbose flag (bool)
	# Output: File locations (string)
	if [[ $v -eq 1 ]]; then
		echo "mapping the reads files..."
	fi
    #bwa index $ref # index the ref file
    bwa mem -R '@RG\tID:foo\tSM:bar\tLB:library1' $ref $reads1 $reads2 > tmp/lane.sam # generates the sam file using reads and ref
    im_file_path="tmp/lane.sam"
    samtools fixmate -O bam tmp/lane.sam tmp/lane_fixmate.bam # generates the bam file using the sam file
    im_file_path="tmp/lane_fixmate.bam"
    samtools sort -O bam -o tmp/lane_sorted.bam -T tmp/lane_temp tmp/lane_fixmate.bam # sorts the bam file
    im_file_path="tmp/lane_sorted.bam"
}

improvement () {
	# Function for improving the number of miscalls
	#
	# Input: File locations (string)
	# Output: File locations (string)
	if [[ $v -eq 1 ]]; then
		echo "improvement process starts..."
	fi
    #samtools faidx $ref # generates the index file for ref
    #refWoExt=$("$ref")
    #refWoExtn="${ref%.*}" # extracts the path without extension for the ref file
    #java -jar lib/picard-tools-1.74/CreateSequenceDictionary.jar R=$ref O=$refWoExtn.dict # generates the sequence dictionary for the ref file
    samtools index tmp/lane_sorted.bam # indexes the bam file before realignment
    if [[ $realign -eq 1 ]]; then # checks for the realignment flag and execute realignment
		java -Xmx2g -jar lib/GenomeAnalysisTK.jar --log_to_file skumar435_1.log -T RealignerTargetCreator -R $ref -I tmp/lane_sorted.bam -o tmp/lane.intervals --known $millsFile
		im_file_path="tmp/lane.intervals"
		java -Xmx4g -jar lib/GenomeAnalysisTK.jar --log_to_file skumar435_2.log -T IndelRealigner -R $ref -I tmp/lane_sorted.bam -targetIntervals tmp/lane.intervals -known $millsFile -o tmp/lane_realigned.bam
		im_file_path="tmp/lane_realigned.bam"
    fi
	if [[ $index -eq 1 ]]; then # checks for the indexing flag and executes the indexing
		samtools index $im_file_path
	fi
}

call_variants () {
	# Function to call variants
	#
	# Input: File locations (string)
    # Ouput: None
	if [[ $v -eq 1 ]]; then
		echo "varain tcalling process starts..."
	fi
	mkdir -p output/ # creates output directory if not present
	# generates the output zipped vcf file	
    bcftools mpileup -Ou -f $ref $im_file_path | bcftools call -vmO z -o output/$output.$extngz
    # checks for the guzip flag to extract the vcf from the zipped file
    if [[ $gunzip -eq 1 ]]; then
		gunzip -c output/$output.$extngz > output/$output.$extnvcf
    fi
}

main() {
	# Function that defines the order in which functions will be called
	# You will see this construct and convention in a lot of structured code.
	# calls the functions in order of execution
	get_input "$@"
	check_files "$ref" "$reads1" "$reads2" "$millsFile" "$output"
	prepare_temp
	mapping "$ref" "$reads1" "$reads2"
	#if [[ $realign -eq 1 ]]; then # checks for the realignment flag and execute
	improvement "$ref" "$millsFile"
	#fi
	call_variants "$ref" "$output"
}

# Calling the main function
main "$@"


# DO NOT EDIT THE BELOW FUNCTION
#bats_test (){
#    command -v bats
#}
# DO NOT EDIT THE ABOVE FUNCTION