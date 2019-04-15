'''
Translate an RNA string into an amino acid string.
     Input: An RNA string Pattern. = > AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
     Output: The translation of Pattern into an amino acid string Peptide. => MAMAPRTEINSTRING
'''

#import collections   
#import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_2_1_data_set1.txt', 'r')
in_codon = open('w_2_1_RNA_codon_table_1.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_rna = "";
in_kmer = 3
in_result=""
ou_result =""
for in_data in in_file:
    if (line==1):
    	in_rna = in_data.strip(' \t\n\r')
    elif (line==3):
    	in_result = in_data.strip(' \t\n\r')
    line+=1    	

#ou_file.write(in_rna+"\n")
#ou_file.write(in_result+"\n")
print in_rna
print in_result
print ""

codons ={}
for in_data in in_codon:
    line = (in_data.strip(' \t\n\r')).split()
    if len(line)==2:
        codons[line[0]]=line[1]
    else:    
        codons[line[0]]=''
#print codons
#print ""

def FindStopPos(rna):
    #print rna
    lpos = 0    
    #for ck, cv in codons.iteritems():
    for ck in ['UGA','UAA', 'UAG']:
        #if(cv==''):
            pos = rna.rfind(ck)-30;
            #print ck, cv, pos
            if(pos>0 and pos>lpos):
                lpos =  pos
    #print lpos
    return lpos

def ProteinValue(in_rna30):
    #rnas30 = []
    rnas30 = [in_rna30[i:i+in_kmer] for i in range(0, len(in_rna30), 3)]
    #print rnas30
    #print len(rnas30)
   
    protein = ''
    for rna in rnas30:
        #print rna, codons[rna]
        protein +=codons[rna]
    
    return protein
    #print  ""
    
lpos = FindStopPos(in_rna)
in_rna30 = in_rna[lpos:lpos+30]
print lpos, in_rna30, len(in_rna)
protein30 =  ProteinValue(in_rna30)

in_rnarem = in_rna[:lpos]

#if (float(len(in_rnarem)%3.0)==0):
proteinrem = ProteinValue(in_rnarem)
##else:
##    lrna = len(in_rnarem)/2
##    in_rnarem1 = in_rnarem[0:lrna] 
##    in_rnarem2 = in_rnarem[lrna:len(in_rnarem)] 
##    print len(in_rnarem), in_rnarem, in_rnarem1, in_rnarem2

protein = proteinrem + protein30
print protein
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

#w_2_1_RNA_codon_table_1
'''
AAA K
AAC N
AAG K
AAU N
ACA T
ACC T
ACG T
ACU T
AGA R
AGC S
AGG R
AGU S
AUA I
AUC I
AUG M
AUU I
CAA Q
CAC H
CAG Q
CAU H
CCA P
CCC P
CCG P
CCU P
CGA R
CGC R
CGG R
CGU R
CUA L
CUC L
CUG L
CUU L
GAA E
GAC D
GAG E
GAU D
GCA A
GCC A
GCG A
GCU A
GGA G
GGC G
GGG G
GGU G
GUA V
GUC V
GUG V
GUU V
UAA 
UAC Y
UAG 
UAU Y
UCA S
UCC S
UCG S
UCU S
UGA 
UGC C
UGG W
UGU C
UUA L
UUC F
UUG L
UUU F
'''
