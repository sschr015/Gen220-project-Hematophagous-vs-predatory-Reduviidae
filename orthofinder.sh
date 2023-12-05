#!/usr/bin/bash -l
#SBATCH --ntasks 32 --mem 8G -p short
module load ncbi-blast
module load orthofinder
CPU=32
MEM=8

orthofinder -a $CPU -f fororthofinder
