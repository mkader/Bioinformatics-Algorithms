'''
Input: Integers k, t, and N, followed by a collection of strings Dna.
     8 5 100
     CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
     GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
     TAGTACCGAGACCGAAAGAAGTATACAGGCGT
     TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
     AATCCACCAGCTCCACGTGCAATGTTGGCCTA
Output: The strings BestMotifs resulting from running GIBBSSAMPLER(Dna, k, t, N) with
     20 random starts. Remember to use pseudocounts!
     TCTCGGGG
     CCAAGGTG
     TACAGGCG
     TTCAGGTG
     TCCACGTG

Note: As with RANDOMIZEDMOTIFSEARCH, there is a very small chance that your algorithm may be implemented correctly 
but not return the correct answer. We suggest running your algorithm on another dataset if you do not get the correct 
answer the first time.

'''

import collections   
import itertools
import datetime
import random

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_3_7_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_kmer = 0
in_dna=[]
in_result=[]
in_ncount=0
res=False
ldata = ''
in_m=0
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (line==1):
        in_kmer = int(ldata.split()[0])
        in_m = int(ldata.split()[1])
        in_ncount = int(ldata.split()[2])
    elif (res==True or len(ldata)==0):
        res=True
        if (len(ldata)!=0):
            in_result.append(ldata)
    elif (line>=2):
        in_dna.append(ldata)    
    line+=1
    
print in_kmer, in_m, in_ncount
print in_dna    
print in_result
print ''

motifs=[]
profile_motif_matrix={}

def ScoreMotif():
    alist=[]
    clist=[]
    tlist=[]
    glist=[]
    for i in range(0,in_kmer):
        alist.append(1.00)
        clist.append(1.00)
        tlist.append(1.00)
        glist.append(1.00)
    #print  alist   
    for j, motif in enumerate(motifs):
        #print dna, dna[0]
        for i in range(0,in_kmer):
            single =motif[i]
            ac = single.count('A')
            cc = single.count('C')
            tc = single.count('T')
            gc = single.count('G')
            #print j, i, dna, sfdna, alist[i], ac, clist[i], cc, tlist[i], tc, glist[i], gc, j
            alist[i]=(alist[i]+float(ac))
            clist[i]=(clist[i]+float(cc))
            tlist[i]=(tlist[i]+float(tc))
            glist[i]=(glist[i]+float(gc))

        profile_motif_matrix['A'] =alist
        profile_motif_matrix['C'] =clist
        profile_motif_matrix['G'] =glist
        profile_motif_matrix['T'] =tlist

    score_motif=0
    if(len(motifs)==in_m):
        tlv=0
        for i in range(0,in_kmer):
            lv=0
            a = profile_motif_matrix['A'][i]
            c = profile_motif_matrix['C'][i]
            g = profile_motif_matrix['G'][i]
            t = profile_motif_matrix['T'][i]
            #print lv,a,c,g,t,tlv
            if(a>lv and a!=0):
                lv=a
            if(c>lv and c!=0):
                lv=c
            if(g>lv and g!=0):
                lv=g
            if(t>lv and t!=0):
                lv=t
            #print lv
            lv=in_m-lv   
            score_motif+=lv
        #print tlv,lv   
        
    for i in range(0,in_kmer):
        profile_motif_matrix['A'][i]/=(j+1.0+j+1.0)
        profile_motif_matrix['C'][i]/=(j+1.0+j+1.0)
        profile_motif_matrix['G'][i]/=(j+1.0+j+1.0)
        profile_motif_matrix['T'][i]/=(j+1.0+j+1.0)
        
    #if(len(motifs)==in_m):
        #print score_motif, motifs,  profile_motif_matrix
    return score_motif

#print len(in_dna[0])
#rl = random.sample(xrange(len(in_dna[0])), len(in_dna[0]))
#print rl
#rl = [9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
      #27,28,29,30,31,0,1,2,3,4,5,6,7,8]
#print rl, random.randrange(0,4) ,len(in_dna)

print len(in_dna[0])*in_m
random_best_motif_score =in_m*in_kmer
random_best_motif= []
random_list=[]
n=0
##if (len(in_dna[0])*in_m>1000):
##    ncount=1000
##else:
##    ncount =len(in_dna[0])*in_m
#print in_ncount    
while(n<in_ncount):
    best_motif_score =in_m*in_kmer
    best_motif= []
    
    rl = random.sample(xrange(len(in_dna[0])), len(in_dna[0]))
    print rl, len(in_dna[0])
    for r,k in enumerate(rl):
    #for k in range(0,len(in_dna[0])):
        dna_pos = random.randrange(0,in_m)
        rndnmr=str(k) +"-"+ str(dna_pos)
        if (rndnmr not in random_list):
            n+=1
            #print rndnmr
            random_list.append(rndnmr)
            dna_kmer = in_dna[0][k:k+in_kmer]
            #print k, kp
            if(len(dna_kmer)==in_kmer):
                motifs.append(dna_kmer)
                ScoreMotif()
                #print "     ",fdna #, d_pr_matrix , fdna, 0
                for i in range(1,len(in_dna)):
                    max_probability_dna_kmer = -1
                    dna_kmer=''
                    #for j in range(0,len(in_dna[i])):
                    for r,j1 in enumerate(rl):
                        j=rl[j1]
                        p = in_dna[i][j:j+in_kmer]
                        if (len(p)==in_kmer):
                            probability_dna_kmer =1
                            for l in range(0,len(p)):
                                probability_dna_kmer*= profile_motif_matrix[p[l]][l]
                            #print "     ",i,in_dna[i], p, tot
                            if(probability_dna_kmer>max_probability_dna_kmer):
                                max_probability_dna_kmer = probability_dna_kmer
                                dna_kmer = p
                    #print "     ",dna_kmer, motif_score, best_motif_score
                    motifs.append(dna_kmer)
                    motif_score = ScoreMotif()
                    #print "     ",dna_kmer, motif_score, best_motif_score
                    if(len(motifs)==in_m):
                        if (motif_score<best_motif_score):
                            best_motif=motifs
                            best_motif_score = motif_score
                        #print "     ",fdna, tot #, d_pr_matrix , pkmer, ptot
                motifs=[]
                profile_motif_matrix={}
            if (best_motif_score<random_best_motif_score):
                random_best_motif=best_motif
                random_best_motif_score = best_motif_score
            #print    k, dna_pos, dna_kmer, n, best_motif_score , best_motif
for i, f in enumerate(random_best_motif):
    print f

#print random_list
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

