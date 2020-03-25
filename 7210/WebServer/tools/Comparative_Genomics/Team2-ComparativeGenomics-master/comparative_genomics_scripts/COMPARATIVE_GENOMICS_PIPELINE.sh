#!/bin/bash

# Run MLST:

# MLST Requirements:
# Must have FASTA files for building the database in a directory called MLST_FASTA_FILES in the working directory

#echo "######################## MLST ###########################"

#./mlst_analysis.sh


#echo "######################## kSNP3 ########################"

#export PATH=/projects/team3/comparatve_genomics/JZ/kSNP/kSNP3.1_Linux_package/kSNP3:$PATH

#MakeFasta /projects/team2/comp_gen_temp/ksnp_run_folder/input_list.txt /projects/team2/comp_gen_temp/ksnp_run_folder/fastainput
#Kchooser /projects/team2/comp_gen_temp/ksnp_run_folder/fastainput
#kSNP3 -in /projects/team2/comp_gen_temp/ksnp_run_folder/input_list.txt -outdir KSNP_FINAL_RESULT -k 19 -vcf -ML | tee /projects/team2/comp_gen_temp/ksnp_run_folder/log.txt


echo "######################## ANI ########################"

export PATH=$PATH:/projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/mummer/
export PATH=$PATH:/projects/VirtualHost/predictb/tools/Miniconda/envs/assem/bin

#wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
#chmod 755 Anaconda3-2019.03-Linux-x86_64.sh
#./Anaconda3-2019.03-Linux-x86_64.sh
/projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/Team2-ComparativeGenomics-master/comparative_genomics_scripts/get_distance_matrix.py -d /projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/Assem_Contigs/ -i /projects/VirtualHost/predictb/html/Site/public/fastas/$1/ -o /projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/distances.csv -t 4
cat /projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/distances_50.csv /projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/distances.csv > /projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/distances_input.csv
export PYTHONPATH=/projects/VirtualHost/predictb/tools/Miniconda/envs/assem/lib/python3.5/site-packages
/projects/VirtualHost/predictb/tools/Miniconda/envs/assem/bin/python3.5 /projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/Team2-ComparativeGenomics-master/comparative_genomics_scripts/make_distance_matrix.py
/projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/Team2-ComparativeGenomics-master/comparative_genomics_scripts/make_meg_file.py
mkdir -p /projects/VirtualHost/predictb/html/Site/public/fastas/$1/output
/projects/VirtualHost/predictb/tools/Comparative_Genomics/megacc -a /projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/infer_NJ_distances.mao -d /projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/in_file.meg -o /projects/VirtualHost/predictb/html/Site/public/fastas/$1/output/output_cg
sed -i 's/;//g' /projects/VirtualHost/predictb/html/Site/public/fastas/$1/output/output_cg.nwk
