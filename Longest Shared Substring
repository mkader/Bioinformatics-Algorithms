'''
Although the suffix tree decreases memory requirements from O(|Text|2) to O(|Text|), on average it still requires about 20 
times as much memory as Text. In the case of a 3 GB human genome, 60 GB of RAM is a huge improvement over the 1 TB that we 
needed to work with Trie(Patterns), but it still presents a memory challenge for most machines. This reveals a dark secret 
of big-O notation, which is that it ignores constant factors. For huge datasets such as the human genome, we will need to 
pay attention to this constant.

Yet before seeing how we can further reduce the memory needed for pattern matching, you may be interested in two additional 
problems showing how suffix trees can be applied to other pattern matching challenges. The first such problem is the Longest 
Shared Substring Problem.

     Input: Strings Text1 and Text2.
               TCGGTAGATTGCGCCCACTC
               AGGGGCTCGCAGTGTAAGAA

     Output: The longest substring that occurs in both  Text1 and Text2.
               AGA
'''

import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_9_5_data_set3.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

in_texts=[]
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(len(ldata)==0):
        break;
    else:
        in_texts.append(ldata)
 
#print in_text
#print ''

in_text = in_texts[0]                 
trie ={}
for i,ip in enumerate(in_text):
    fci =ip
    ipa = in_text[i+1:]
    if (fci in trie):
        trie[fci]+=[ipa]
    else:
        trie[fci]=[ipa]
    #print fci, ipa

#print>>ou_file,trie        
#print trie
#print ''

try:
    def ExtendTrie(epatterns,n):
        etrie ={}
        for i,ip in enumerate(epatterns):
            if (len(ip)>0):
                fci =ip[0]
                ipa = ip[1:]
                if (fci in etrie):
                    etrie[fci]+=[ipa]
                else:
                    etrie[fci]=[ipa]
        for j,jp in enumerate(etrie):
            if(len(etrie[jp])>1):
                etrie[jp]=ExtendTrie(etrie[jp],n+1)
        return etrie


    for i,ip in enumerate(trie):
        #print i,ip
        trie[ip]=ExtendTrie(trie[ip],0)
except:
    print "Unexpected error:", sys.exc_info()[0]
    pass

#print trie

def PREFIXTRIEMATCHING(t, tr,p):
    #global mlpos
    #print>>ou_file, p,t#, tr
    #print p,t#, tr
    symbol = t[0]
    v=tr
    found=False
    pos=0
    matsys=""
    while(not found):
        found=True
        #print>>ou_file, "  1p ",p, symbol, v
        #print "  1p ",p, symbol, v
        if(isinstance(v, list)):
            for i,ip in enumerate(v):
                tmatsys = matsys
                tpos = pos
                #print "   1p ",ip, symbol, v, tmatsys
                for k,kp in enumerate(list(ip)):
                    #print "    2lp ", i,kp, symbol
                    if(kp==symbol):
                        tmatsys+=kp
                    else:
                        break
                    if(tpos+1>=len(t)):
                        break
                    else:
                        tpos+=1
                        symbol=t[tpos]
            #print "   3lp ", tmatsys
            lshared.append(tmatsys)
        else:
            for i,ip in enumerate(list(v)):
                #print>>ou_file, "   2p ", i,ip
                #print "   2p ", i,ip, symbol
                if(ip==symbol):
                    matsys+=ip
                    #print>>ou_file, "   3p ", ip,symbol,pos,v[ip],len(v[ip]), len(t)
                    #print "   3p ", ip,symbol,pos,v[ip],len(v[ip]), len(t)
                    if (len(t)==pos+1 and len(v[ip])>0):
                        found=True
                        break
                    if(len(v[ip])>0):
                        pos+=1
                        symbol=t[pos]
                    v= v[ip]
                    #print "     4p ", v
                    found=False
                    break
        
            if(not found and len(v)==0):
                #print p, matsys
                #mpos[matsys] += [p]
                mlpos.append(p)
                #print " Pos ",p, t[0], matsys    
    #print p, matsys
    lshared.append(matsys)
in_text =in_texts[1]        
p=0
mlpos=[]
lshared=[]
while len(in_text)>0:
    PREFIXTRIEMATCHING(in_text, trie, p)
    in_text =in_text[1:len(in_text)]
    p+=1


#for j,jp in enumerate(mlpos):
    #print jp
    #print>>ou_file,jp,

lp=''
lv=0
for j,jp in enumerate(lshared):
    #print jp
    if(len(jp)>lv):
        lv=len(jp)
        lp=jp    
print>>ou_file, lp

tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
