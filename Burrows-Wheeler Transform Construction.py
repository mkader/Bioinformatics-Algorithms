'''
Construct the Burrows-Wheeler transform of a string.
     Input: GCGTGCCTGGTCA$ =>  Output: ACTGGCT$TGCGGC
     Input: ACGGGCTTTGCGGC$ => Output: ACTGGCT$TGCGGC
     Input: panamabananas$ => Output: panamabananas$
'''

import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_10_1_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

in_text=""
in_res=""
line=0
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    #if(len(ldata)==0):
    if(line==4):
        break;
    #else:
    elif(line==0):
        in_text =ldata
    elif(line==3):
        in_res =ldata    
    line+=1
#print in_res
tlen =len(in_text)
trie=[]  
for i in range(0,tlen):
    trie.append(in_text[i:]+in_text[:i])

#for i in range(0,tlen):
#    print>>ou_file, trie[i]
#print>>ou_file,""

bwt=""
trie=sorted(trie)
for i in range(0,tlen):
    #print>>ou_file, trie[i]
    bwt+=trie[i][tlen-1:tlen]
    #print>>ou_file,trie[i][tlen-1:tlen]
#print>>ou_file,""
print>>ou_file,bwt
print>>ou_file,""

##Need to check this  code
##pos=1
##found=True
##while(found):
##    found=False
##    for i in range(0,tlen/2):
##        ipa = in_text[i:pos+i]
##        if(ipa in in_text[pos+i:]):
##            #print "  ", trie
##            pos+=1
##            found=True
##print pos
##trie=[]            
##for i in range(0,tlen):
##    if (i==2128 or i==2129):
##        print i,in_text[i:pos+i]
##    trie.append(in_text[i:pos+i])
##
###for i in range(0,tlen):
###    print>>ou_file, trie[i]
###print>>ou_file,""
##
##trin= [i[0] for i in sorted(enumerate(trie), key=lambda x:x[1])]
###print>>ou_file,trin
###print>>ou_file,""
##bwt=''
##for i in range(0,tlen):
##    if (trin[i]==2128 or trin[i]==2129):
##        print i,trin[i],in_text[trin[i]-1:trin[i]]
##    if(trin[i]!=0):
##        bwt+=in_text[trin[i]-1:trin[i]]
##    else:
##        bwt+=in_text[tlen-1:tlen]
##
##
##for i in range(0,tlen):
##    if (bwt[i]!=in_res[i]):
##        print i,bwt[i],in_res[i]
##if (bwt==in_res):
##    print "true"
###print>>ou_file,bwt

    
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
