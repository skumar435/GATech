#!/bin/bash

# gets input for the dircetory
get_input () {
	# Function for doing your getopts
    input=""
    output_dir="output/"
    gms_out_dir="output/out_gms2/"
    prod_out_dir="output/out_prod/"
    rna_out_dir="output/out_rna/"
    gff_ext=".gff"
    n_cds="_cds"
    n_rna=".rna_merge"
    n_int="_int"
    n_final="_final"
    is_gm="0"
	
	# Input: Getopts array
	# reads the command line for options and flags and executes the condition when a particular option/flag is encountered
    while getopts "i:g" comOpt
	do
		case $comOpt in
			i) input="$OPTARG";;
			g) is_gm=1;;
			*) exit 1;;
		esac
    done
    input="$input*"
}

# gets genemark exclusive genes
getGMInt () {
	for file in $input
	do
		fullname=$(basename -- "$file")
		fname="${fullname%.*}"
		bedtools intersect -f 1.0 -r -v -wa -a "$gms_out_dir$fname$gff_ext" -b "$prod_out_dir$fname$gff_ext" > "$gms_out_dir$fname$n_int$gff_ext"
	done
}

# merge the genemark exclusive genes with prodigal
mergeCDSGFF () {
	for file in $input
	do
		fullname=$(basename -- "$file")
		fname="${fullname%.*}"
		cat "$prod_out_dir$fname$gff_ext" "$gms_out_dir$fname$n_int$gff_ext" > "$output_dir$fname$n_cds$gff_ext"
	done
}

# merge the whole cds gff with the rna gff
mergeRNAGFF () {
	for file in $input
	do
		fullname=$(basename -- "$file")
		fname="${fullname%.*}"
		if [ $is_gm -eq 1 ]; then
			cat "$output_dir$fname$n_cds$gff_ext" "$rna_out_dir$fname$n_rna$gff_ext" > "$output_dir$fname$n_final$gff_ext"
		else
			cat "$prod_out_dir$fname$gff_ext" "$rna_out_dir$fname$n_rna$gff_ext" > "$output_dir$fname$n_final$gff_ext"
		fi
	done
}

main() {
	# Function that defines the order in which functions will be called
	# You will see this construct and convention in a lot of structured code.
	# calls the functions in order of execution
	get_input "$@"
	# check if genemark is used to create the gff
	if [ $is_gm -eq 1 ]; then
		getGMInt "$input" "$prod_out_dir" "$gms2_out_dir" "$gff_ext" "$n_int"
		mergeCDSGFF "$input" "$prod_out_dir" "$gms_out_dir" "$output_dir" "$gff_ext" "$n_int" "$n_cds"
	fi
	mergeRNAGFF "$input" "$rna_out_dir" "$output_dir" "$gff_ext" "$n_rna" "$n_final" "$prod_out_dir"
}

# Calling the main function
main "$@"