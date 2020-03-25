# Team2-GenePrediction
Developed By: Sachin Kumar, Mansi Gupta, Vineeth Aljapur, Manu Tej Sharma Arrojwala, Mingming Cao

## Overview
This pipeline of gene prediction is part of outbreak detection project of Computational Genomics course. The goal of this pipeline is identify the coding regions and non-coding regions of the genome. To do this we tried to quantitatively evaluate state of the art tools for our purpose and come up with a pipeline which gives out the best results according to our analysis. Beware, our pipeline has been optimized to work best on the *Salmonella enterica* genomes.

This pipeline includes tools like Prodigal, GeneMarkS2 for identifying genes and tools like Aragon, Infernal and RNAmmer for identifying non-coding regions of RNA. You can find further information on the tools from the links provided below.

## Requirements
We recommend installing these dependencies from the links provided.

We recommend using [conda](https://conda.io/en/latest/) to install latest version of  python and other python modules.\

[Python3](https://www.python.org/downloads/release/python-372/) To get python3 \
[GeneValidator](https://genevalidator.wurmlab.com/) To validate the results \
[Prodigal](https://github.com/hyattpd/Prodigal) To predict the genes \
[GeneMark-S2](http://exon.gatech.edu/GeneMark/license_download.cgi) To predict the genes \
[Glimmer](https://ccb.jhu.edu/software/glimmer/) To predict the genes \
[Blast](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download) To validate the results\

[Perl](https://www.perl.org/get.html) To ger Perl  \
[Aragorn](https://github.com/TheSEED/aragorn): Aragorn for tRNA and tmRNA prediction \
[RNAmmer](http://www.cbs.dtu.dk/cgi-bin/sw_request?rnammer): RNAmmer for rRNA prediction \
[Infernal](http://eddylab.org/infernal/): Infernal for misc_RNA prediction \
Further, for gff file operations, [bedtools](https://github.com/arq5x/bedtools2/releases) are highly recommended.



## QuickStart
```bash
conda create --name gene_pred python=3.7
conda activate gene_pred
git clone https://github.gatech.edu/compgenomics2019/Team2-GenePrediction
chmod 755 Team2-GenePrediction/gene_prediction.py
export PATH=$PWD/Team2-GenePrediction:$PATH

gene_prediction.py -h


# Usage
# gene_prediction.py -i Input [-h] [-f Format] [-g] [-q] [-v]
# Required Arguments:
# 	-i 		--Input			Input folder containing genome assemblies
# Optional Arguments:
# 	-h 		--help			echos help message and exits
#	 -f 		--Format			Output format (gff, gbk, sqn, sco)
#	 -g 		--genemark			To inculde GeneMark-S2 results
#	 -q 		--quiet			To supress text on terminal
# 	-v 		--verbose			To display running commands
```

If you have a folder named 'assemblies' containing all fasta files, you can run the above pipeline as described in the following example.

```bash
# check the contents of the file
ls assemblies
# CGT2006_contigs.fasta
# CGT2010_contigs.fasta
# CGT2044_contigs.fasta
# CGT2049_contigs.fasta
# CGT2060_contigs.fasta

gene_prediction.py -i assemblies -q

# check the generated output
ls output
# CGT2006_contigs_final.gff
# CGT2010_contigs_final.gff
# CGT2044_contigs_final.gff
# CGT2049_contigs_final.gff
# CGT2060_contigs_final.gff
# out_prod
# out_rna

ls output/out_prod
# CGT2006_contigs.gff
# CGT2010_contigs.gff
# CGT2044_contigs.gff
# CGT2049_contigs.gff
# CGT2060_contigs.gff
# nucl
# prot

ls output/out_rna
# aragorn
# CGT2006_contigs.rna_merge.gff
# CGT2010_contigs.rna_merge.gff
# CGT2044_contigs.rna_merge.gff
# CGT2049_contigs.rna_merge.gff
# CGT2060_contigs.rna_merge.gff
# infernal
# rnammer

```
