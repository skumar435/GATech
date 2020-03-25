#!/bin/bash

while getopts "i:" opt; do
	case "$opt" in
		i)
			dir=$OPTARG;;
	esac
done

# if [ ! -z "$i"  ];then
# 	echo "Missing input directory"
# 	exit 1
# fi

# if [ ! -d "$dir" ]; then
# 	echo "No such input directory"
# 	exit 1
# fi

# rm assemble_report.txt

datapath=$dir

mkdir projects/VirtualHost/predictb/tools/assembly/input/quast_output

list_contig="$(ls $datapath)"
numOfContig="$(ls $datapath | wc -l)"

i=1
# !!!change $numOfTrimmedDirs <==> n to run first n samples
while [ $i -le $numOfContig ]
do
	filename=$(echo $list_contig | awk '{print $'$i'}')
    	prefix=${filename%_*}
	prefix=${prefix##*/}
	echo Path $filename
	echo Prefix $prefix
	# checking with Quast
	/projects/VirtualHost/predictb/tools/assembly/quast-5.0.2/quast.py $datapath"$prefix"_contigs.fasta -o projects/VirtualHost/predictb/tools/assembly/input/quast_output/"$prefix"_quast

	i=$[i+1]
done

#Getting N50 values
awk '/N50/ {print FILENAME,$2}' projects/VirtualHost/predictb/tools/assembly/input/quast_output/*/report.txt > projects/VirtualHost/predictb/tools/assembly/N50.temp.stats.txt;

#Getting L50 values
awk '/L50/ {print FILENAME,$2}' projects/VirtualHost/predictb/tools/assembly/input/quast_output/*/report.txt > projects/VirtualHost/predictb/tools/assembly/L50.temp.stats.txt;

#Getting the no. of contigs
awk '{if($1== "#" && $2== "contigs" && $3!="(>=") {print FILENAME,$3}}' projects/VirtualHost/predictb/tools/assembly/input/quast_output/*/report.txt > projects/VirtualHost/predictb/tools/assembly/contig_number.temp.stats.txt;

#Getting Total Length of assemblies
awk '{if($1== "Total" && $3!="(>=") {print FILENAME,$3}}' projects/VirtualHost/predictb/tools/assembly/input/quast_output/*/report.txt > projects/VirtualHost/predictb/tools/assembly/total_length.temp.stats.txt;

#Merging content of files
echo -e 'Sample_Name N50\tL50\tContig_Number\tTotal_length' > projects/VirtualHost/predictb/tools/assembly/assemble_report.txt;paste <(awk '{print $1 "\t" $2}' projects/VirtualHost/predictb/tools/assembly/N50.temp.stats.txt ) <(awk '{print "\t" $2}' projects/VirtualHost/predictb/tools/assembly/L50.temp.stats.txt ) <(awk '{print "\t" $2}' projects/VirtualHost/predictb/tools/assembly/contig_number.temp.stats.txt ) <(awk '{print "\t" $2}' total_length.temp.stats.txt )>>projects/VirtualHost/predictb/tools/assembly/assemble_report.txt;

#Removing temp files
rm projects/VirtualHost/predictb/tools/assembly/*temp.stats.txt;
