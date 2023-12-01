#!/usr/bin/bash -l
#SBATCH --mem 65G -c 32 --out funannotate_run_Cavernicola.log
module load funannotate
funannotate sort -i ./raw_data/Cavernicola_scaffolds.fasta -o ./raw_data/Cavernicola_scaffolds_sort.fasta --minlen 5000
funannotate mask -i ./raw_data/Cavernicola_scaffolds_sort.fasta -o ./raw_data/Cavernicola_scaffolds_masked.fasta --cpus 32
funannotate predict -i ./raw_data/Cavernicola_scaffolds_masked.fasta -o Cavernicola_funannotate -s "Cavernicola sp" --transcript_evidence ./raw_data/TriPr.Trinity.fasta --cpus 32 --augustus_species drosophila --busco_db insecta_odb10 --weights snap:0 genemark:0