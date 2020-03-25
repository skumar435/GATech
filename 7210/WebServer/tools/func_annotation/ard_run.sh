#!/bin/bash
export PATH=$PATH:/projects/VirtualHost/predictb/tools/Miniconda/envs/charm/bin
path_to_resfinder=/projects/VirtualHost/predictb/
path_to_dbs=/projects/VirtualHost/predictb/tools/func_annotation/arg_dbs
path_to_blast=/projects/VirtualHost/predictb/
path_to_python3=/projects/VirtualHost/predictb/tools/Python-3.7.3/Python

input_folder_base=/projects/VirtualHost/predictb/html/Site/public/fastas
path_to_gffs=/projects/VirtualHost/predictb/tools/input/Prodigal_results/output/CGT2006_contigs.gff
out_dir="output_ard"
v=0

usage="$(basename "$0") [-h]
	-i <path_to_input_clusters>
	-o <path_to_output_directory>
	-g <path_to_prodigal_GFFs>
	-v (verbose mode)"
# input: .faa of unique genes
# o is out directory
while getopts "i:o:g:f:vh" option
do
	case $option in
		i) input_path=$OPTARG;;
		o) out_dir=$OPTARG;;
		g) path_to_gffs=$OPTARG;;
		v) v=1;;
		h) echo "$usage"
		   exit;;
	esac
done

input_dir="$input_folder_base"/"$input_path"
outdir="$input_dir"/"$out_dir"
input_path="$input_dir"/output/out_prod/prot
for file in "$input_path"/*
do
	input_path="$file"
done

filend=$(echo "$input_path" | sed 's/.*\./\./')
infile=$(basename "$input_path" "$filend")

#[[ v -eq 1 ]] && echo "Querying Victors database"
#mkdir -p "$outdir"/victors
#"$path_to_blast"p -query "$input_path" \
#	-db "$path_to_dbs"/victors \
#	-out "$outdir"/victors/victors_"$infile".out \
#	-outfmt "6 qseqid sseqid length pident qcovs qstart qend sstart send evalue stitle" \
#	-max_target_seqs 1 \
#	-evalue 0.001
#awk -F "\t" '{ if(($4 >= 90) && ($5 >= 90)) {
#	print } }' "$outdir"/victors/victors_"$infile".out > "$outdir"/victors/victors_"$infile"_90.tsv
#echo "##gff-version 3" > "$outdir"/victors/cluster_victors.gff
#awk -F "\t" 'BEGIN{OFS="\t"}{ print $1, "Victors", "ARD", ".", ".", $10, ".", ".", "hit_id="$2";hit_name="$11;
#	}' "$outdir"/victors/victors_"$infile"_90.tsv >> "$outdir"/victors/cluster_victors.gff

[[ v -eq 1 ]] && echo "Querying VFDB"
mkdir -p "$outdir"/vfdb
blastp -query "$input_path" \
	-db "$path_to_dbs"/vfdb \
	-out "$outdir"/vfdb/vfdb_"$infile".out \
	-outfmt "6 qseqid sseqid length pident qcovs qstart qend sstart send evalue stitle" \
	-max_target_seqs 1 \
	-evalue 0.001
awk -F "\t" '{ if(($4 >= 90) && ($5 >= 90)) {
	print } }' "$outdir"/vfdb/vfdb_"$infile".out > "$outdir"/vfdb/vfdb_"$infile"_90.tsv
echo "##gff-version 3" > "$outdir"/vfdb/cluster_vfdb.gff
awk -F "\t" 'BEGIN{OFS="\t"}{ print $1, "VFDB", "Virulence_Factors", ".", ".", $10, ".", ".",
	"hit_id="$2";hit_name="$11}' "$outdir"/vfdb/vfdb_"$infile"_90.tsv >> "$outdir"/vfdb/cluster_vfdb.gff

[[ v -eq 1 ]] && echo "Running RGI"
mkdir -p "$outdir"/rgi
/projects/VirtualHost/predictb/tools/rgi main -i "$input_path" -o "$outdir"/rgi/rgi_"$infile" -t protein --clean
sed 's/;/,/g' "$outdir"/rgi/rgi_"$infile".txt > "$outdir"/rgi/rgi_"$infile"_nosemi.txt
awk -F " " 'BEGIN{OFS="\t"}{ if(NR>1) print $1;
	}' "$outdir"/rgi/rgi_"$infile"_nosemi.txt > "$outdir"/rgi/rgi_gff_pt1.tsv
awk -F "\t" 'BEGIN{OFS="\t"}{ if(NR>1) print "RGI", "ARD", ".", ".", ".", ".", ".",
	"best_hit="$9";ARO_accession="$11";drug_class="$15";resistance_mech="$16";gene_family="$17;
	}' "$outdir"/rgi/rgi_"$infile"_nosemi.txt > "$outdir"/rgi/rgi_gff_pt2.tsv
echo "##gff-version 3" > "$outdir"/rgi/cluster_rgi.gff
paste "$outdir"/rgi/rgi_gff_pt1.tsv "$outdir"/rgi/rgi_gff_pt2.tsv >> "$outdir"/rgi/cluster_rgi.gff
#mv "$outdir" "$input_dir"
#for start and stop site of the contigs
input_dir1="$input_dir/"
input_path_gff="$input_dir1"output/out_prod/
input_path_fasta="$input_dir1"output/out_prod/prot/
input_path_rgi="$input_dir1"output_ard/rgi/
input_path_vfdb="$input_dir1"output_ard/vfdb/
#for file in "$input_path_gff"/*
input_path_abs_gff=""
input_path_abs_fasta=""
input_path_abs_gff=$(find $input_path_gff -name "*.gff")
for file in "$input_path_fasta"*
do
	input_path_abs_fasta="$file"
	# echo $input_file_gff
done
#echo "input_file"
#echo "$input_path_abs_gff"
#echo "$input_path_abs_fasta"
filend_gff=$(echo "$input_path_gff" | sed 's/.*\./\./')
infile_gff=$(basename "$input_path_gff" "$filend_gff")
#echo $input_file_gff
#echo $filend_gff
#echo $infile_gff
#awk -v OFS='\t' '{ split($9, a, ";"); split(a[1], b, "_"); print $1"_"b[2], $2, $3, $4, $5, $6, $7, $8, $9 }' CGT2006_contigs.gff > CGT2006_contigs_mod.gff
#awk -v OFS='\t' '{ split($9, a, ";"); split(a[1], b, "_"); print $1"_"b[2], $2, $3, $4, $5, $6, $7, $8, $9 }' $input_file >  _numbered.gff
awk -v OFS='\t' '{ split($9, a, ";"); split(a[1], b, "_"); print $1"_"b[2], $2, $3, $4, $5, $6, $7, $8, $9 }' $input_path_abs_gff > "$input_path_gff"final.gff
sed '/^#/d' "$input_path_gff"final.gff > "$input_path_gff"final_mod.gff
sed '/^#/d' "$input_path_vfdb"cluster_vfdb.gff > "$input_path_vfdb"nohash_cluster_vfdb.gff
sed '/^#/	d' "$input_path_rgi"cluster_rgi.gff > "$input_path_rgi"nohash_cluster_rgi.gff
awk 'NR==FNR { n[$1]=$0;next } { print n[$1] }' "$input_path_gff"final_mod.gff  "$input_path_vfdb"nohash_cluster_vfdb.gff > "$input_path_vfdb"intermediate_vfdb.gff
awk 'NR==FNR { n[$1]=$0;next } { print n[$1] }' "$input_path_gff"final_mod.gff  "$input_path_rgi"nohash_cluster_rgi.gff > "$input_path_rgi"intermediate_rgi.gff
awk -v OFS='\t' 'FNR==NR{a[NR]=$4;next}{$4=a[FNR]}1' "$input_path_vfdb"/intermediate_vfdb.gff "$input_path_vfdb"nohash_cluster_vfdb.gff > "$input_path_vfdb"pre_final_vfdb.gff
awk -v OFS='\t' 'FNR==NR{a[NR]=$5;next}{$5=a[FNR]}1' "$input_path_vfdb"/intermediate_vfdb.gff "$input_path_vfdb"pre_final_vfdb.gff > "$input_path_vfdb"final_vfdb.gff
awk -v OFS='\t' 'FNR==NR{a[NR]=$4;next}{$4=a[FNR]}1' "$input_path_rgi"/intermediate_rgi.gff "$input_path_rgi"nohash_cluster_rgi.gff > "$input_path_rgi"pre_final_rgi.gff
awk -v OFS='\t' 'FNR==NR{a[NR]=$5;next}{$5=a[FNR]}1' "$input_path_rgi"/intermediate_rgi.gff "$input_path_rgi"pre_final_rgi.gff > "$input_path_rgi"final_rgi.gff
rm "$input_path_rgi"/intermediate_rgi.gff
rm "$input_path_vfdb"/intermediate_vfdb.gff
rm "$input_path_rgi"nohash_cluster_rgi.gff
rm "$input_path_vfdb"nohash_cluster_vfdb.gff
rm "$input_path_gff"final_mod.gff
rm "$input_path_gff"final.gff
rm "$input_path_rgi"pre_final_rgi.gff
rm "$input_path_vfdb"pre_final_vfdb.gff
