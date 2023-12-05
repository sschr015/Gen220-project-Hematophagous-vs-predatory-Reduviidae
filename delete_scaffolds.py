#!/usr/bin/env python3
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(prog="Delete scaffolds with less then 4 types of nucleotides")

parser.add_argument('-i', "--file",
                    help='path to the file with final masked scaffolds')
parser.add_argument('-o', "--out",
                    help='output file')
args = parser.parse_args()

fastafile = args.file
outfastafile = args.out
records = []
for r in SeqIO.parse(fastafile, "fasta"):
    if (("A" in r.seq or "a" in r.seq) and ("G" in r.seq or "g" in r.seq) and ("T" in r.seq or "t" in r.seq) and ("C" in r.seq or "c" in r.seq)): records.append(r)
SeqIO.write(records, outfastafile, "fasta")