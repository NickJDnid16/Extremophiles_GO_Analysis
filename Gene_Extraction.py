import glob

#################################Upper
top_hit = {}
for file in glob.glob('./Genome_Files/Under/*.m8_Cold'):
    print file
    for line in open(file,'rb'):
        timber = line.split('\t')
        query = file + timber[0]
        timber1 = timber[1]
        hit = timber[1].split('|')[1]
        bit = float(timber[11].replace('\\n',''))

        if query in top_hit:
            prev = top_hit[query]
            if bit > prev[0]:
                top_hit[query] = [bit,hit]
            else:
                continue
        else:
            top_hit[query] = [bit,hit]

unique_hits = []

for k,v in top_hit.iteritems():
    if v[1] in unique_hits:
        continue
    else:
        unique_hits.append(v[1])

output = open('Cold_genes.txt','wb')
for i in unique_hits:
    output.write(i+'\n')
output.close()

########################################Lower
top_hit = {}
for file in glob.glob('./Genome_Files/Under/*.m8'):
    print file
    for line in open(file,'rb'):
        timber = line.split('\t')
        query = file + timber[0]
        timber1 = timber[1]
        hit = timber[1].split('|')[1]
        bit = float(timber[11].replace('\\n',''))

        if query in top_hit:
            prev = top_hit[query]
            if bit > prev[0]:
                top_hit[query] = [bit,hit]
            else:
                continue
        else:
            top_hit[query] = [bit,hit]

unique_hits = []

for k,v in top_hit.iteritems():
    if v[1] in unique_hits:
        continue
    else:
        unique_hits.append(v[1])

output = open('BaseLine_genes.txt','wb')
for i in unique_hits:
    output.write(i+'\n')
output.close()