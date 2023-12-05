#!/usr/bin/bash -l
#SBATCH -c 32 --mem 65G --out tree_%A.log
module load muscle
module load IQ-TREE/2.1.1
module load trimal

DIR=$1
ALDIR=$2
mkdir $ALDIR'_muscle'
mkdir $ALDIR'_trimmed'
for file in $(ls $DIR)
    do
    muscle -align $DIR'/'$file -output $ALDIR'_muscle/'$file'.efa'
    trimal -automated1 -in $ALDIR'_muscle/'$file'.efa' -out $ALDIR'_trimmed/'$file'.phy' -phylip
    done

iqtree2 -S $ALDIR'_trimmed' -nt AUTO -b 1000 -alrt 1000