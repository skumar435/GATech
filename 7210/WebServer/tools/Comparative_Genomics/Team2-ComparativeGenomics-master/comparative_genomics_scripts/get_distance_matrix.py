#!/projects/VirtualHost/predictb/tools/bin/bin/python3.7
# -*- coding: utf-8 -*-

import argparse, os, subprocess
import math

from multiprocessing import Pool


parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-d', '--dir', help='Directory containing reference genomes files', type=str, required=True)
requiredNamed.add_argument('-i', '--input', help='Directory containing input fasta file', type=str, required=True)
parser.add_argument('-o', '--output', help='Output file name, default to “distances.csv” if -o is provided with no additional strings. If -o is not provided,write to STDOUT', const='distance_matrix.csv', nargs='?', type=str)
parser.add_argument('-t', '--threads', help='Number of theads/processes to run the analysis, defaults to 1', default=1, type=int, nargs='?')
# parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')

args = parser.parse_args()

root_dir = args.dir
in_dir = args.input

in_file = os.listdir(in_dir)
files = os.listdir(root_dir)
files = [file for file in files if file.endswith('.fasta') ]
in_file = [file for file in in_file if file.endswith('.fasta')]

rarray = []

temp_dir = os.path.join(root_dir, 'temp')
subprocess.run(['mkdir', temp_dir])

def get_distance(file1, file2):
	
	f1 = file1.split('/')[-1].split('.')[0]
	f2 = file2.split('/')[-1].split('.')[0]

	print (f1)
	subprocess.run(['dnadiff', '-p', temp_dir+'/'+f1+f2, file1, file2])

	with open(temp_dir+'/'+f1+f2+'.report', 'r') as f:
		for line in f:
			if line.startswith('AvgIdentity'):
				distance = float(line.strip().split()[1])
				return [f1, f2, 100.0-distance]

# User supplies an empty directory for -d
if args.dir != None and len(os.listdir(args.dir) ) == 0:
    with Exception as e5:
    	raise e5

# Threads are positive integer values
if args.threads != None and args.threads <= 0:
	with Exception as e7:
		raise e7

pool = Pool(args.threads)

if args.dir != None and args.input != None:
	#temp = []
	#temp.append(['\t'])
	#for file in files:
	#	temp[0].append(file)
	#for file1 in files:
	#	t = []
	#	t.append(file1)
	#	for file2 in files:
	#		if file1 == file2:
	#			t.append(0.0)
	#			continue
	#		t.append([os.path.join(root_dir, file1), os.path.join(in_dir, file2)])
	#	temp.append(t)
	arr = []
	for file in files:
	        arr.append([os.path.join(in_dir, in_file[0]), os.path.join(root_dir, file)])
	print(arr)            
	res = pool.starmap(get_distance, arr)
	

	# for i in range(len(temp)):
	#     for j in range(len(temp)):
	#         if i != 0 and j != 0 and i < j:
	#             temp[i][j] = temp[j][i] = res.pop()
	# for row in temp:
	# 	rarray.append(','.join(str(val) for val in row))

subprocess.run(['rm', '-r', temp_dir])

if not args.output:
	print (rarray)
else:
	if os.path.isfile(os.path.join(root_dir, args.output)):
		with open(args.output, 'w') as op:
			rstring = ''
			for row in res:
				rstring += ",".join(str(x) for x in row) + '\n'
			op.write(rstring)	
	else:
		with open(os.path.join(root_dir, args.output), 'w') as op:
			rstring = ''
			for row in res:
				rstring += ",".join(str(x) for x in row) + '\n'
			op.write(rstring)
