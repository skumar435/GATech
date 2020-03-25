# Calculates the genomic distance using kMer based Mash distancing

This script has the usage:
~ genomeDistance.py 
with following arguments:
mandatory:  '-a', "An input genome"
	          '-b', "Another input genome"
	          '-d', '--dir', "Directory containing genome files" (only if 'a/b' is a directory)
            '-S', '--seed', "Seed value for random set generation"
optional:   '-s', '--setsize', "Number of random k-mer to evaluate", default=1000, type=int
	          '-o', '--output', "Output file name", default="genomeDist.txt"
	          '-t', '--threads', "Number of threads to run", default=1, type=int
	          '-v', '--verbose', "Verbose mode"
            '-f', '--force', "Overwrite file if exists"
