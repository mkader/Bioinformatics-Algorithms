'''
Input: Integers k and t, followed by a collection of strings Dna.
     3 5
     GGCGTTCAGGCA
     AAGAATCAGTCA
     CAAGGAGTTCGC
     CACGTCAATCAC
     CAATAATATTCG
Output: A collection of strings BestMotifs resulting from applying GREEDYMOTIFSEARCH(Dna,k,t) with
     pseudocounts. If at any step you find more than one Profile-most probable k-mer in a given string,
     use the one occurring first.
     TTC
     ATC
     TTC
     ATC
     TTC
'''
import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_3_5_data_set1.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_kmer = 0
in_dna=[]
in_result=[]
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

best_motif_score =in_m*in_kmer
best_motif= []
for k in range(0,len(in_dna[0])):
    dna_kmer = in_dna[0][k:k+in_kmer]
    #print k, kp
    if(len(dna_kmer)==in_kmer):
        motifs.append(dna_kmer)
        ScoreMotif()
        #print "     ",fdna #, d_pr_matrix , fdna, 0
        for i in range(1,len(in_dna)):
            max_probability_dna_kmer = -1
            dna_kmer=''
            for j in range(0,len(in_dna[i])):
                p = in_dna[i][j:j+in_kmer]
                if (len(p)==in_kmer):
                    probability_dna_kmer =1
                    for l in range(0,len(p)):
                        probability_dna_kmer*= profile_motif_matrix[p[l]][l]
                    #print "     ",i,in_dna[i], p, tot
                    if(probability_dna_kmer>max_probability_dna_kmer):
                        max_probability_dna_kmer = probability_dna_kmer
                        dna_kmer = p
            #print "     ",pkmer, ptot
            motifs.append(dna_kmer)
            motif_score = ScoreMotif()
            if(len(motifs)==in_m):
                if (motif_score<best_motif_score):
                    best_motif=motifs
                    best_motif_score = motif_score
                #print "     ",fdna, tot #, d_pr_matrix , pkmer, ptot
        motifs=[]
        profile_motif_matrix={}

#print    ftlv , fmlv
for i, f in enumerate(best_motif):
    print f

tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

