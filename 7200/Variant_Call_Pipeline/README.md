# Executes the variant call pipeline from the GATK
"The following specifies the usage for the command:
Options --
-a : specifies the first reads filepath
-b : specifies the second reads filepath
-r : specifies the reference filepath
-f : specifies the mills filepath
-o : specifies the output filename without extension
Flags --
-e : realignment steps to be executed
-i : indexing step to be executed
-z : output file needs to be unzipped
-v : verbose is set on
-h : shows the usage of the command
Example : snp_pipeline.bash -a reads1 -b reads2 -r ref -f millsFile -o outputFN -ez"
