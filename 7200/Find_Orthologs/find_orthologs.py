#!/usr/bin/env python3

'''
Script for finding orthologs using reciprocal BLAST hits.

You *must* use the import statements at the end of this docstring. You may choose
to import any of the other allowed modules.

You have to write an argparse for getting command line arguments. The usage for
this script is:
    ./find_orthologs.py -i1 <Input file 1> -i2 <Input file 2> -o <Output file name> –t <Sequence type – n/p>

where "n" specifies a nucleotide sequence and "p" specifies a protein sequence.
'''
import sys
import argparse
import subprocess

from blast_utilities.orthologs import get_reciprocal_hits


def main():
    '''
    This is the main function.
    '''
    
    '''
    Insert argparse code that populates the following variables
     - file_one
     - file_two
     - output_file
     - input_sequence_type
    '''
    parser = argparse.ArgumentParser(prog='Find orthologs', prefix_chars='-')
    parser.add_argument('-i1', help="input file1")
    parser.add_argument('-i2', help="input file2")
    parser.add_argument('-o', help="output file")
    parser.add_argument('-t', help="type of sequence")
    args = parser.parse_args()

    file_one = args.i1
    file_two = args.i2
    output_file = args.o
    input_sequence_type = args.t

    '''
    output_list is a list of reciprocal BLAST hits. Each element is a tab
    separated pair of gene names. Eg:
    ["lcl|AM421808.1_cds_CAM09336.1_10	lcl|AE002098.2_cds_NMB0033_33", "lcl|AM421808.1_cds_CAM09337.1_11	lcl|AE002098.2_cds_NMB0034_34", "lcl|AM421808.1_cds_CAM09338.1_12	lcl|AE002098.2_cds_NMB0035_35", "lcl|AM421808.1_cds_CAM09339.1_13	lcl|AE002098.2_cds_NMB0036_36", ...]
    '''
    output_list = get_reciprocal_hits(file_one, file_two, input_sequence_type)
    with open(output_file, 'w') as output_fh:
        for ortholog_pair in output_list:
            output_fh.write(ortholog_pair+"\n")

if __name__ == "__main__":
    main()
