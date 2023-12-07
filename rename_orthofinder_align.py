#!/usr/bin/env python3
import argparse
from Bio import SeqIO
import os

parser = argparse.ArgumentParser(prog="Delete scaffolds with less then 4 types of nucleotides")

parser.add_argument('-i', "--dir",
                    help='path to the directory with single-copied genes .fa')
parser.add_argument('-o', "--odir",
                    help='path to the output directory with renamed files')
parser.add_argument('-n','--names_list', nargs='+',
                    help='list of names in the order of columns from Orthogroups.tsv')
args = parser.parse_args()
outdir = args.odir
names = args.names_list
i=-1
new_file = []
for file in os.listdir(args.dir):
    for record in SeqIO.parse(f'{args.dir}/{file}', "fasta"):
        i+=1
        print(record)
        record.id = names[i]
        record.name = str()
        record.description = str()
        new_file.append(record)
    SeqIO.write(new_file, f'{outdir}/{file}', "fasta")
    i=-1
    new_file = []