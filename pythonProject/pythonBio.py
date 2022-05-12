# PCR 계산
# Tm=2(A+T)+4(C+G)-7 (오차는 존재함.)
# ex) 5'-ACGTCCGACTT-3'
exSeq = 'ACGTCCGACTT'
totalNumOfAT = 0
totalNumOfGC = 0
for nt in exSeq:
    if nt == 'A' or nt == 'T':
        totalNumOfAT += 1
    if nt == 'G' or nt == 'C':
        totalNumOfGC += 1
Tm = 2 * totalNumOfAT + 4 * totalNumOfGC - 7
print('Tm Value =', Tm)
