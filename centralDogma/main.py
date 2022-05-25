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
print('--------------------------------------')