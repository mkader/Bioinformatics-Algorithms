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

in_file = open('w_4_3_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_kmer = 0
in_dna=''
res=False
in_result=''
ldata = ''
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (line==1):
        in_kmer = int(ldata)
    elif (line==2):
        in_dna = ldata
    if (len(ldata)==0 or res):
        res=True
        in_result += ldata + "\n"
    line+=1

print in_kmer, in_dna
#print in_result
print ''

'''
AAGATTCTCTAC => [AAGA (AAG, AGA)] [AGAT (AGA, GAT)] ...
kdna => ['AAGA', 'AGAT', 'GATT', 'ATTC', 'TTCT', 'TCTC', 'CTCT', 'TCTA', 'CTAC', 'TAC']
ldna => ['AAG', 'AGA', 'GAT', 'ATT', 'TTC', 'TCT', 'CTC', 'TCT', 'CTA', 'TAC']
rdna => ['AGA', 'GAT', 'ATT', 'TTC', 'TCT', 'CTC', 'TCT', 'CTA', 'TAC', 'TAC']
sort
['AAGA', 'AGAT', 'ATTC', 'CTAC', 'CTCT', 'GATT', 'TAC', 'TCTA', 'TCTC', 'TTCT']
['AAG', 'AGA', 'ATT', 'CTA', 'CTC', 'GAT', 'TAC', 'TCT', 'TCT', 'TTC']
['AGA', 'ATT', 'CTA', 'CTC', 'GAT', 'TAC', 'TAC', 'TCT', 'TCT', 'TTC']
'''
rdna = []
ldna = []
kdna = []
for i in range(0,len(in_dna)):
    dna = in_dna[i:i+in_kmer]
    if (len(dna)>=in_kmer-1):
        kdna.append(dna)
        tdna = dna[0:in_kmer-1]
        ldna.append(tdna)
        if (len(dna)==in_kmer):
            mdna = dna[1:in_kmer] 
        else:
            mdna = dna
        rdna.append(mdna)

kdna.sort()
ldna.sort()
rdna.sort()
#print kdna
#print ldna
#print rdna
#print len(kdna), len(ldna), len(rdna)

'''
i lpat return mdnas
0 AAG  -1     []
1 AGA  -1     [AAG AGA]
...
3 CTA  -1     [AAG AGA, AGA GAT, ATT TTC]
        3     [AAG AGA, AGA GAT, ATT TTC, CTA TAC]
....
'''
def CheckValue(lpat):
   for i,md in enumerate(mdnas):
       md0 = md.split()[0]
       #print "    ", md, md0, lpat
       if(md0==lpat):
           return i
   return -1     

'''
(lp=rp && kp=rpat) = C
i lpat lp kp  j rpat rp  C mdnas       pos
0 AAG  AG AGA 0 AGA  AG  T AAG AGA     -1
              ...
              9 TTC  TT  F
1 AGA  GA GAT 4 GAT  GA  T AGA GAT     -1                   
2 ATT  TT TTC 9 TTC  TT  T ATT TTC     -1
3 CTA  TA TAC 5 TAC  TA  T CTA TAC     -1
              6 TAC  TA  T              3,mdnas[3].find(rpat)=F   
...
7 TCT  CT CTA 2 CTA  CT  T TCT CTA     -1
8 TCT  CT CTC 3 CTC  CT  T TCT CTA,CTC  6,mdnas[6].find(rpat)=T   

mdnas =>
['AAG AGA', 'AGA GAT', 'ATT TTC', 'CTA TAC', 'CTC TCT',
'GAT ATT', 'TCT CTA,CTC', 'TTC TCT']
'''
k= 1
mdnas=[]
for i,lpat in enumerate(ldna):
    lp = lpat[k:len(lpat)]
    kp = kdna[i][1:in_kmer]
    #print i, lpat, lp, kp
    #print mdnas
    match = ''
    for j,rpat in enumerate(rdna):
        rp =rpat[0:len(rpat)-k]
        #print " ", j, rpat, rp
        if (lp == rp and kp == rpat):
            pos = CheckValue(lpat)
            #print "  ", pos
            if (pos==-1):
                mdnas.append(lpat + " " + rpat)
            else:
                #print "   ", mdnas[pos].find(rpat)
                if(mdnas[pos].find(rpat)<0):
                    mdnas[pos]+= "," + rpat
                    
print mdnas
for i,mdna in enumerate(mdnas):
    lp =mdna.split()
    res=''
    for j,l in enumerate(lp):
        if(j==0):
            res+=l+" -> "
        elif (j==len(lp)-1):
            res+= l
        else:
            res+= l+","
    #print res
    ou_file.write(res+"\n")


tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

