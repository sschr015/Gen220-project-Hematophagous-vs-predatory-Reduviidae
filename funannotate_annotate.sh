#!/usr/bin/bash -l
#SBATCH --mem 65G -c 32 --out funannotate_annotate_%A.log
echo "The species name is $1"
INAME=$1'_funannotate'
IDIR=$1'_function'
module load funannotate
funannotate annotate -i $INAME --cpus 32 -o $IDIR --busco_db insecta_odb10