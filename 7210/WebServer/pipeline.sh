#!/bin/bash
# To run: ./fk7210.sh -s 0 -e 3
#!!!get start and end from front end
###################################################
# home: data, assemble, predict, annotate, compare
# data: fastq, contig, predict_faa, annotate_gff <- each contains data files as described
#       + assemble_report.txt
# assemble, predict, annotate, compare: <- each is the wkdir for each step 
##################################################

while getopts "s:e:" opt; do
	case "$opt" in
		s)
			start=$OPTARG;;
        e)
            end=$OPTARG;;
	esac
done

# a list of what to do 
couldDo=("assemble" "predict" "annotate" "compare")

for i in $(seq $start $end);
do
    echo ${couldDo[i]};
    if [ $i == 0 ]
    then # run assembly
        #copy fastq to assemble folder
        cp -r ./data/fastq ./assemble/input
        #go to assemble folder
        cd ./assemble
        #!!!disable quast in assembly.sh? run assemble
        ./assembly.sh -i ./input
        # copy result contigs to data folder
        cp -r ./input/Assembled_Contigs ../data/contig
        # generate report using quast_summary.sh
        ./quast_summary.sh -i ./input/Assembled_Contigs
        # copy report to main folder
        cp assemble_report.txt ../
        # remove ./assemble/input
        rm -r ./input
        # exit to main folder
        cd ..
    fi
    if [ $i == 1 ]
    then # run predict
        #copy contig to predict folder
        cp -r ./data/contig ./predict/input
        #go to predict folder
        cd ./predict
        #run preditc
        gene_prediction.py -i ./input -q
        #copy results to data folder
        cp -r ./output/out_prod/prot/ ../data/predict_faa
        # remove ./predict/input
        rm -r ./input
        # exit to main folder
        cd ..
    fi
    if [ $i == 2 ]
    then # run annotate 
        #!!! correct inputs? what about gffs? faa from prediction
        functional_annotation_team2.py -i $predict_faa -ard 
        #what's the output? and where to get information about stats about outputs?  
        #copy predict_faa to annotate folder
        cp -r ./data/predict_faa ./annotate/input
        #go to annotate folder
        cd ./annotate
        #run annotate
        functional_annotation_team2.py -i ./input -ard 
        #copy results to data folder
        cp -r ./Func_annotation_result/ ../data/annotate_gff
        # remove ./annotate/input
        rm -r ./input
        # exit to main folder
        cd ..
    fi
    fi
    if [ $i == 3 ]
    then # run compare
        #!!!scripts?
    fi
done
