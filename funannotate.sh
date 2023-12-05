#!/usr/bin/bash -l
#SBATCH --mem 65G -c 32 --out funannotate_predict_%A.log
echo "The species name is $1"
echo "The path to assembly is $2"
ISPECIES=$1
IPATH=$2
OSORT='./raw_data/'$1'_sort.fasta'
OMASK='./raw_data/'$1'_mask.fasta'
ODIR=$1'_funannotate'
module load funannotate
funannotate sort -i $2 -o $OSORT --minlen 5000
funannotate mask -i $OSORT -o $OMASK --cpus 32
funannotate predict -i $OMASK -o $ODIR -s $1 --transcript_evidence ./raw_data/TriPr.Trinity.fasta --cpus 32 --augustus_species drosophila --busco_db insecta_odb10 --min_training_models 100 --weights snap:0 genemark:0