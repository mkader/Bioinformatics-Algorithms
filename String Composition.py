'''
     Input: An integer k and a string Text.
             5
             CAATCCAAC
     Output: Compositionk(Text), where the k-mers are written in lexicographic order.
             AATCC
             ATCCA
             CAATC
             CCAAC
             TCCAA
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_4_1_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_kmer = 0
in_dna=''
in_result=''
ldata = ''
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (line==1):
        in_kmer=int(ldata)
    elif (line==2):
        in_dna = ldata
    elif (line>3):
        in_result += ldata + "\n"
    line+=1
    
    
#print in_kmer, in_dna
#print in_result
#ou_file.write(in_result+"\n\n")

dnas = [in_dna[i:i+in_kmer] for i in range(0, len(in_dna)) if len(in_dna[i:i+in_kmer])==in_kmer]

#print dnas
dnas.sort()
#print dnas

for i,dna in enumerate(dnas):
    ou_file.write(dna+"\n")
                
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

