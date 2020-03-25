awk -F '\t' -v OFS='\t' '!/^#/ {$1=$1;print}' <name_of_gff_file>  >  <name_of_tsv_file>
