from ete3 import NCBITaxa
import csv
ncbi = NCBITaxa()

tax_ids = []
with open("ids.txt") as file:  
    for line in file:
        tax_ids.append(int(line.rstrip()))

family_ids = []

for id in tax_ids:
    taxid2lineage = ncbi.get_lineage(id)
    ranks = ncbi.get_rank(taxid2lineage)
    try:
        family_ids.append([id, list(ranks.keys())[list(ranks.values()).index('family')]])
    except:
        pass

final_ids = []

for id in family_ids:
    print(id[0], id[1])
    taxid2name = ncbi.get_taxid_translator([id[1]])
    final_ids.append(taxid2name)

print(final_ids)

tsv_file = "family_names.tsv"

i = 0
with open(tsv_file, 'w') as tsvfile:
    for id in final_ids:
        for key, value in id.items():
            tsvfile.write(str(family_ids[i][0]) + "\t" + str(key) + "\t" + value + "\n")
        i = i + 1
