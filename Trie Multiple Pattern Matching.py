'''
TrieMathing to solve the Multiple Pattern Matching
     Input: A string Text and a collection of strings Patterns.
             AATCGGGTTCAATCGGGGT
             ATCG
             GGGT
     Output: All starting positions in Text where a string from Patterns appears as a substring.
             1 11
             4 15
     Logic:
            1 11 20 29 
            4 15 22  
'''
import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_9_2_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 0
in_text=""
in_patterns =[]
mpos ={}
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(len(ldata)==0):
        break;
    if(line==0):
        in_text=ldata
    else:
        in_patterns.append(ldata)
        mpos[ldata]=[]
    line+=1
    #print mpos

#print in_text
#print in_patterns
#print mpos

trie ={}
for i,ip in enumerate(in_patterns):
    fci =ip[0]
    ipa = ip[1:]
    if (fci in trie):
        trie[fci]+=[ipa]
    else:
        trie[fci]=[ipa]

print trie
print''

def ExtendTrie(epatterns):
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
        if(len(etrie[jp])>0):
            etrie[jp]=ExtendTrie(etrie[jp])
    return etrie

for i,ip in enumerate(trie):
    trie[ip]=ExtendTrie(trie[ip])

#print trie
#print ''


def PREFIXTRIEMATCHING(t, tr,p):
    print p,t#, tr
    symbol = t[0]
    v=tr
    found=False
    pos=0
    matsys=""
    while(not found):
        found=True
        #print "  1 ",symbol, v
        for i,ip in enumerate(v):
            #print "   2 ", i,ip
            if(ip==symbol):
                matsys+=ip
                #print "   3 ", ip,symbol,pos,v[ip],len(v[ip]), len(t)
                if (len(t)==pos+1 and len(v[ip])>0):
                    found=True
                    break
                if(len(v[ip])>0):
                    pos+=1
                    symbol=t[pos]
                v= v[ip]
                found=False
                break
        if(not found and len(v)==0):
            mpos[matsys] += [p]
            mlpos.append(p)
            #print " Pos ",p, t[0], matsys    
        
p=0
mlpos=[]
while len(in_text)>0:
    PREFIXTRIEMATCHING(in_text, trie, p)
    in_text =in_text[1:len(in_text)]
    p+=1


for j,jp in enumerate(mlpos):
    #print jp
    print>>ou_file,jp,

###print mpos.values()
##for i,ip in enumerate(in_patterns):
##    #print ip
##    for j,jp in enumerate(mpos[ip]):
##        #print jp
##        print>>ou_file,jp,
##    print>>ou_file, ''
        
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
