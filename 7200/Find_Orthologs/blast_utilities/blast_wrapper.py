#!/usr/bin/env python3

'''
Define different blast wrapper functions here.
'''

import sys
import subprocess
import os

def genBlastDB(fname1, fname2, filetype):
	ftype = ""
	if filetype == "n":
		ftype = "nucl"
	else:
		ftype = "prot"
	subprocess.run(["makeblastdb", "-in", fname1, "-dbtype", ftype])
	subprocess.run(["makeblastdb", "-in", fname2, "-dbtype", ftype])

def runBlast(fname1, fname2, filetype):
	cmd = ""
	intOut1 = "f1tof2.out"
	intOut2 = "f2tof1.out"
	if filetype == "n":
		cmd = "blastn"
		subprocess.run([cmd, "-db", fname2, "-query", fname1, "-evalue", "0.05", "-qcov_hsp_perc", "70", "-perc_identity", "75", "-max_target_seqs", "1", "-outfmt", "6", "-out", intOut1])
		subprocess.run([cmd, "-db", fname1, "-query", fname2, "-evalue", "0.05", "-qcov_hsp_perc", "70", "-perc_identity", "75", "-max_target_seqs", "1", "-outfmt", "6", "-out", intOut2])
	else:
		cmd = "blastp"
		subprocess.run([cmd, "-db", fname2, "-query", fname1, "-evalue", "0.05", "-qcov_hsp_perc", "70", "-max_target_seqs", "1", "-outfmt", "6", "-out", intOut1])
		subprocess.run([cmd, "-db", fname1, "-query", fname2, "-evalue", "0.05", "-qcov_hsp_perc", "70", "-max_target_seqs", "1", "-outfmt", "6", "-out", intOut2])
	return intOut1, intOut2