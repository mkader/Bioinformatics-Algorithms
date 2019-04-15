'''
     Input: A collection Patterns of k-mers.
             ATGCG
             GCATG
             CATGC
             AGGCA
     Output: The overlap graph Overlap(Patterns), in the form of an adjacency list.
             AGGCA -> GGCAT
             CATGC -> ATGCG
             GCATG -> CATGC
             GGCAT -> GCATG
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_4_2_data_set1.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_kmer = 0
in_patterns=[]
res=False
in_result=''
ldata = ''
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    
    if (len(ldata)==0 or res):
        res=True
        in_result += ldata + "\n"
    else:
        in_patterns.append(ldata)
    line+=1
#print in_patterns
#print in_result

in_patterns.sort()

#print in_patterns


used = [True] * len(in_patterns)

for i,pat in enumerate(in_patterns):
    k=1
    pr = pat[k:len(pat)]
    for j,mpat in enumerate(in_patterns):
        #print i, pat, j, mpat, k, pr, mpat[0:len(mpat)-k]
        if (used[j] and pr == mpat[0:len(mpat)-k]):
            used[j] = False
            #print used    
            #print " ", i, pat, j, mpat, mpat[0:len(mpat)-k]
            ou_file.write(pat + " -> " +mpat +"\n")
            #print>>ou_file,i,"\t - ",j
                
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

