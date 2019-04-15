'''
We say that position i in k-mers p1 … pk and q1 … qk is a mismatch if pi ? qi. For example, CGAAT and CGGAC have two mismatches. 
Our observation that a DnaA box may appear with slight variations leads to the following generalization of the Pattern Matching Problem:

Find all approximate occurrences of a pattern in a string.
     Input: Two strings Pattern and Text along with an integer d.
             ATTCTGGA
             CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
             3
      Output: All positions where Pattern appears in Text with at most d mismatches.
              6 7 26 27
'''

import collections   
import datetime

tstart = datetime.datetime.now()
   
in_file = open('w1_6_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_pattern = "";
in_genome = "";
in_mistake = 0
in_result=""
ou_result =""
for in_data in in_file:
    if (line==1):
    	in_pattern = in_data.strip(' \t\n\r')
    elif (line==2):
    	in_genome = in_data.strip(' \t\n\r')
    elif (line==3):
    	in_mistake = int(in_data.strip(' \t\n\r'))
    elif (line==5):
    	in_result = in_data.strip(' \t\n\r')	
    line+=1    	

print in_mistake
print in_result
print ""
kmer = len(in_pattern)

def FindMistake(v):
    mistake = 0
    for i in range(0, kmer, 1):
        if (v[i]!=in_pattern[i]):
            mistake+=1
            
            if(mistake>in_mistake):
                #print v, in_pattern, mistake, "F",i
                return False
    #print v, in_pattern, mistake ,"T", i
    return True


#genomes = [in_genome[i:i+kmer] for i in range(0, len(in_genome), 1)]
for i in xrange(len(in_genome)-kmer+1):
    v = in_genome[i:i+kmer]
    if FindMistake(v):
        ou_result+= str(i) + " "
        
print ou_result

tend = datetime.datetime.now()        
print str(tend-tstart)
