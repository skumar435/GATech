#!/usr/bin/env python3

import sys
import argparse
import re
import os
import random
import threading
import multiprocessing

def argumentProcess():
	parser = argparse.ArgumentParser(prog='GenomeDistance', prefix_chars='-')
	parser.add_argument('-a', help="An input genome")
	parser.add_argument('-b', help="Another input genome")
	parser.add_argument('-d', '--dir', help="Directory containing genome files")
	parser.add_argument('-s', '--setsize', help="Number of random k-mer to evaluate", default=1000, type=int)
	parser.add_argument('-S', '--seed', help="Seed value for random set generation")
	parser.add_argument('-o', '--output', help="Output file name", default="genomeDist.txt")
	parser.add_argument('-t', '--threads', help="Number of threads to run", default=1, type=int)
	parser.add_argument('-v', '--verbose', help="Verbose mode")
	parser.add_argument('-f', '--force', help="Overwrite file if exists", action="store_true")
	args = parser.parse_args()
	return args

def fileRead(fileContent):
	