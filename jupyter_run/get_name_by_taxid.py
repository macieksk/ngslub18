from ete3 import NCBITaxa
import csv
ncbi = NCBITaxa()

tax_ids = []
with open("ids.txt") as file:  
    for line in file:
        tax_ids.append(line)

family_ids = []

for id in tax_ids:
    taxid2lineage = ncbi.get_lineage(id)
    ranks = ncbi.get_rank(taxid2lineage)
    family_ids.append(list(ranks.keys())[list(ranks.values()).index('family')])

taxid2name = ncbi.get_taxid_translator(family_ids)
print(taxid2name)

tsv_file = "family_names.tsv"

with open(tsv_file, 'w') as tsvfile:
   for key, value in taxid2name.items():
      tsvfile.write(str(key) + "\t" + value + "\n")
