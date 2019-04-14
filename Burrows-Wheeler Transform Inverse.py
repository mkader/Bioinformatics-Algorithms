'''
Inverse Burrows-Wheeler Transform Problem:
     Input:  TTCCTAACG$A = > Output: TACATCACGT$
     
     Explanation  
     12123123113
     TTCCTAACG$A
     $AAACCCGTTT
     11231231123

     $1->T1->G1->C3->A2->C1->T3....
     $   T   G   C   A   C   T

     {'G1': 'C3', 'T2': '$1', 'T3': 'A3', 'T1': 'G1', 'A1': 'T2', 'A3': 'C2', 'A2': 'C1', 'C3': 'A2', 'C2': 'A1', 'C1': 'T3', '$1': 'T1'}
     $1 -> T1 $ $
     T1 -> G1 T T$
     G1 -> C3 G GT$
     C3 -> A2 C CGT$
     A2 -> C1 A ACGT$
     C1 -> T3 C CACGT$
     T3 -> A3 T TCACGT$
     A3 -> C2 A ATCACGT$
     C2 -> A1 C CATCACGT$
     A1 -> T2 A ACATCACGT$
     T2 -> $1 T TACATCACGT$
'''

import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_10_2_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

in_text=""
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(len(ldata)==0):
        break;
    else:
        in_text =ldata
rtext = sorted(in_text)
#print rtext
rdict={}
idict={}
bwta={}
ntext=""
for i,rt in enumerate(rtext):
    if (rt not in rdict.keys()):
        rdict[rt]=1
    else:
        rdict[rt]=rdict[rt]+1
    it =in_text[i]     
    if (it not in idict.keys()):
        idict[it]=1
    else:
        idict[it]=idict[it]+1
    #ntext+=str(ndict[t])
    bwta[rt+str(rdict[rt])]=it+str(idict[it])   
    #print rt+str(rdict[rt]),it,idict[it]
    #print rt, rdict[rt], it, idict[it]
#print bwta
dk='$1'
bwt=''
for i in range(0,len(rtext)):
    bwt=dk[0]+bwt
    #print dk,'->',bwta[dk], dk[0],bwt
    dk=bwta[dk]
#print bwt
print>>ou_file,bwt

    
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
