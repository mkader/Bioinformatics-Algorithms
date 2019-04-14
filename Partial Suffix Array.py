'''
A partial suffix array.
     Input: A string Text and a positive integer K.
            PANAMABANANAS$
            5 
     Output: SuffixArrayK(Text), in the form of a list of ordered pairs (i, SuffixArray(i)) for all nonempty entries in the partial suffix array.
             1,5
             11,10
             12,0
     Logic
        GCGTGCCTGGTGCA$
        5

        3,5
        8,0
        12,10

        GCGTGCCTGGTGCA$ 0  14 
        CGTGCCTGGTGCA$G 1  13 
        GTGCCTGGTGCA$GC 2  12 
        TGCCTGGTGCA$GCG 3   5 0 
        GCCTGGTGCA$GCGT 4   1
        CCTGGTGCA$GCGTG 5   6
        CTGGTGCA$GCGTGC 6  11
        TGGTGCA$GCGTGCC 7   4
        GGTGCA$GCGTGCCT 8   0 0
        GTGCA$GCGTGCCTG 9   8
        TGCA$GCGTGCCTGG 10  9
        GCA$GCGTGCCTGGT 11  2
        CA$GCGTGCCTGGTG 12 10 0
        A$GCGTGCCTGGTGC 13  3
        $GCGTGCCTGGTGCA 14  7
            in  rev
'''

import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_10_5_data_set2.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

in_text=""
line=0
in_k=0
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(len(ldata)==0):
        break;
    elif(line==0):
        in_text =ldata
    elif(line==1):
        in_k=int(ldata)
    line+=1
rtext = sorted(in_text)
tlen =len(in_text)

def Method1():
    trie=[]
    for i in range(0,tlen):
        trie.append(in_text[i:]+in_text[:i])
        #print trie[i], i

    #print in_text
    #print>>ou_file,trie    
    #print>>ou_file,in_text
    #print>>ou_file,""

    bwt=""
    trie=sorted(trie)
    for i in range(0,tlen):
        t = trie[i]
        tp = t.find('$')
        sa = in_text.find(t[:tp+1])
        #print t, tp, sa, sa%in_k
        if(sa%in_k == 0):
            print>>ou_file, str(i)+","+str(sa)

def Method2():
    trie=[]
    for i in range(0,tlen+1):
        for j in range(i,tlen+1):
            sv = in_text[i:j] 
            #print i,j, sv , in_text.find(sv), in_text.rfind(sv)
            if (in_text.find(sv) == in_text.rfind(sv)):
                trie.append(sv)
                break
            
    trie=sorted(trie)
    for i,t in enumerate(trie):
        sa = in_text.find(t)
        #print t, sa, sa%in_k
        if(sa%in_k == 0):
            print>>ou_file, str(i)+","+str(sa)
#fast
Method1()
#print>>ou_file,""
#Slow
#Method2()
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
