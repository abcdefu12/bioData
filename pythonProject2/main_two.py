f = open('dna_sequence.txt', 'r')
g = open('codon_table.txt', 'r')
data = f.readlines()
data1 = g.readlines()
DNASeq = ''
Info = ''
codon = 3
DNASplit = []

for line in data:
    line = line.replace('\n', '')
    line = line.replace(' ', '')
    DNASeq = DNASeq + line
    # splitCodon = list(map)
    line = line.replace('\n', '')

print(DNASeq)
DNASplit = list(map(''.join, zip(*[iter(DNASeq)]*codon)))
print(DNASplit)

i = 0
Info_name = ['Triplet', 'AminoAcidSingle', 'AminoAcid', 'Fraction']

for line in data1:
    line = line.replace('\n', '\t')
    Info = Info + line
    InfoB = Info.split('\t')
    i += 1

dictionary = dict(zip(Info_name, InfoB))


print('i:', i)
print('dic:', dictionary)
# ProteinDic = {'Triplet', 'AminoAcidSingle', 'AminoAcid','Fraction'}
f.close()
g.close()

print('Info:', Info)
print('InfoB:', InfoB)
