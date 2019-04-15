'''
You now have a method to assemble a genome, since the String Reconstruction Problem reduces to finding an Eulerian path 
in the de Bruijn graph generated from reads.

     Input: The adjacency list of a directed graph that has an Eulerian path.
         CTT -> TTA
         ACC -> CCA
         TAC -> ACC
         GGC -> GCT
         GCT -> CTT
         TTA -> TAC
    Output: An Eulerian path in this graph.
        GGCTTACCA
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_5_2_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_adjacency=[]
lpos = 0
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (len(ldata)==0):
        break
    else:
        ls = ldata.split()
        in_adjacency.append(ls[0] +  ls[2][-1])

print in_adjacency
#for i,d in enumerate(in_adjacency):
#    ou_file.write(d + "\n")
#ou_file.write("\n\n\n")
lpos = len(in_adjacency[0])-2     
print len(in_adjacency)
i=0            
tot_iadj = len(in_adjacency)
pos =1
while (1<tot_iadj):
    ia = in_adjacency[i]
    end_ia = ia[pos:len(ia)]
    match=False
    for j,ja in enumerate(in_adjacency):
        sta_ja = ja[0:len(ia)-pos]
        if (end_ia==sta_ja and ja != ia and len(end_ia)>lpos):
            in_adjacency.remove(ja)
            in_adjacency.remove(ia)
            in_adjacency.append(ia +  ja[len(sta_ja):len(ja)])
            #print "     ", ia, ja,  pos,len(ja), ja[len(sta_ja):len(ja)], i,len(sta_ja)
            i=-1
            tot_iadj = len(in_adjacency)
            #print tot_iadj
            #print in_adjacency
            match=True
            pos = 1
            break
    if(not match):
        pos+=1
        if (len(end_ia)==0):
            i+=1
            pos=1
    else:
        i+=1
    #print i , tot_iadj
print len(in_adjacency)
for i,d in enumerate(in_adjacency):
   print d
   ou_file.write(d + "\n")    
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

