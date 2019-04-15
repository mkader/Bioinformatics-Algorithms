'''
Find substrings of a genome encoding a given amino acid sequence.
     Input: A DNA string Text and an amino acid string Peptide.
           ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
           MA
     Output: All substrings of Text encoding Peptide (if any such substrings exist).
           ATGGCC
           GGCCAT
           ATGGCC
'''

import collections   
import itertools
import datetime
import re

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_2_2_data_set1.txt', 'r')
in_codon = open('w_2_1_RNA_codon_table_1.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_dna = "";
in_kmer = 3
in_peptide = ""
in_result=""
ou_result =""
for in_data in in_file:
    if (line==1):
    	in_dna = in_data.strip(' \t\n\r')
    elif (line==2):
    	in_peptide = in_data.strip(' \t\n\r')
    elif (line>3):
    	in_result += in_data.strip(' \t\n\r') + "\n"
    line+=1    	

#ou_file.write(in_dna+"\n")
#ou_file.write(in_result+"\n")
#print in_dna,in_peptide
#print>>ou_file, in_peptide
#print in_result
#print ""

#codons = collections.defaultdict(list)
aminoacids = collections.defaultdict(list)
for in_data in in_codon:
    line = (in_data.strip(' \t\n\r')).split()
    if len(line)==2:
        condo,aminoacid = line
        #print  condo,aminoacid
        aminoacids[aminoacid].append(condo)
        #codons[condo].append(aminoacid)
    #else:    
    #    codons[condo].append('')
#print codons
#print ""
#print aminoacids
#print codons

def RDNA(dna):
    return dna.replace('T','U')

def DNA(rdna):
    return rdna.replace('U','T')

def Reverse(dna):
    rdna = dna
    rdna = rdna.replace("A","1")
    rdna = rdna.replace("G","2")
    rdna = rdna.replace("T","A")
    rdna = rdna.replace("1","T")
    rdna = rdna.replace("C","G")
    rdna = rdna.replace("2","C")
    return rdna[::-1]

rdna = RDNA(in_dna)
#print>>ou_file, 'rdna ',rdna

rev_rdna = RDNA(Reverse(in_dna))
#print>>ou_file, "rev_rdna ",rev_rdna


p=in_peptide[:1]
#print p, aminoacids[p]
pattern = aminoacids[p]
            
for p in in_peptide[1:]:
    #print aminoacids[p]
    patterno = [pa+aa for pa in pattern for aa in aminoacids[p]]
    pattern=patterno

#print pattern
'''
M = AUG = >
A = ['GCA', 'GCC', 'GCG', 'GCU'] = > ['AUGGCA', 'AUGGCC', 'AUGGCG', 'AUGGCU']
'''
#for j, pa in enumerate(pattern):
#    print>>ou_file, j, pa
#    ou_file.write(str(j) + " " + DNA(pa)+"\n")
    
ou_result =[]
#print pattern
for i, p in enumerate(pattern):
    #ou_file.write(str(rdna.find(p)) + "  " + p+"\n")
    if (rdna.find(p)>=0):
        #print DNA(p), [(a.start(), a.end()) for a in list(re.finditer(p, rdna))]
        ou_result +=  [DNA(p) for a in list(re.finditer(p, rdna))]
    if (rev_rdna.find(p)>=0):
        #print [(a.start(), a.end()) for a in list(re.finditer(p, rev_rdna))]
        ou_result +=[Reverse(DNA(p)) for a in list(re.finditer(p, rev_rdna))]

for j, pa in enumerate(ou_result):
    print pa        
#print ou_result
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

