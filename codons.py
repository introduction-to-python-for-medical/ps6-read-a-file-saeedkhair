path = "data/codons.txt"
file = open(path)
rows = file.readlines()
file.close()

def create_codon_dict(file_path):
    dictionary = {}
    for row in rows:
        row_list = row.strip().split("\t")
        codon = row_list[0]
        amino_acid = row_list[2]
        dictionary[codon] = amino_acid
    return dictionary
