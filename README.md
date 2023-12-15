# Exploring the genetic adaptations of hematophagous Triatominae (Hemiptera: Reduviidae)
## Veronica Tyts & Sarah Schroeder
### Introduction
Hi! Welcome to the git hub repository for our gen220 project. Within this repository you will find all of the scripts we used to identify genetic differences between hematophagous and predatory reduviids, annotate those genes, and create our figures.    

# Explanation of scripts 
## De novo assembly
<details>
  
We only needed to assemble RNA seq data for one species. We used the script **trinity.sh** in which we used the default settings of Trinity and included paths to fastq files of our data. 
</details>

## Gene annotation
<details>
  
We used the tool funannote to annote our whole genome sequences. Inputs for the script **funannotate.sh** should be annotated genomes in fasta file format. Note that the insect genome is large for this tool, so we made modifications accordingly. The cleaning step has been bypassed, minimum sequence length has been set at 5kb, RNA seq data of a closely related species was added as evidence for the predict tool, the minimum training models for Augustus was set to 100 genes, the Drosophila training model was used for Augustus, and both snap and gene mark software were turned off. Because the cleaning step was bypassed, the script **delete_scaffolds.py** can be used to delete scaffolds with less than 4 types of nucleotides.
The script **funannotate_annotate.sh** can then be used to complete annotation. Default settings are used in this script with insecta_odb10 busco database
</details>

## Orthofinder
<details>
  
Orthofinder can be used to identify orthogroups among species. The default settings are used within **orthofinder.sh** with protein fasta files created by funannotate as input.  
</details>

## Identification of lost and gained orthogroups
<details>
  
We used the script **orthofinder_out.py** to create tables listing the single copy and multiple copy orthogroups gained by the hematophagous reduviids, the single and multiple copy orthogroups lost by the reduviids, and the single copy orthogroups present in all six species. This script uses the Orthogroups.GeneCount.tsv file created by orthofinder as input. 
</details>

## Merging annotation and function

<details>

To merge gene annotations and functions identified with funannotate with the identified gained and lost genes, we used the script **combined_annotations.py**. The inputs for this script are the path to folder containing gained and lost orthogroup tables, orthogroups.tsv file created by orthofinder containing all orthogroups and the genes withing them, and the path to the folder containing gene annotations for each species. 
</details>

## Visualizing the gained/lost genes functional comparison of hematophagous and predatory genomes
<details> 
  
We used matplotlib in Python to show the difference between gained/lost gene functions between hematophagous and predatory species. The script **Final_plot.ipynb** was used, functional types' details can be found in annotated files. 

</details>

## Tree building
<details>
  
### Add species names 
Before preparing data for a tree we first needed to add species names to the single copy ortholgroup fasta files created by orthofinder using the script **rename_orthofinder_align.py**. Inputs include a names list containing the name of all species in order of the columns from Orthogroups.tsv (output of orthofinder), as well as a path to the directory of single copy orthogroup fasta files created by orthofinder. 

### Align and trim and create tree file
Sequences can now be prepared for a tree using **align_and_trim.sh**. Default settings of muscle and trimal are used to allin and trim sequences. IQ-tree is using with 1000 bootstrap replicates and 1000 likelihood ratio test replicates. The -con -t tree commands are used to obtain a consensus tree file. 
  
</details>

## Visualizing the phylogeny
<details>
  
We used ggtree in R to visualize our phylogeny. The script **ggtree.R** was used and hematophagous species were marked by red tip labels. A color gradient with legend was also created for detailing branches with bootstrap support. 
</details>
