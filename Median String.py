'''
      Pseudocode:
          MEDIANSTRING(Dna, k)
              BestPattern ? AAA…AA
              for each k-mer Pattern from AAA…AA to TTT…TT
                  if d(Pattern, Dna) < d(BestPattern, Dna)
                       BestPattern ? Pattern
              output BestPattern
     Input: An integer k, followed by a collection of strings Dna.
             3
             AAATTGACGCAT
             GACGACCACGTT
             CGTCAGCGCCTG
             GCTGAGCACCGG
             AGTACGGGACAG
      Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all k-mers Pattern.
            GAC
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_3_2_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_kmer = 0
in_dna=[]
in_result=''
res=False
ldata = ''
dist_dna=''
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (line==1):
        in_kmer=int(ldata)
    elif (line>1 and len(ldata)!=0):
        in_dna.append(ldata)
        dist_dna+=ldata
    elif (line==0 or len(ldata)==0):
        line = -1
        in_result = ldata
    line+=1
    
    
#print in_kmer, in_result
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
    return mistake

#convert dna to dna kmer
dnas={}
for d in in_dna:
    sd= [d[i:i+in_kmer] for i in range(0, len(d)-in_kmer+1, 1)]
    dnas[d] = sd


'''
3
AAATTGACGCAT
GACGACCACGTT
CGTCAGCGCCTG
GCTGAGCACCGG
AGTACGGGACAG

GAC

md_sum = 5*3= 15
AAA => AAATTGACGCAT => AGT 2(mismatch) 3(c =least mismatch), GTA 2 2, TAC 2 2,
ACG 2 2, CGG 3 2, GGG 3 2, GGA 2 2,GAC 2 2, ACA 1 2, CAG 2 1, sum_c = 1
AAA => GACGACCACGTT => ... 2(c=least mismatch), sum_c= 3
AAA => GCTGAGCACCGG => ... 2(c=least mismatch), sum_c= 5
AAA => CGTCAGCGCCTG => ... 2(c=least mismatch), sum_c= 7
(sum_c<=md_sum) => 7<15 =>  md_sum = 7, md_va = AAA
AAC => sum_c = 5 =>  => 5<7 =>  md_sum = 5, md_va = AAC
AAG => sum_c = 5 =>  => 5<7 =>  md_sum = 5, md_va = AAG
ACA => sum_c = 4 =>  => 5<7 =>  md_sum = 4, md_va = ACA
ACG => sum_c = 2 =>  => 2<5 =>  md_sum = 2, md_va = ACG
...
GAC => sum_c = 2 =>  => 2<5 =>  md_sum = 2, md_va = GAC

2 GAC
'''
###ou_file.write("\n\n")
md_sum= len(in_dna) * in_kmer
#print md_sum
md_va=''
for iv in motifs:
    sum_c=0
    for k in dnas:
        #print "     ",  k
        c=in_kmer
        for kv in dnas[k]:
            nm = FindMistake(iv,kv)
            #print "         RES " ,iv, kv, nm, c
            if(nm==0):
                c=0
                break
            elif(nm<c):
                c=nm
        sum_c+=c
        #print sum_c, md_sum
        if (md_sum>0 and sum_c>md_sum): break
    if(sum_c<=md_sum):
        md_sum = sum_c
        md_va= iv
    print sum_c, iv, md_sum,md_va

print md_sum,md_va    
                
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

