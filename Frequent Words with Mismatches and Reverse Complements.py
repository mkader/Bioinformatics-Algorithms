'''
Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.
      Input: A DNA string Text as well as integers k and d.
           ACGTTGCATGTCGCATGATGCATGAGAGCT
           4 1
      Output: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible k-mers.
           ATGT ACAT
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w1_8_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_genome = "";
in_kmer =0
in_mistake = 0
in_result=""
ou_result =""
for in_data in in_file:
    if (line==1):
    	in_genome = in_data.strip(' \t\n\r')
    elif (line==2):
        line2 = (in_data.strip(' \t\n\r')).split()
        in_kmer = int(line2[0])
        in_mistake = int(line2[1])
    elif (line==4):
    	in_result = in_data.strip(' \t\n\r')
    line+=1    	

distinct_letters = "".join(set(in_genome))
ou_file.write(in_genome+"\n")
ou_file.write(in_result+"\n")
print in_genome
print in_kmer
print in_mistake
print in_result
#print distinct_letters
print ""

pos_genomes = [in_genome[i:i+in_kmer] for i in range(0, len(in_genome), 1) if len(in_genome[i:i+in_kmer]) == in_kmer]
#print pos_genomes
#print len(pos_genomes)
#print  ""

patterns = map("".join, itertools.product(distinct_letters, repeat=in_kmer))
#print patterns
print len(patterns)
#print ""

def diff_letters(a,b):
    #ou_file.write("     " + str(process_patterns[j]) +"\n")
    count = 0
    for i in range(len(a)):
      if(a[i] != b[i]):
          count +=1
          if(count>in_mistake):
              return False
    return True

def Reverse(in_str):
    ou_str = in_str
    ou_str = ou_str.replace("A","1")
    ou_str = ou_str.replace("G","2")
    ou_str = ou_str.replace("T","A")
    ou_str = ou_str.replace("1","T")
    ou_str = ou_str.replace("C","G")
    ou_str = ou_str.replace("2","C")
    return ou_str[::-1]

reverse_pos_genomes = []
for j,g in enumerate(pos_genomes):
    rev = Reverse(g)
    #if(pos_genomes.count(rev)==0):
    reverse_pos_genomes.append(rev)
    
print pos_genomes
print reverse_pos_genomes
#print len(reverse_pos_genomes)
#print  ""

genomes = pos_genomes + reverse_pos_genomes
#print genomes
print len(genomes)
#print  ""
    
mis_patterns=collections.defaultdict(list)
max_count = 0
for i,pp in enumerate(patterns):
    ou_file.write(str(i) + " " +pp+"\n")
    count = 0
    for j,g in enumerate(genomes):
       if(diff_letters(pp,g)):
            count+=1
    mis_patterns[pp]=count
    if count>0 and count>max_count:
        max_count = count
	    
print max_count #, mis_patterns
for i,p in enumerate(mis_patterns):
    if mis_patterns[p]==max_count:
        print i,p, mis_patterns[p]

tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

