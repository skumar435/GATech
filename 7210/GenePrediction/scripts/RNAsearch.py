#!/usr/bin/env python3

from subprocess import Popen, PIPE

import re, os

'''Infernal detects ncRNA from Rfam'''

def INFERNAL2GFF3(INFERNAL_output):
    INFERNAL_output_gff = INFERNAL_output + '.gff'
    f = open(INFERNAL_output_gff,'w')
    process = Popen(args=['awk', r'BEGIN {print "##gff-version 3"} NR>2{if($8 < $9 && $8 > 0) printf "%s\tinfernal\tmisc_RNA\t%d\t%d\t.\t%s\t.\tID=%s_infernal_%s_%s;Name=%s\n" ,$3,$8,$9,$10,$3,$8,$9,$1}',INFERNAL_output], 
                   stdout = f, stderr = PIPE)
    stdout, stderr = process.communicate()
    del stdout,stderr

def INFERNAL (input_file,database_path,output_file,cpu_cores):
    process = Popen(args = ['cmscan',
                            '-E','1e-06',
                            '--rfam',               # set heuristic filters at Rfam-level (fast)
                            '--cpu', cpu_cores,     # number of parallel CPU workers to use for multithreads
                            '--tblout',output_file, # save parseable table of hits to file <s>
                            '--noali',              # don't output alignments, so output is smaller
                            database_path,          # Using the Rfam 12.0 bacteria databases
                            input_file],            # Input raw genome assembly file
                            stdout = PIPE, stderr = PIPE)

    stdout, stderr = process.communicate()
    del stdout,stderr

    INFERNAL2GFF3(output_file)

''' ARAGORN detects tRNA, mtRNA, and tmRNA genes
    By default, all RNA gene types above will be searched'''

def ARAGORN2GFF3(ARAGORN_output):
    # For robust use, the path should be specified
    ARAGRON_output_gff = ARAGORN_output + '.gff'
    f = open(ARAGRON_output_gff,'w')
    
    process = Popen(args = ['perl',                 # It's a perl script that use perl to run   
                            'cnv_aragorn2gff.pl',   # The script needs to be in current directory or we can add path for it
                            '-i', ARAGORN_output,   # Input file name          
                            '-gff-ver=3'],           # Print out in batch mode, which can be applied for gff convertation
                            stdout = f, stderr = PIPE)

    stdout, stderr = process.communicate()
    del stdout,stderr

def ARAGORN (input_file,output_file):
    process = Popen(args = ['aragorn',              
                            '-l',                   # Assume that each sequence has a linear topology.
                            '-gc1',                 # Use the GenBank transl_table = <num> genetic code.
                            '-w',                   # Print out in batch mode.
                            input_file,
                            '-o',output_file],
                            stdout = PIPE, stderr = PIPE)
    stdout, stderr = process.communicate()
    del stdout,stderr

    ARAGORN2GFF3(output_file)

''' 
    RNAmmer can also detects rRNA, but only have perl version
'''
# Because RNAmmer will generate gff version 2, we need to transfer it from 2 to 3.
def RNAMMER2GFF3(RNAMMER_output):
    
    RNAMMER_output_gff3 = RNAMMER_output + '.gff'
    f = open(RNAMMER_output_gff3,'w')
    process = Popen(args=['awk', r'BEGIN {print "##gff-version 3"} NR>5{if($4 < $5 && $4 > 0 && $5 > 0) printf "%s\tRNAmmer-1.2\t%s\t%d\t%d\t%s\t%s\t.\tID=%s_rnammer_%s_%s;Name=%s\n" ,$1,$3,$4,$5,$6,$7,$1,$4,$5,$9}',RNAMMER_output], stdout = f, stderr = PIPE)
    stdout, stderr = process.communicate()
    del stdout,stderr
    
def RNAMMER (input_file,output_file):
    # For RNAMMER, the primary programs need to be modified

    process = Popen(args = ['rnammer',
                            '-S', 'bac'     # Kingdom us bacteria
                            '-gff', output_file,
                            input_file],
                            stdout = PIPE, stderr = PIPE)
    stdout, stderr = process.communicate()
    RNAMMER2GFF3(output_file)
    del stdout,stderr

    
def RNAmerge(file_1, file_2, name):
    list_f1 = []
    list_f2 = []
    list_merge = ["##gff-version 3\n"]
    out_dir_RNA = "./output/out_rna/"
    merge_file = name+'.rna_merge.gff'
    with open(file_1,'r') as f1:
        for line in f1:
            if not re.match("##",line):
                list_f1.append(line)
    f1.close()
    with open(file_2,'r') as f2:
        for line in f2:
            if not re.match("##",line):
                list_f2.append(line)
    f2.close()
    k = 0
    for i in range(len(list_f1)):
        for j in range(len(k,list_f2)):
            if list_f1[i].split()[3] < list_f2[j].split()[3]:
                list_merge.append(list_f1[i]);break
            else:
                list_merge.append(list_f2[j]);k += 1
    with open(out_dir_RNA+merge_file,'w') as f3:
        for line in list_merge:
            f3.write(line)
    f3.close()  

def createRNAOutDirs():
    if not os.path.exists(os.getcwd()+"/output/"):
        os.makedirs(os.getcwd()+"/output")
    if not os.path.exists(os.getcwd()+"/output/out_rna/"):
        os.makedirs(os.getcwd()+"/output/out_rna")
    if not os.path.exists(os.getcwd()+"/output/out_rna/infernal"):
        os.makedirs(os.getcwd()+"/output/out_rna/infernal")
    if not os.path.exists(os.getcwd()+"/output/out_rna/aragorn"):
        os.makedirs(os.getcwd()+"/output/out_rna/aragorn")
    if not os.path.exists(os.getcwd()+"/output/out_rna/rnammer"):
        os.makedirs(os.getcwd()+"/output/out_rna/rnammer")

def RNApredict(inputDir):
    pass
    # Parameters need to specified
    for file in os.listdir(inputDir):
        database_path = './db/bacteria' # Rfam is a essential reference to infernal

        out_dir_RNA = "./output/out_rna/"
        out_dir_ncRNA = "./output/out_rna/infernal/"
        out_dir_tRNA = "./output/out_rna/aragorn/"
        out_dir_rRNA = "./output/out_rna/rnammer/"
        output_file_ncRNA = out_dir_ncRNA+file.split(".")[0]+'.ncRNA'
        output_file_tRNA = out_dir_tRNA+file.split(".")[0]+'.tRNA'
        output_file_rRNA = out_dir_rRNA+file.split(".")[0]+'.rRNA'

        cpu_cores = '4'  # Get options to change the number of cores, should be string

        # doncRNA = True # Get options to ensure if fo this
        # dotRNA  = True # Get options to ensure if fo this
        # dorRNA  = True # Get options to ensure if fo this

        # if doncRNA == True:
        INFERNAL(inputDir+file, database_path, output_file_ncRNA, cpu_cores)
        # if dotRNA  == True:
        ARAGORN(inputDir+file, output_file_tRNA)
        # if dorRNA  == True:
        RNAMMER(inputDir+file, output_file_rRNA)
        
        # if doncRNA and dotRNA and dorRNA:
        RNAmerge(output_file_ncRNA+".gff", output_file_tRNA+".gff", file.split(".")[0])
        RNAmerge(out_dir_RNA+file.split(".")[0]+'.rna_merge.gff', output_file_rRNA+".gff", file.split(".")[0])
    # elif doncRNA and dotRNA:
        # RNAmerge(output_file_ncRNA,output_file_tRNA)
    # elif doncRNA and dorRNA:
    #     RNAmerge(output_file_ncRNA,output_file_rRNA)
    # elif dotRNA and dorRNA:
    #     RNAmerge(output_file_tRNA,output_file_rRNA)

# if __name__ == '__main__':
#     main()
