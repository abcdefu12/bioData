# open a codon table file

codons1 = {} # single-letter
codons2 = {} # three-letter

f=open('codon_table.txt','r')
title = f.readline()

for line in f.readlines():
	data = line.split('\t')
	codon = data[0]
	aa1 = data[1]
	aa2 =data[2]
	fraction = float(data[3])
	
	codons1[codon] = aa1
	codons2[codon] = aa2

f.close()

# open a DNA sequence file
f=open('dna_sequence.txt', 'r')
sequence = ''
for line in f.readlines():
	sequence = sequence + line.strip().upper().replace(' ','')
f.close()

protein1 = ''
protein2 = ''

for i in range(0, len(sequence), 3):
	codon = sequence[i:i+3]
	protein1 = protein1 + codons1[codon]
	protein2 = protein2 + codons2[codon]
	
print(protein1)
print(protein2)
