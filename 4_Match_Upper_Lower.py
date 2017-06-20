'''
Created on 25 Oct 2015

@author: nid16
'''

import codecs
import time
import linecache
from datetime import datetime

startTime = datetime.now()

OutPut = codecs.open('./Extremophiles_And_Vector.txt', encoding='utf-8', mode='wb')

lines = 0



for BinLine in codecs.open('./BinVec.txt',encoding='utf-8', mode='rb'):
    csv = BinLine.split(",")

    Gene = csv[0]
    Gene.strip("'")
    
    lines = lines +1
    
    line = linecache.getline('./Extremophile_Genes_GO_Class_BC_Thermophile.txt', lines)

    count = 0

    if "GO" in line:
        print count
        count += 1
        csv[1] = csv[1].replace('\n', '')
        Ge = line.split(",")
        length = len(Ge) -1
        if Ge[0] == Gene:

            if "Under" in Ge[length]:
                print "Under"


                Out = ','.join(csv)
                OutPut.write(Out.strip('\'"'))
                OutPut.write(",Under")
                OutPut.write("\n")

            elif "Upper" in Ge[length]:

                print "Upper"
                Out = ','.join(csv)
                Out = Out.replace('\'','')
                OutPut.write(Out.strip('"\''))
                OutPut.write(",Upper")
                OutPut.write("\n")


            else:
                Out = ','.join(csv)
                Out = Out.replace('\'','')
                OutPut.write(Out.strip('"\''))
                OutPut.write(",?")
                OutPut.write("\n")

    else:
        print "NO GO"

OutPut.close()

print(datetime.now()-startTime)