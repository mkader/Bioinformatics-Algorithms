'''
     Input: Integers k and d, followed by a collection of strings Dna.
             3 1
             ATTTGGC
             TGCCTTA
             CGGTATC
             GAAAATT
    Output: All (k, d)-motifs in Dna.
            ATA ATT GTT TTT
    Logic:
          MOTIFENUMERATION(Dna, k, d)
              for each k-mer a in Dna
                  for each k-mer a’ differing from a by at most d mutations
                      if a’ appears in each string from Dna with at most d mutations
                          output a’
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_3_1_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_kmer = 0
in_dmut=0
in_dna=[]
in_result=''
res=False
ldata = ''
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (line==1):
        ldatav = ldata.split()
        in_kmer=int(ldatav[0])
        in_dmut=int(ldatav[1])
    elif (line>1 and len(ldata)!=0):
        in_dna.append(ldata)
    elif (line==0 or len(ldata)==0):
        line = -1
        in_result = ldata
    line+=1
    
    
#print in_kmer, in_dmut
#print in_result
#print in_dna
#print dist_dna
ou_file.write(in_result+"\n\n")
dist_dna ="ACTG"

motifs =  map("".join, itertools.product(dist_dna, repeat=in_kmer))

#print motifs
ou_motif=[]
def FindMistake(iv,kv):
    mistake = 0
    for i,v in enumerate(iv):
        if (v!=kv[i]):
            mistake+=1
    if(mistake<=in_dmut):
        #print iv, kv, mistake
        return True
    return False

##version 2 - good , fast
#convert dna to dna kmer
dnas={}
for d in in_dna:
    sd= [d[i:i+in_kmer] for i in range(0, len(d)-in_kmer+1, 1)]
    dnas[d] = sd
#check motifs of dnas
for iv in motifs:
    #print iv 
    k=0
    for j in dnas:
        #print "  ", j, dnas[j]
        find=False
        for jv in dnas[j]:
            find=FindMistake(iv,jv)
            #print "   ",iv, jv, find, k
            if (find):
                k+=1
                break
        if(not find): break
    if(k==len(dnas)):
        ou_motif.append(iv)                
#print ou_motif

####version 1 - good    
###for j1,dna1 in enumerate(in_dna):
###    for k in range(0, len(dna1)):
###        ou_file.write(dna1[k:k+in_kmer]+" ")
##
###ou_file.write("\n\n")
##for iv in motifs:
##    #iv = 'AACTA'
##    #ou_file.write(iv+" ")
##    #print j, iv
##    c=0
##    for j1,dna1 in enumerate(in_dna):
##        #print "     ", j1, c, dna1
##        for k in range(0, len(dna1)-in_kmer+1):
##            kv = dna1[k:k+in_kmer]
##            #print "         KV ",kv ,iv, k, c
##            if FindMistake(iv,kv):
##                c+=1            
##                #print "         RES " ,k, kv
##                break
##    #print j1,c
##    if(c-1==j1):
##        ou_motif.append(iv)
###ou_file.write("\n\n")
###print ou_motif
for j,om in enumerate(ou_motif):
    print om
    ou_file.write(om+" ")    
                
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

