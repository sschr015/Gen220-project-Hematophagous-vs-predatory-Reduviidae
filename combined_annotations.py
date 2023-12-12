#!/usr/bin/env python3
import argparse
import os
import pandas as pd

parser = argparse.ArgumentParser(prog="Important genes sorter")

parser.add_argument('-i', "--ortho_out",
                    help='path to gained lost orthogroups folder')
parser.add_argument('-o', "--out",
                    help='output folder')
parser.add_argument('-all_orthogroups', "--file",
                    help='path to all orthogroup tsv file')
parser.add_argument('-annotation_files', "--annotations",
                    help='path to folder with annotations')
args = parser.parse_args()
df = pd.read_csv(args.file, sep="\t")
df.index = df["Orthogroup"]
df = df.drop("Orthogroup", axis=1)
df = df.drop("rhodnius-prolixus-cdcpeptidesrproc33", axis=1)
annotated_cell = str()
functional_cell = str()
function_list = []
annotation_list = []
annotcols = pd.DataFrame()

for sfile in os.listdir(args.ortho_out):
    sfiledf = pd.read_csv(f"{args.ortho_out}/{sfile}", sep = "\t")
    sorted = df.loc[sfiledf["Orthogroup"]]
    for column in sorted.columns.values:
        species = column.replace(".proteins","")
        for row in sorted.index.values:
            list = str(sorted.loc[row, column])
            if len(list) > 5:
                for gene in list.split(", "):
                    function_file = pd.read_csv(f"{args.annotations}/{species}.annotations.txt", sep = "\t")
                    function_file.index = function_file["TranscriptID"]
                    functional_cell = (functional_cell + str(function_file.loc[gene, "COG"]) + ', ')
                    annotated_cell = (annotated_cell + str(function_file.loc[gene, "Product"]) + ', ')
                function_list.append(functional_cell)
                annotation_list.append(annotated_cell)
                annotated_cell = str()
                functional_cell = str()
            else:
                function_list.append(None)
                annotation_list.append(None)
        annotcols[f'{species}_functions'] = function_list
        annotcols[f'{species}_annotation'] = annotation_list
        function_list = []
        annotation_list = []
    annotcols.index = sorted.index
    merged = pd.merge(sorted, annotcols, "left", left_on="Orthogroup", right_index=True)
    merged.to_csv(f"{args.out}/{sfile}", sep="\t")
    annotcols = pd.DataFrame()
