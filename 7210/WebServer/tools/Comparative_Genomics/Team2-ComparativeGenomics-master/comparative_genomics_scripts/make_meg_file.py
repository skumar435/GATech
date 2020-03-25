#!/projects/VirtualHost/predictb/tools/bin/bin/python3.7
out_file = '/projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/in_file.meg'
in_file = '/projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/distance_matrix.csv'
with open(out_file, 'w') as f:
    txt = '#mega\n'
    txt += '!Title: Genetic distance data of N meningitidis strains;\n'
    txt += '!Format DataType=Distance DataFormat=LowerLeft NTaxa=51;\n'
    txt += '!Description\n'
    txt += 'Genetic distance data of N meningitidis strains based on predicted cgMLST;\n\n'
    with open(in_file) as fp:
        count  = 0
        j = 0
        for line in fp:
            if count ==0 :
                count +=1 
                contigs = line.strip().split(',')[1:]
                contigs = [contig.split('.')[0] for contig in contigs]
                contigs = [contig.split('_')[0] for contig in contigs]
                for contig in contigs:
                    txt += '#'+contig+'\n'
                txt += '\n'
            else:
                string = ''
                for i in range(j):
                    string += line.strip().split(',')[1:][i] + '\t'
                txt += string+'\n'
                j += 1
                
    f.write(txt)
