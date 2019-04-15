'''
Input: Integers k and t, followed by a collection of strings Dna.
     3 5
     GGCGTTCAGGCA
     AAGAATCAGTCA
     CAAGGAGTTCGC
     CACGTCAATCAC
     CAATAATATTCG
Output: A collection of strings BestMotifs resulting from applying GREEDYMOTIFSEARCH(Dna,k,t). 
If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.
     CAG
     CAG
     CAA
     CAA
     CAA
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_3_4_data_set1.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_kmer = 0
in_dna=[]
in_result=[]
#in_profile=[]
#in_matrix=[]
res=False
ldata = ''
in_m=0
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (line==1):
        in_kmer = int(ldata.split()[0])
        in_m = int(ldata.split()[1])
    elif (res==True or len(ldata)==0):
        res=True
        if (len(ldata)!=0):
            in_result.append(ldata)
    elif (line>=2):
        in_dna.append(ldata)    
    line+=1
    
print in_kmer, in_m
#print in_dna    
print in_result
print ''

motifs=[]
profile_motif_matrix={}

'''
GGCGTTCAGGCA
GGC A[0.0, 0.0, 0.0] C[0.0, 0.0, 1.0] T[0.0, 0.0, 0.0] G[1.0, 1.0, 0.0]
    => ['AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
    => ['GGC', 'AAG', 'CAA', 'CAC', 'CAA'] (max_probability_dna_kmer)
    => A[1.0, 4.0, 2.0], C[3.0, 0.0, 2.0], T[0.0, 0.0, 0.0], G[1.0, 1.0, 1.0]/5(in_m)
        => max(Col1 1,3,0,1) => 3 - 5(in_m) = 2 (score_motif)
        => max(Col2 4,0,0,1) => 4 - 5(in_m) = 1 (score_motif)
        => max(Col3 2,2,0,1) => 2 - 5(in_m) = 3 (score_motif) => 6.0
    => A[0.2, 0.8, 0.4], C[0.6, 0.0, 0.4], T[0.0, 0.0, 0.0], G[0.2, 0.2, 0.2]
GCG A[0.0, 0.0, 0.0] C[0.0, 1.0, 0.0] T[0.0, 0.0, 0.0] G[1.0, 0.0, 1.0]
    => ['AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
    => ['GCG', 'AAG', 'CAA', 'CAC', 'CAA'] (max_probability_dna_kmer)
    => A[0.2, 0.8, 0.4], C[0.6, 0.2, 0.2], T[0.0, 0.0, 0.0], G[0.2, 0.0, 0.4] (/5)
...
GCA A[0.0, 0.0, 1.0] C[0.0, 1.0, 0.0] T[0.0, 0.0, 0.0] G[0.0, 0.0, 1.0]
    => ['AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
    => ['GCA', 'AAG', 'CAA', 'CAC', 'CAA'] (max_probability_dna_kmer)
    => A[0.2, 0.8, 0.6], C[0.6, 0.2, 0.2], T[0.0, 0.0, 0.0], G[0.2, 0.0, 0.2] (/5)
'''
def ScoreMotif():
    alist=[]
    clist=[]
    tlist=[]
    glist=[]
    for i in range(0,in_kmer):
        alist.append(0.00)
        clist.append(0.00)
        tlist.append(0.00)
        glist.append(0.00)
    #print  motifs
    for j, motif in enumerate(motifs):
        #print dna, dna[0]
        for i in range(0,in_kmer):
            single =motif[i]
            ac = single.count('A')
            cc = single.count('C')
            tc = single.count('T')
            gc = single.count('G')
            #print j, i, alist[i], ac, clist[i], cc, tlist[i], tc, glist[i], gc
            alist[i]=(alist[i]+float(ac))
            clist[i]=(clist[i]+float(cc))
            tlist[i]=(tlist[i]+float(tc))
            glist[i]=(glist[i]+float(gc))
        #print j, alist  , clist  ,tlist,glist
        profile_motif_matrix['A'] =alist
        profile_motif_matrix['C'] =clist
        profile_motif_matrix['G'] =glist
        profile_motif_matrix['T'] =tlist
        #print profile_motif_matrix

    score_motif=0
    if(len(motifs)==in_m):
        for i in range(0,in_kmer):
            lv=0
            a = profile_motif_matrix['A'][i]
            c = profile_motif_matrix['C'][i]
            g = profile_motif_matrix['G'][i]
            t = profile_motif_matrix['T'][i]
            #print " ",lv,a,c,g,t, score_motif
            if(a>lv and a!=0):
                lv=a
            if(c>lv and c!=0):
                lv=c
            if(g>lv and g!=0):
                lv=g
            if(t>lv and t!=0):
                lv=t
            #print " ", lv
            lv=in_m-lv   
            score_motif+=lv
        #print tlv,lv   

    #print "j = ",j, profile_motif_matrix    , len(motifs),in_m
    #print profile_motif_matrix
    for i in range(0,in_kmer):
        profile_motif_matrix['A'][i]/=(j+1.0)
        profile_motif_matrix['C'][i]/=(j+1.0)
        profile_motif_matrix['G'][i]/=(j+1.0)
        profile_motif_matrix['T'][i]/=(j+1.0)
        
    #if(len(motifs)==in_m):
        #print score_motif, motifs,  profile_motif_matrix
    #print " ",profile_motif_matrix
    #print score_motif
    return score_motif

'''
['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
GGC
    => motifs[GGC]
    =>'AAGAATCAGTCA' => AAG 0 (probability_dna_kmer), AGA 0, GAA 0, ...
        => AAG 0 (max_probability_dna_kmer)
        => motifs[GGC, AAG]
    =>'CAAGGAGTTCGC' => CAA 0 (probability_dna_kmer), AAG 0, AGG 0, ...
        => CAA 0 (max_probability_dna_kmer)
        => motifs[GGC, AAG, CAA]
    ...
    motifs['GGC', 'AAG', 'CAA', 'CAC', 'CAA']
        => motif_score = 6.0
        => best_motif ['GGC', 'AAG', 'CAA', 'CAC', 'CAA'], best_motif_score 6.0
    
GCG
    => motifs[GCG]
    =>'AAGAATCAGTCA' => AAG 0 (probability_dna_kmer), AGA 0, GAA 0, ...
        => AAG 0 (max_probability_dna_kmer)
        => motifs[GCG, AAG]
    =>'CAAGGAGTTCGC' => CAA 0 (probability_dna_kmer), AAG 0, AGG 0, ...
        => CAA 0 (max_probability_dna_kmer)
        => motifs[GCG, AAG, CAA]
    ...
    motifs['GGC', 'AAG', 'CAA', 'CAC', 'CAA']
        => motif_score = 6.0
        => best_motif ['GGC', 'AAG', 'CAA', 'CAC', 'CAA'], best_motif_score 6.0
...
CAG
    => motifs[CAG]
    =>'AAGAATCAGTCA' => AAG 1.x (probability_dna_kmer), AGA 1.x, ... CAG 1...
        => CAG 1 (max_probability_dna_kmer)
        => motifs[CAG, CAG]
    =>'CAAGGAGTTCGC' => CAA 0 (probability_dna_kmer), AAG 0, AGG 0, ...
        => CAA 0 (max_probability_dna_kmer)
        => motifs[CAG, CAG, CAA]
    ...
    motifs['CAG', 'CAG', 'CAA', 'CAC', 'CAA']
        => motif_score = 3.0
        => best_motif ['CAG', 'CAG', 'CAA', 'CAC', 'CAA'], best_motif_score 3.0

ans ['CAG', 'CAG', 'CAA', 'CAC', 'CAA']
'''
best_motif_score =in_m*in_kmer
best_motif= []
for k in range(0,len(in_dna[0])-in_kmer+1):
    dna_kmer = in_dna[0][k:k+in_kmer]
    motifs.append(dna_kmer)
    ScoreMotif()
    #print k, dna_kmer, motifs
    #print "     ",fdna #, d_pr_matrix , fdna, 0
    for i in range(1,len(in_dna)):
        max_probability_dna_kmer = -1
        dna_kmer=''
        #print " ",i, in_dna[i]
        for j in range(0,len(in_dna[i])-in_kmer+1):
            p = in_dna[i][j:j+in_kmer]
            #print "  ", j,p
            probability_dna_kmer =1
            for l in range(0,len(p)):
                probability_dna_kmer*= profile_motif_matrix[p[l]][l]
                #print "   ", l, p[l], profile_motif_matrix[p[l]], profile_motif_matrix[p[l]][l], probability_dna_kmer
            #print "   ", j, p, probability_dna_kmer
            if(probability_dna_kmer>max_probability_dna_kmer):
                max_probability_dna_kmer = probability_dna_kmer
                dna_kmer = p
        motifs.append(dna_kmer)
        motif_score = ScoreMotif()
        #print " ",dna_kmer, max_probability_dna_kmer, motifs
        if(len(motifs)==in_m):
            if (motif_score<best_motif_score):
                best_motif=motifs
                best_motif_score = motif_score
            #print "  ",best_motif, best_motif_score, motif_score
    motifs=[]
    profile_motif_matrix={}


#print    best_motif_score , best_motif
for i, f in enumerate(best_motif):
    print f

tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

