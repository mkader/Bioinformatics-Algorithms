'''
     Input: AACGATAGCGGTAGA$
     Output: 15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5
     Logic:
        {'A': ['ACGATAGCGGTAGA$', 'CGATAGCGGTAGA$', 'TAGCGGTAGA$', 'GCGGTAGA$', 'GA$', '$'], 'C': ['GATAGCGGTAGA$', 'GGTAGA$'], 'T': ['AGCGGTAGA$', 'AGA$'], 'G': ['ATAGCGGTAGA$', 'CGGTAGA$', 'GTAGA$', 'TAGA$', 'A$'], '$': ['']}

        {'A': 
          {'A':['CGATAGCGGTAGA$'], 
           'C': ['GATAGCGGTAGA$'], 
           'T': ['AGCGGTAGA$'], 
           'G': 
            {'A': ['$'], 
             'C': ['GGTAGA$']}, 
           '$': ['']}, 
         'C': 
          {'G': 
            {'A': ['TAGCGGTAGA$'], 
             'G': ['TAGA$']}}, 
         'T': 
          {'A': 
            {'G': 
              {'A': ['$'], 
               'C': ['GGTAGA$']}}}, 
         'G': 
          {'A': 
            {'T': ['AGCGGTAGA$'], 
             '$': ['']}, 
           'C': ['GGTAGA$'], 
           'T': ['AGA$'], 
           'G': ['TAGA$']}, 
         '$': {}}

        AACGATAGCG G T A G A $
        0123456789101112131415
     
        [15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5]
        aa
        ac
        cg
        ga
        at
        ta
        ag
        gc
        cg
        gg
        g
        t
        a
        g
        a
        $
'''

import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_9_7_data_set2.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

in_text=""
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(len(ldata)==0):
        break;
    else:
        in_text =ldata
 
#print in_text
#print ''
def Solution1():
    pos=5
    tlen =len(in_text)
    found=True
    while(found):
        found=False
        for i in range(0,tlen/2):
            ipa = in_text[i:pos+i]
            if(ipa in in_text[pos+i:]):
                #print "  ", trie
                pos+=1
                found=True
    print pos
    trie=[]            
    for i in range(0,tlen):
        trie.append(in_text[i:pos+i])
    print "done"

    print>>ou_file, [i[0] for i in sorted(enumerate(trie), key=lambda x:x[1])]
#Solution1()
#w_9_7_data_set2 - 0:02:35.756000

def Solution2():
    pos=1
    tlen =len(in_text)
    found=True
    while(found):
        found=False
        for i in range(0,tlen/2):
            ipa = buffer(in_text,i,pos+i)
            #print ipa
            if(ipa in buffer(in_text,pos+i,len(in_text))):
                #print "  ", trie
                pos+=1
                found=True
    print pos
    trie=[]            
    for i in range(0,tlen):
        trie.append(in_text[i:pos+i])
    print "done"

    print>>ou_file, [i[0] for i in sorted(enumerate(trie), key=lambda x:x[1])]
Solution2()    
    
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
