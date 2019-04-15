'''
As the question on the preceding step illustrates, not every Eulerian path in the paired de Bruijn graph 
constructed from (k,d)-mer composition spells out a solution of the String Reconstruction from Read-Pairs Problem.

The String Reconstruction from Read-Pairs Problem.
     Input: An integer d followed by a collection of paired k-mers PairedReads.
         2
         GAGA|TTGA
         TCGT|GATG
         CGTG|ATGT
         TGGT|TGAG
         GTGA|TGTT
         GTGG|GTGA
         TGAG|GTTG
         GGTC|GAGA
         GTCG|AGAT
     Output: A string Text with (k, d)-mer composition equal to PairedReads.
           GTGGTCGTGAGATGTTGA
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_5_4_data_set3.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 0
in_pkmer=[]
in_skmer=[]
in_kmer={}
bkmer=[]
in_distance = 0
okmer=[]
i=0
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (len(ldata)==0):
        break
    elif (line==0):
        in_distance =int(ldata)
    else:
        ls = ldata.split("|")
        in_kmer[i]=[ls[0],ls[1]]
        i+=1
    line+=1

bkmer=[False]*len(in_kmer)
#print in_kmer
#print bkmer
#print ''

i=0
pos = len(in_kmer[0][0])-1
while(bkmer.count(False)>1):
    if(not bkmer[i]):
        ikmer = in_kmer[i][0]
        ikmer1 = in_kmer[i][1]
        ek = ikmer[len(ikmer)-pos:len(ikmer)]
        ek1 = ikmer1[len(ikmer1)-pos:len(ikmer1)]
        #print i, ikmer,  ek
        for j in range(0,len(in_kmer)):
            if(not bkmer[j]):
                jkmer = in_kmer[j][0]
                jkmer1 = in_kmer[j][1]
                sk = jkmer[0:pos]
                sk1 = jkmer1[0:pos]
                if(ek==sk and ek1==sk1):
                    #print " ", i, ikmer,  ek, j, jkmer, sk
                    #print i,j ,bkmer.count(False)
                    npref =ikmer+jkmer[pos:len(jkmer)]
                    nsuff =in_kmer[i][1]+in_kmer[j][1][pos:len(jkmer)]
                    in_kmer[i][0]=npref
                    in_kmer[i][1]=nsuff
                    #print " ", i, ikmer,  ek, j, jkmer, sk,npref,nsuff
                    bkmer[j]=True
                    #print in_kmer
                    #print bkmer
                    #print ''
                    i=-1
                    break
    i+=1
    #print bkmer.count(False), i


bpos = bkmer.index(False)
pre = in_kmer[bpos][0]
suf = in_kmer[bpos][1]
res = pre+suf[len(suf)-(pos+1+in_distance):len(suf)]
print bkmer.count(False),pos,in_distance ,len(pre),len(bkmer),len(bkmer)+pos
#ou_file.write(pre+"\n")
#ou_file.write(suf+"\n")
ou_file.write(res+"\n\n")


tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

