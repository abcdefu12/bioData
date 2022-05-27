# translation to protein code start
print('<< translation of central Dogma >>')

# codon table file read
aaSeq1char = {}  # aa name: single-letter ex.A
aaSeq3char = {}  # aa name: three-letter ex.Ala
fractionDic = {}
dic = {}

f = open('codon_table.txt', 'r')
title = f.readline()

for line in f.readlines():
    data = line.split('\t')
    triplet = data[0]
    aa1char = data[1]
    aa3char = data[2]
    fraction = float(data[3])

    # aaSeq1char[triplet] = aa1char   # codon Table for 1char
    # aaSeq3char[triplet] = aa3char   # codon Table for 3char
    # fractionDic[triplet] = fraction
    dic[triplet] = [aa1char, aa3char, fraction]

f.close()

# codon table
print('< codon Table >')
print('Codon dic:', dic)
# print('codon Table for 1Char:', aaSeq1char)
# print('codon Table for 3Char:', aaSeq3char)
# print('--------------------------------------')


# Get DNA sequence which was provided
f = open('dna_sequence.txt', 'r')   # now it is e.coli DNA sequence
sequence = ''
for line in f.readlines():
    sequence = sequence + line.strip().upper().replace(' ', '')
f.close()
print(sequence)
# proteinSeq1Char = ''
# proteinSeq3Char = ''
pSeq1Char = ''
pSeq3Char = ''

for i in range(0, len(sequence), 3):
    Triplet = sequence[i:i + 3]
    # proteinSeq1Char = proteinSeq1Char + aaSeq1char[Triplet]
    # proteinSeq3Char = proteinSeq3Char + aaSeq3char[Triplet]
    # print(dic[Triplet][0])
    # print(type(dic[Triplet]))
    pSeq1Char = pSeq1Char + dic[Triplet][0]
    pSeq3Char = pSeq3Char + dic[Triplet][1]

print('< result of translation >')
print('pseq', pSeq1Char)
print('pseq', pSeq3Char)
# print('protein seq of single letter:', proteinSeq1Char)
# print('protein seq of triple letter:', proteinSeq3Char)
print('--------------------------------------')


# reverse translation start
dic1 = {}
f = open('codon_table.txt', 'r')
title = f.readline()
for line in f.readlines():
    data = line.split('\t')
    triplet = data[0]
    aa1char = data[1]
    aa3char = data[2]
    fraction = float(data[3])

    if aa3char in dic1:
        dic1fraction = dic1[aa3char][1]
        if fraction >= dic1fraction:
            dic1[aa3char] = [triplet, fraction]
    else:
        dic1[aa3char] = [triplet, fraction]

f.close()
print(dic1)

dnaSeq = ''
for j in range(0, len(pSeq3Char), 3):
    triplet = pSeq3Char[j:j + 3]
    dnaSeq = dnaSeq + dic1[triplet][0]
print('reverse seq:', dnaSeq)