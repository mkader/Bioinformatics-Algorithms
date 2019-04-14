'''
Recall that constructing Trie(Patterns) required O(|Patterns|) runtime and memory. Accordingly, the runtime and memory 
required to construct SuffixTrie(Text) are both equal to the combined length of all suffixes in Text. There are |Text| 
suffixes of Text, ranging in length from 1 to |Text| and having total length |Text|·(|Text|+1)/2, which is O(|Text|2). 
Thus, we need to reduce both the construction time and memory requirements of suffix tries to make them practical. 
Before doing so, you might like to see how useful suffix tries are by trying the following problem.

Find the longest repeat in a string.
     Input: ATATCGTTTTATCGTT.
     Output: A longest repeat in Text, i.e., a longest substring of Text that appears in Text more than once. =>TATCGTT
     Logic:
        A TATCGTTTTATCGTT
           CGTTTTATCGTT

        T ATCGTTTTATCGTT
          CGTTTTATCGTT
          TTTATCGTT
            ATCGTT
           ATCGTT

        C GTTTTATCGTT

        G TTTTATCGTT

        AT
        TA
'''

import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_9_3_data_set2.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 0
in_text=""
mpos ={}
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(len(ldata)==0):
        break;
    if(line==0):
        in_text=ldata
    line+=1
    #print mpos

###print in_text
###print in_patterns
###print mpos
###print ''

def RepeatedTimes(kmer):
    words = [in_text[i:i+kmer] for i in range(0, len(in_text), 1) if (len(in_text[i:i+kmer])==kmer)]
    from collections import Counter
    word = Counter(words)
    times = word.values()
    mtimes = max(times)
    #print>>ou_file,  n
    if (mtimes>1):
        #print>>ou_file,  n
        tmtimes = times.count(mtimes)
        fwords  = word.most_common(tmtimes)
        #print>>ou_file, " " ,fwords
        for fword in fwords:
            print>>ou_file, " ", fword[0]
        return True 
    return False
ml=len(in_text)/2
for n in range(ml,0,-1):
    if (RepeatedTimes(n)):
        break

        
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
