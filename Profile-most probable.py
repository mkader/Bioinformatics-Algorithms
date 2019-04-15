'''
     Input: A string Text, an integer k, and a k × 4 matrix Profile.
             ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
             5
             A C G T
             0.2 0.4 0.3 0.1
             0.2 0.3 0.3 0.2
             0.3 0.1 0.5 0.1
             0.2 0.5 0.2 0.1
             0.3 0.1 0.4 0.2
     Output: A Profile-most probable k-mer in Text.
            CCGAG
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_3_3_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_kmer = 0
in_dna=''
in_result=''
in_profile=[]
in_matrix=[]
res=False
ldata = ''
m=0
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (line==1):
        in_dna = ldata
    elif (line==2):
        in_kmer=int(ldata)
    elif (line==3):
        in_profile=ldata.split()    
    elif (line>1 and len(ldata)!=0):
        m+=1
        in_matrix.append(ldata)
    elif (line==0 or len(ldata)==0):
        line = -1
        in_result = ldata
    line+=1
    
print in_dna    
print in_kmer, in_profile, m
print in_result
#print dist_dna
#ou_file.write(in_result+"\n\n")

d_pr_matrix = {}
for i,p in enumerate(in_profile):
    pm=[]
    for j in range(0,m):
        pm.append((in_matrix[j].split())[i])
        #print p, (in_matrix[j].split())[i]
    #d_pr_matrix[p] =
    #print p
    d_pr_matrix[p]=pm
    
print d_pr_matrix


max_mp=0
max_dna=''
for i in range(0, len(in_dna)-in_kmer+1):
    p = in_dna[i:i+in_kmer]
    sum_mp=sum(float(d_pr_matrix[pl][j]) for j,pl in enumerate(p))
    #print j, p, pl, d_pr_matrix[pl], d_pr_matrix[pl][j], sum_mp
    #print p, sum_mp, ts
    if(sum_mp> max_mp):
        max_mp = sum_mp
        max_dna = p

print    max_mp,   max_dna   
                
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

