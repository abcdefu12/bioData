# translation to protein code start
print('<< translation of central Dogma >>')

# codon table file read
aaSeq1char = {}  # aa name: single-letter ex.A
aaSeq3char = {}  # aa name: three-letter ex.Ala

f = open('codon_table.txt', 'r')
title = f.readline()

for line in f.readlines():
    data = line.split('\t')
    Triplet = data[0]
    aa1char = data[1]
    aa3char = data[2]
    fraction = float(data[3])

    aaSeq1char[Triplet] = aa1char   # codon Table for 1char
    aaSeq3char[Triplet] = aa3char   # codon Table for 3char

f.close()

# codon table
print('< codon Table >')
print('codon Table for 1Char:', aaSeq1char)
print('codon Table for 3Char:', aaSeq3char)
# print('--------------------------------------')


# Get DNA sequence which was provided
f = open('dna_sequence.txt', 'r')   # now it is e.coli DNA sequence
sequence = ''
for line in f.readlines():
    sequence = sequence + line.strip().upper().replace(' ', '')
f.close()

proteinSeq1Char = ''
proteinSeq3Char = ''

for i in range(0, len(sequence), 3):
    Triplet = sequence[i:i + 3]
    proteinSeq1Char = proteinSeq1Char + aaSeq1char[Triplet]
    proteinSeq3Char = proteinSeq3Char + aaSeq3char[Triplet]

print('< result of translation >')
print('protein seq of single letter:', proteinSeq1Char)
print('protein seq of triple letter:', proteinSeq3Char)
print('--------------------------------------')