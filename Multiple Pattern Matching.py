'''
Multiple Pattern Matching Problem.
     Input: A string Text followed by a collection of strings Patterns.
             AATCGGGTTCAATCGGGGT
             ATCG
             GGGT
     Output: All starting positions in Text where a string from Patterns appears as a substring.
             1 4 11 15
     
     Logic
       AATCGGGTTCAATCGGGGT
        {'A': 0, 'C': 4, 'T': 14, 'G': 7}

           A  A  A  A  C  C  C  G  G  G  G  G  G  G  T  T  T  T  T
        A [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4]
        C [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]
        $ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        G [0, 0, 0, 0, 0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 7]
        T [0, 0, 0, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5]
           A  A  T  C  G  G  G  T  T  C  A  A  T  C  G  G  G  G  T
           0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18

        GCGTGCCTGGTGCA
        GTG
        GCG
        CCC 
        TGC

        2 1 0 2

        ACGGGCTT$TGCGGC
        GTG GCG CCC TGC

        2 1 0 2

        {'A': 1, 'C': 2, '$': 0, 'G': 6, 'T': 12}
        {'G6': 11, 'G5': 10, 'G4': 9, 'G3': 8, 'G2': 7, 'G1': 6, 'T2': 13, 'T3': 14, 'T1': 12, 'A1': 1, 'C3': 4, 'C2': 3, 'C1': 2, '$1': 0, 'C4': 5}

        $ [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
        A [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        C [0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4]
        G [0, 0, 0, 1, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5, 6, 6]
        T [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 3, 3, 3, 3, 3]

        GCGTGCCTGGTGCA$      $ A C G T
         0  1  $ A 1  1   0  0 0 0 0 0
         1  1  A C 1  2   1  0 1 1 0 0
         2  1  C G 1  6   2  0 1 1 0 0
         3  2  C G 2  7      0 1 1 1 0
         4  3  C G 3  8      0 1 1 2 0 
         5  4  C C 2  3      0 1 1 3 0
         6  1  G T 1  12  6  0 1 2 3 0
         7  2  G T 2  13     0 1 2 3 1
         8  3  G $ 1  0      0 1 2 3 2
         9  4  G T 3  14     1 1 2 3 2
        10  5  G G 4  9      1 1 2 3 3
        11  6  G C 3  4      1 1 2 4 3
        12  1  T G 5  10  12 1 1 3 4 3
        13  2  T G 6  11     1 1 3 5 3
        14  3  T C 4  5      1 1 3 6 3
        15                   1 1 4 6 3
        j  rp  r i ip ltf fc co 

        G[i->j 0:14]=>[j->fc+co|j  6+0, 6+6-1]=>[ltf-> 6,11]
        T[i->j 6:11]=>[j->fc+co|j 12+0,12+3-1]=>[ltf->12,14]
        G[i->j12:14]=>[j->fc+co|j 6+4,6+6-1]=>[ltf->10,11]=11-10+1=2

        g -6,11
        c-4,4
        g-8,8 =1

        c-2,5
        c-6,3
        c-   =0
'''

import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_10_6_data_set2.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

in_text=""
line=0
patterns=[]
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(len(ldata)==0):
        break;
    elif(line==0):
        in_text =ldata
    else:
        patterns.append(ldata)
    line+=1

oin_text =in_text

in_text+='$'
#print in_res
tlen =len(in_text)
trie=[]  
for i in range(0,tlen):
    trie.append(in_text[i:]+in_text[:i])

#for i in range(0,tlen):
#    print>>ou_file, trie[i]
#print>>ou_file,""

bwt=""
trie=sorted(trie)
for i in range(0,tlen):
    #print>>ou_file, trie[i]
    bwt+=trie[i][tlen-1:tlen]
    #print>>ou_file,trie[i][tlen-1:tlen]
#print>>ou_file,in_text
#print>>ou_file,""
#print>>ou_file,bwt
#print>>ou_file,""

in_text = bwt


rtext = sorted(in_text)
focc={}
for i,rc in enumerate(rtext):
    if (rc not in focc.keys()):
        focc[rc]=i
#print focc

def FillMatrix(tc, ti):
    global bwt
    for i,t in enumerate(set(in_text)):
        if (tc!=t):
            bwt[t][ti+1]=bwt[t][ti]

#print patterns
#print in_text, set(in_text)
rd=ra=rc=rg=rt=0
bwt={}
for i,t in enumerate(set(in_text)):
    bwt[t]=map(int,list('0'*(len(in_text)+1)))

for i in range(0,len(in_text)):
    #print>>ou_file,rtext[i],in_text[i]
    rti=in_text[i]
    bwt[rti][i+1]=bwt[rti][i]+1
    FillMatrix(rti,i)
    #print i, rti, rd,ra,rc,rg,rt
#print    bwt
#for i,kv in enumerate(sorted(bwt.keys())):
#    print kv,bwt[kv]

ou_pos=[]
def PrintTrie(top,bottom):
    global oin_text
    oin_text+='$'
    #print "Range"
    for i in range(top, bottom+1):
        #print i, trie[i]
        t = trie[i]
        tp = t.find('$')
        sa = oin_text.find(t[:tp+1])
        ou_pos.append(sa)
        #print sa
        #print i, t, tp, sa, oin_text
    
def  BETTERBWMATCHING(FirstOccurrence, LastColumn, Pattern, Count):
    top = 0
    bottom = len(LastColumn)- 1
    while (top <= bottom):
        if (len(Pattern)>0):
            symbol = Pattern[len(Pattern)-1]
            Pattern=Pattern[:len(Pattern)-1]
            #print top, bottom, symbol
            if (symbol in LastColumn[top:bottom+1]):
                top = FirstOccurrence[symbol] +Count[symbol][top]
                bottom = FirstOccurrence[symbol] +Count[symbol][bottom+1]-1
                #print " ", top, bottom
            else:
                return 0
        else:
            PrintTrie(top,bottom)
            return bottom-top+1

for i,pattern in enumerate(patterns):
    times= BETTERBWMATCHING(focc,in_text, pattern, bwt)
    #print pattern, times
    #print>>ou_file,times ,
#print ''

for i,op in enumerate(sorted(ou_pos)):
    print>>ou_file,op,

tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
