'''
     Input: An integer k and a string Text.
             4
             AAGATTCTCTAC
     Output: DeBruijnk(Text).
             AAG -> AGA
             AGA -> GAT
             ATT -> TTC
             CTA -> TAC
             CTC -> TCT
             GAT -> ATT
             TCT -> CTA,CTC
             TTC -> TCT
'''


import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_4_4_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_dna=[]
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (len(ldata)==0):
        break
    else:
        in_dna.append(ldata)
    
print in_dna
print ''

'''
in_dna = ['GAGG', 'GGGG', 'GGGA', 'CAGG', 'AGGG', 'GGAG']
dna  = ['GAG', 'GGG', 'GGG', 'CAG', 'AGG', 'GGA']
unqiue dna =  ['AGG', 'CAG', 'GAG', 'GGA', 'GGG']
'''
kmer = len(in_dna[0])-1
dna = [in_dna[i][:kmer] for i in range(0,len(in_dna))]
dna = list(set(dna))
dna.sort()

'''
C = mv.find(dr)
D =d[:kmer]
M = d[:kmer]==dna and mv.find(dr)<0)
dna i d    dr  D   C M mv 
AGG 0 GAGG AGG GAG -1 F
    1 GGGG GGG GGG -1 F
    2 GGGA GGA GGG -1 F 
    3 CAGG AGG CAG -1 F
    4 AGGG GGG AGG -1 T GGG
    5 GGAG GAG GGA -1 F
CAG 3 CAGG AGG CAG -1 T AGG
..
GGG 1 GGGG GGG GGG -1 T GGG
    2 GGGA GGA GGG -1 T GGG, GGA
'''
def FindMatch(dna):
    mv=''
    for i,d in enumerate(in_dna):
        dr = d[1:kmer+1]
        #print " ",i,d, dr,d[:kmer], mv.find(dr), mv
        if (d[:kmer]==dna and mv.find(dr)<0):
            mv+=dr +","
    return mv

'''
i d   mv
0 AGG GGG
1 CAG AGG
2 GAG AGG
3 GGA GAG
4 GGG GGG, GGA
'''
for i,d in enumerate(dna):
    mv = FindMatch(d)
    #print i, d, mv, mv[:len(mv)-1]
    #print d + " -> " + mv[:len(mv)-1]
    ou_file.write(d + " -> " + mv[:len(mv)-1]+"\n")
    
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

