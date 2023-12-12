# Exploring the genetic adaptations of hematophagous Triatominae (Hemiptera: Reduviidae)
## Veronica Tyts & Sarah Schroeder
### Introduction
Hi! Welcome to the git hub repository for our gen220 project. Within this repository you will find all of the scripts we used to identify genetic differences between hematophagous and predatory reduviids, annotate those genes, and create our figures.
### Explanation of scripts
<details> 
## Gene annotation
We used the tool funannote to annote our whole genome sequences. Inputs for the script "funannotate.sh" should be annotated genomes in fasta file format. Note that the insect genome is large for this tool, so we made modifications accordingly. The cleaning step has been bypassed, minimum sequence length has been set at 5kb, RNA seq data of a closely related species was added as evidence for the predict tool, the minimum training models for Augustus was set to 100 genes, the Drosophila training model was used for Augustus, and both snap and gene mark software were turned off.
The script funannotate_annotate.sh can then be used to complete annotation. Default settings are used in this script with insecta_odb10 busco database
</details>
