#!/usr/bin/bash -l
#SBATCH --mem 60G -c 32 --out funannotate_run_Zelurus.log
module load funannotate
funannotate sort -i ./raw_data/Zelurus_nigrolineatus_scaffolds.fasta -o ./raw_data/Zelurus_nigrolineatus_scaffolds_sort.fasta --minlen 5000
funannotate mask -i ./raw_data/Zelurus_nigrolineatus_scaffolds_sort.fasta -o ./raw_data/Zelurus_nigrolineatus_scaffolds_masked.fasta --cpus 8
funannotate predict -i ./raw_data/Zelurus_nigrolineatus_scaffolds_masked.fasta -o Zelurus_nigrolineatus_funannotate -s "Zelurus nigrolineatus" --transcript_evidence ./raw_data/TriPr.Trinity.fasta --cpus 32 --augustus_species drosophila --busco_db eukaryota_odb10 --weights snap:0 genemark:0