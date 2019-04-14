'''
Burrows-Wheeler Transform Matching
     Input: A string BWT(Text), followed by a collection of Patterns.
            TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC
            CCT CAC GAG CAG ATC
     Output: A list of integers, where the i-th integer corresponds to the number of substring matches of the i-th member of Patterns in Text.
             2 1 1 0 1
             
     Logic
      C$GGAGGTGCGCTTC
      GTG GCG CCC TGC

      0 1 0 1
      ACGGGCTTTGCGGC

      ACGGGCTT$TGCGGC
      GTG GCG CCC TGC

      2 1 0 2
      {'G6': 11, 'G5': 10, 'G4': 9, 'G3': 8, 'G2': 7, 'G1': 6, 'T2': 13, 'T3': 14, 'T1': 12, 'A1': 1, 'C3': 4, 'C2': 3, 'C1': 2, '$1': 0, 'C4': 5}

      GCGTGCCTGGTGCA$
       0  1  $ A 1  1 
       1  1  A C 1  2
       2  1  C G 1  6
       3  2  C G 2  7
       4  3  C G 3  8
       5  4  C C 2  3
       6  1  G T 1  12
       7  2  G T 2  13
       8  3  G $ 1  0
       9  4  G T 3  14
      10  5  G G 4  9
      11  6  G C 3  4 
      12  1  T G 5  10
      13  2  T G 6  11
      14  3  T C 4  5
      j  rp  r i ip ltf 

      G[i-> 0:14]=>[j-> 2,13]=>[ltf-> 6,11]
      T[i-> 6:11]=>[j-> 6, 9]=>[ltf->12,14]
      G[i->12:14]=>[j->12,13]=>[ltf->10,11]=11-10+1=2

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

in_file = open('w_10_3_data_set0.txt', 'r')
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
    elif(line==1):
        patterns=ldata.split(' ')
    line+=1
rtext = sorted(in_text)
#print ''.join(rtext)
rdict={}
bwtr={}
for i,rt in enumerate(rtext):
    if (rt not in rdict.keys()):
        rdict[rt]=1
    else:
        rdict[rt]=rdict[rt]+1
    #it =in_text[i]     
    bwtr[rt+str(rdict[rt])]=i   
    #print rt+str(rdict[rt]),i
#print bwtr 
rdict={}
ltf=[]
for i,rt in enumerate(in_text):
    if (rt not in rdict.keys()):
        rdict[rt]=1
    else:
        rdict[rt]=rdict[rt]+1
    ##bwtr[rt+str(rdict[rt])]=i   
    ltf.append(bwtr[rt+str(rdict[rt])])
#print ltf

def BWMATCHING(LastColumn, Pattern, LastToFirst):
    top = 0
    bottom = len(LastColumn)- 1
    #print Pattern,"\t",LastColumn,"\t"
    while (top <= bottom):
        if (len(Pattern)>0):
            symbol = Pattern[len(Pattern)-1]
            #print symbol,LastColumn[top:bottom+1],"\t",
            Pattern=Pattern[:len(Pattern)-1]
            if (symbol in LastColumn[top:bottom+1]):
                topIndex = LastColumn.find(symbol,top,bottom+1)
                bottomIndex = LastColumn.rfind(symbol,top,bottom+1)
                top = LastToFirst[topIndex]
                bottom = LastToFirst[bottomIndex]
                #print "\t",topIndex,"\t", bottomIndex, "\t",top, "\t",bottom
            else:
                return 0
        else:
            return bottom-top+1

for i,pattern in enumerate(patterns):
    times= BWMATCHING(in_text, pattern, ltf)
    #print times
    print>>ou_file,times ,
#print ''
    
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
