'''
Trie Construction.
     Input: A collection of strings Patterns.
            GGTA
            CG
            GGC
     
     Output: The adjacency list corresponding to Trie(Patterns), in the following format. If Trie(Patterns) has n nodes, first label 
             the root with 1 and then label the remaining nodes with the integers 2 through n in  any order you like. Each edge of 
             the adjacency list of Trie(Patterns) will be encoded by a triple: the first two members of the triple must be the integers 
             labeling the initial and terminal nodes of the edge, respectively; the third member of the triple must be the symbol labeling the edge.
             1 2 G
             2 3 G
             3 4 T
             4 5 A
             3 6 C
             1 7 C
             7 8 G
     
     Logic:
        CAGTCTAG
        CATGCCTA
        CCAAATGC
        CCCGGTAG
        CCCGGTGA
        CCGACTGT
        CCGCTGTA

        2C3A10G11T12C13T14A15G
        2C3A4T5G6C7C8T9A
        2CCAAATGC
        2CCCGGTAG
        2CCCGGTGA
        2CCGACTGT
        2CCGCTGTA

        GGTA
        CG
        GGC

        CG
        GGC
        GGTA
        CTA
        CGTR
        TAGR
        CGTA
        GGTRST
        GGCA
        GGTRTU

        GGTRST
        GGTRTU
        GGTA

        2G3G4T5A
        2G3G4T6R7S8T
        2G3G4T6R9T10U

        {2'G': 
          {3'G': 
            {4'T': 
              {5'A': [''], 
               6'R': 
                {7'S': 
                  {8'T': ['']},     
                 9'T': 
                  {10'U': ['']}}}}}}

        CG
        GGC
        GGTA
        CTA
        CGTR
        TAGR
        CGTA
        GGTRST
        GGCA
        GGTRTU

        C T A
          G
            TA
             R	

        G G C
              A
            T A
              R ST
                TU
        T AGR


        {'C': ['G', 'TA', 'GTA'], 'T': ['AGR'], 'G': ['GC', 'GTA', 'GTRST', 'GCA', 'GTRTU']}

        {'C': ['G':['T':['R','A']], 'T':['A']], 'T': ['AGR'], 'G': [G:['C':['A'], 'T':['A','R':['ST','TU']]}

        1   2C
        2C  3T
        3T  4A
        2C  5G
        5G  6T
        6T  7A
        6T  8R
        1   9T
        9T  10A
        9T  11G
        9T  12R
        1   13G
        13G  14G
        14G  15C
        15C 16A
        14G  17T
        17T 18A
        17T 19R
        19R 20S
        20S 21T
        19R 22T
        22T 23U

        {
         2'C':1 
          {3'T':2 { 4'A':3 [''] }, 
           5'G':2 
            {6'T':3 	
              { 7'A'4: [''],  		
                8'R'4: ['']} }
          }, 
         9'T'1: {'10A 11G 12R': ['']}, 
         13'G'1: 
          {14'G'2: 
            {15'C'3: 
              {16'A'4: ['']}, 
             17'T'3: 
              {18'A'4: [''], 
               19'R'4: 
                {20'S'5: {21'T'6: ['']}, 
                 22'T'5: {23'U'6: ['']}}
              }
            }
          }
         }

        2C5G
        2C5G6T7R
        2C5G6T8A
        2C3T4A
'''

import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_9_1_data_set4.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 0
in_patterns =[]
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(len(ldata)==0):
        break;
    else:
        in_patterns.append(ldata)
 
trie ={}
for i,ip in enumerate(in_patterns):
    fci =ip[0]
    ipa = ip[1:]
    if (fci in trie):
        trie[fci]+=[ipa]
    else:
        trie[fci]=[ipa]

#print trie
#print''

def ExtendTrie(epatterns):
    etrie ={}
    #print " 1 ", epatterns, len(epatterns),epatterns[0]
    if len(epatterns[0])==0 and len(epatterns)==2:
        etrie[epatterns[1]]=['']
        return etrie
    elif (len(epatterns))>1:
        for i,ip in enumerate(epatterns):
            if (len(ip)>0):
                fci =ip[0]
                ipa = ip[1:]
                if (fci in etrie):
                    etrie[fci]+=[ipa]
                else:
                    etrie[fci]=[ipa]
        for j,jp in enumerate(etrie):
            if(len(etrie[jp])>0):
                etrie[jp]=ExtendTrie(etrie[jp])
        return etrie
    else:
        if (len(epatterns[0])>0):
            etrie[epatterns[0]]=['']
            return etrie
        else:
            return [epatterns[0]]

for i,ip in enumerate(trie):
    trie[ip]=ExtendTrie(trie[ip])

#print trie
#print ''

leaf={}
node = 1
def DisplayTrie(ip,t,sn):
    global node
    if(not isinstance(t, list)):
        #print "  ",leaf[sn],node+1, ip#, " -1 ", sn, leaf
        print>>ou_file,leaf[sn],(node+1), ip
        sn=sn+1
        leaf[sn] = node+1
        for j,jp in enumerate(t):
            node+=1
            DisplayTrie(jp,t[jp],sn)
    else:
        for k,kp in enumerate(ip):
            node+=1
            print>>ou_file,node-1,node, kp
            #print "  ",leaf[sn], node, kp#, " -2 ", sn
        node=node-1
        return  ""    

for i,ip in enumerate(trie):
    #print ip,node
    leaf[0] = 1
    DisplayTrie(ip,trie[ip],0)
    node+=1
    leaf={}
    leaf[0] = 1
    #print leaf
    
    
       
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
