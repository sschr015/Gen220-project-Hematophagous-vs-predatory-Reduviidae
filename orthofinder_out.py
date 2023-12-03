#!/usr/bin/env python3
import argparse
import pandas as pd

parser = argparse.ArgumentParser(prog="Important genes sorter")

parser.add_argument('-i', "--file",
                    help='path to Orthogroups.GeneCount.tsv file')
parser.add_argument('-o', "--out",
                    help='output folder')
args = parser.parse_args()

folder = args.out
df = pd.read_csv(args.file, sep="\t")
#Homalocoris_erythrogaster is outgroup

type_phy = df[(df['Homalocoris_erythrogaster'] == 1) & (df['Opisthacidius'] == 1) & (df['Zeluroides_americanus'] == 1) & (df['Zelurus_nigrolineatus'] == 1) & (df['Cavernicola'] == 1) & (df['Rhodnius_prolixus'] == 1)]
type_gain = df[(df['Opisthacidius'] == 0) & (df['Zeluroides_americanus'] == 0) & (df['Zelurus_nigrolineatus'] == 0) & (df['Cavernicola'] > 0) & (df['Rhodnius_prolixus'] > 0)]
type_gainM = type_gain[(type_gain['Cavernicola'] > 1) | (type_gain['Rhodnius_prolixus'] > 1)]
type_gainS = type_gain[(type_gain['Cavernicola'] == 1) & (type_gain['Rhodnius_prolixus'] == 1)]
logic_for_lost = ((df['Opisthacidius'] > 0) & ((df['Zeluroides_americanus'] > 0) | (df['Zelurus_nigrolineatus'] > 0)) | ((df['Zeluroides_americanus'] > 0) & (df['Zelurus_nigrolineatus'] > 0)))
type_lost = df[logic_for_lost & (df['Cavernicola'] == 1) & (df['Rhodnius_prolixus'] == 1)]
type_lostM = type_lost[(type_lost['Opisthacidius'] > 1) | (type_lost['Zeluroides_americanus'] > 1) | (type_lost['Zelurus_nigrolineatus'] > 1)]
type_lostS = type_lost[(type_lost['Opisthacidius'] == 1) & (type_lost['Zeluroides_americanus'] == 1) | (type_lost['Zelurus_nigrolineatus'] == 1))]

type_phy.to_csv("type_1.tsv", sep="\t", index=False)
type_gain.to_csv("type_2.tsv", sep="\t", index=False)
type_gainS.to_csv("type_2a.tsv", sep="\t", index=False)
type_gainM.to_csv("type_2b.tsv", sep="\t", index=False)
type_lost.to_csv("type_3.tsv", sep="\t", index=False)
type_lostS.to_csv("type_3a.tsv", sep="\t", index=False)
type_lostM.to_csv("type_3b.tsv", sep="\t", index=False)