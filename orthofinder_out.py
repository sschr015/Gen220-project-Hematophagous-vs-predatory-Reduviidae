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

type_phy = df[(df['Homalocoris_erythrogaster.proteins'] == 1) & (df['Opisthacidius.proteins'] == 1) & (df['Zeluroides_americanus.proteins'] == 1) & (df['Zelurus_nigrolineatus.proteins'] == 1) & (df['Cavernicola.proteins'] == 1) & (df['rhodnius-prolixus-cdcpeptidesrproc33'] == 1)]
type_gain = df[(df['Opisthacidius.proteins'] == 0) & (df['Zeluroides_americanus.proteins'] == 0) & (df['Zelurus_nigrolineatus.proteins'] == 0) & (df['Cavernicola.proteins'] > 0) & (df['rhodnius-prolixus-cdcpeptidesrproc33'] > 0)]
type_gainM = type_gain[(type_gain['Cavernicola.proteins'] > 1) | (type_gain['rhodnius-prolixus-cdcpeptidesrproc33'] > 1)]
type_gainS = type_gain[(type_gain['Cavernicola.proteins'] == 1) & (type_gain['rhodnius-prolixus-cdcpeptidesrproc33'] == 1)]
logic_for_lost = ((df['Opisthacidius.proteins'] > 0) & ((df['Zeluroides_americanus.proteins'] > 0) | (df['Zelurus_nigrolineatus.proteins'] > 0)) | ((df['Zeluroides_americanus.proteins'] > 0) & (df['Zelurus_nigrolineatus.proteins'] > 0)))
type_lost = df[logic_for_lost & (df['Cavernicola.proteins'] == 0) & (df['rhodnius-prolixus-cdcpeptidesrproc33'] == 0)]
type_lostM = type_lost[(type_lost['Opisthacidius.proteins'] > 1) | (type_lost['Zeluroides_americanus.proteins'] > 1) | (type_lost['Zelurus_nigrolineatus.proteins'] > 1)]
type_lostS = type_lost[(type_lost['Opisthacidius.proteins'] == 1) & (type_lost['Zeluroides_americanus.proteins'] == 1) & (type_lost['Zelurus_nigrolineatus.proteins'] == 1)]

type_phy.to_csv(f"{folder}/type_phy.tsv", sep="\t", index=False)
type_gain.to_csv(f"{folder}/type_gain.tsv", sep="\t", index=False)
type_gainS.to_csv(f"{folder}/type_gainS.tsv", sep="\t", index=False)
type_gainM.to_csv(f"{folder}/type_gainM.tsv", sep="\t", index=False)
type_lost.to_csv(f"{folder}/type_lost.tsv", sep="\t", index=False)
type_lostS.to_csv(f"{folder}/type_lostS.tsv", sep="\t", index=False)
type_lostM.to_csv(f"{folder}/type_lostM.tsv", sep="\t", index=False)