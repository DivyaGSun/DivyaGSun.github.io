#Cite: codon table taken from internet
bases = "UCAG"
codons = [a + b + c for a in bases for b in bases for c in bases]
amino_acids ='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

def run(seq):
    peptide = ''
    for i in range(0, len(seq), 3):
        codon = seq[i: i+3]
        #print(codon)
        amino_acid = codon_table.get(codon)
        #print(amino_acid)
        if amino_acid != '*':
            peptide += amino_acid
        else:
            break

    return peptide
