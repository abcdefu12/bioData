f = open('degannotation-n.dat', 'r')
lines = f.readline()


data = {}
i = 0
j = 0
for line in f.readlines():
    data = line.split('\t')
    DEG_AC = data[0]
    Gene_Ref = data[2]
    # Function = data[5]
    # Organism = data[6]

    # DEG_AC	#Gene_Name	#Gene_Ref	#COG	#Class	#Function	#Organism	#Refseq	#Strand	#Start	#Stop	#Condition
    # print(Gene_Ref)
    if Gene_Ref == 'tRNA':
        i += 1
    if Gene_Ref == 'non-coding element':
        j += 1

print('total num of tRNA:', i)
print('total num of non-coding:', j)
f.close()

print('-----------------------------')

g = open('degannotation-p.dat', 'r')
lines = g.readline()

OrganismList = []
k = 0
l = 0
for line in g.readlines():
    data = line.split('\t')
    # DEG_AC = data[0]
    # Gene_Ref = data[2]
    Function = data[5]
    Organism = data[7]

    # print(Organism)
    # print(Function)

    if Organism not in OrganismList:
        OrganismList.append(Organism)
    if 'Escherichia coli MG1655 I' in Organism:
        k += 1
    if 'DNA replication' in Function:
        l += 1


# print(OrganismList)
print('bacterial Species total num:', len(OrganismList))
print("'Escherichia coli MG1655 I' included:", k)
print('DNA Replication included:', l)
g.close()