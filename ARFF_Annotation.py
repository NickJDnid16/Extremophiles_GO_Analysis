input = open ('./Uniprot_Genes_Lower.csv',mode='rb')
output = open ('./Gene_And_GO_Lower.txt',mode='wb')



for line in input:
    if "GO:" in line:
        line = line.replace('\n','')
        data = line.split('\t')
        gene = data[0]
        GO_Terms = data[3]
        GO_Terms = GO_Terms.replace("; ",',')
        output.write(gene+","+GO_Terms+",Lower\n")

