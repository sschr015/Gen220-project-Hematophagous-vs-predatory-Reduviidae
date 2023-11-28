#!/usr/bin/bash -l
#SBATCH --ntasks 32 --mem 20G -p short
module load trinity-rnaseq
module switch perl/5.22.0
Trinity --seqType fq --left ./raw_data/TriPr_F1.fastq --right ./raw_data/TriPr_F2.fastq --CPU 8 --max_memory 20G