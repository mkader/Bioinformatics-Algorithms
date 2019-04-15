'''
Our goal is to modify our previous algorithm to find DnaA boxes by identifying frequent k-mers, possibly with mismatches. 
Given strings Text and Pattern as well as an integer d, we define Countd(Text, Pattern) as the total number of occurrences of 
Pattern in Text with at most d mismatches. For example, Count1(AACAAGCTGATAAACATTTAAAGAG, AAAAA) = 4 because AAAAA 
appears four times in this string with at most one mismatch: AACAA, ATAAA, AAACA, and AAAGA. Note that two of these occurrences overlap.

A most frequent k-mer with up to d mismatches in Text is simply a string Pattern maximizing Countd(Text, Pattern) among all k-mers. 
Note that Pattern does not need to actually appear as a substring of Text; for example, as we saw above, AAAAA is the most 
frequent 5-mer with 1 mismatch in AACAAGCTGATAAACATTTAAAGAG, even though it does not appear in this string. Keep this in 
mind while solving the following problem:

Find the most frequent k-mers with mismatches in a string.
     Input: A string Text as well as integers k and d. (You may assume k = 12 and d = 3.) => ACGTTGCATGTCGCATGATGCATGAGAGCT 4 1
     Output: All most frequent k-mers with up to d mismatches in Text. => GATG ATGC ATGT
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)
in_file = open('w1_7_data_set3.txt', 'r')
ou_file = open('data_set_out1.txt', 'w')

line = 1
in_genome = "";
in_kmer =0
in_mistake = 0
in_result=""
for in_data in in_file:
    if (line==1):
    	line1 = (in_data.strip(' \t\n\r')).split()
    	in_genome = line1[0]
    	in_kmer = int(line1[1])
    	in_mistake = int(line1[2])
    if (line==3):
        print in_kmer, in_mistake, in_data
    line+=1    	

distinct_letters = "".join(set(in_genome))

def diff_letters(a,b):
    #ou_file.write("     " + str(process_patterns[j]) +"\n")
    count = 0
    for i in range(len(a)):
      if(a[i] != b[i]):
          count +=1
          if(count>in_mistake):
              return False
    return True    

genomes = [in_genome[i:i+in_kmer] for i in range(0, len(in_genome), 1) if len(in_genome[i:i+in_kmer]) ==in_kmer]
patterns = map("".join, itertools.product(distinct_letters, repeat=in_kmer))


mis_patterns=collections.defaultdict(list)
max_count =0
for i,iv in enumerate(patterns):
    count = 0
    for j,jv in enumerate(genomes):
        if diff_letters(iv,jv):
            count+=1
            #print>>ou_file,i,p,j,jv, count
    mis_patterns[iv]=count
    if count>0 and count>max_count:
        max_count = count
   
print max_count #, mis_patterns
for i,p in enumerate(mis_patterns):
    if mis_patterns[p]==max_count:
        print i,p, mis_patterns[p]

tend = datetime.datetime.now()        
print str(tend-tstart)
print "Done 1"
ou_file.close()


