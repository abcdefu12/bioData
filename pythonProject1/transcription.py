DNASeq = ''
f = open('ecoliDNA.txt', 'r')

data = f.readlines()

for line in data:
    line = line.replace('\n', '')
    line = line.replace(' ', '')
    DNASeq = DNASeq + line

print(DNASeq)

f.close()
