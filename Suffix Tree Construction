'''
     Input: ATAAATG$
     Output: The edge labels of SuffixTree(Text). You may return these strings in any order.
             AAATG$
             G$
             T
             ATG$
             TG$
             A
             A
             AAATG$
             G$
             T
             G$
             $
     Logic:    
'''

import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_9_4_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

in_text=""
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(len(ldata)==0):
        break;
    else:
        in_text=ldata
 
#print in_text
#print ''

##Compare purpose
##in_file1 = open('w_9_4_data_set1_out.txt', 'r')
##in_res=[]
##for in_data in in_file1:
##    ldata = in_data.strip(' \t\n\r')
##    if(len(ldata)==0):
##        break;
##    else:
##        in_res.append(ldata)
##
##print len(in_res)
                
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

#print>>ou_file,trie 
trees=[]
def PrintTree(tr,oip):
    for i,ip in enumerate(tr):
        if(isinstance(tr[ip], list)):
            if (len(tr[ip])==1):
                trees.append(oip+ip+tr[ip][0])
            else :
                trees.append(ip)
                for j,jp in enumerate(tr[ip]):
                    trees.append(jp)
        elif (len(tr[ip])==0):
            trees.append(ip)
        elif (len(tr[ip])==1):
            PrintTree(tr[ip],oip+ip)
        else:
            trees.append(oip+ip)
            PrintTree(tr[ip],'')
            
PrintTree(trie,'')
for i,ip in enumerate(trees):
    print>>ou_file,ip

##Compare Purpose        
##print len(trees)
##print ''
##for i,ip in enumerate(trees):
##    if (ip in in_res):
##        #print ip
##        in_res.remove(ip)
##    else:
##        print " " , ip        
##    print len(in_res)
##
##print ''
##print len(in_res)    


tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"


#Tree code
'''
import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_9_4_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

in_text=""
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(len(ldata)==0):
        break;
    else:
        in_text=ldata
 
trees=[]
f=0
for i,ip in enumerate(in_text):
    #if (ip=='A'):
        ras = in_text[i:len(in_text)]
        #ras =ras.replace("A","A ");
        #print ras
        trees.append(ras)

trees=sorted(trees)
#print>>ou_file,' '
#for i,ip in enumerate(trees):
#    print>>ou_file,ip
#print trees

for i in range(0, len(trees)-1):
    for k,kp in enumerate(trees[i]):
        if(kp!=trees[i+1][k]):
            break
        elif (kp!=' '):
            for j in range(i+1, len(trees)):
                if (k-1>=0 and trees[j][k-1]!=' '):
                    break
                elif (kp==trees[j][k]):
                    s = list(trees[j])
                    s[k] = ' '
                    trees[j] =  "".join(s)
                else:
                    break
        elif(i+1==j):
            break

#print>>ou_file,' '
for i,ip in enumerate(trees):
    print>>ou_file,ip
                


tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"

'''
