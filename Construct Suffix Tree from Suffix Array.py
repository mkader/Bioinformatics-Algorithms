'''
Construct a suffix tree from the suffix array and LCP array of a string.
     Input: A string Text, SuffixArray(Text), and LCP(Text).
            GTAGT$
            5, 2, 3, 0, 4, 1
            0, 0, 0, 2, 0, 1

     Output: return the list of all strings forming edge labels of the suffix tree.
           $
           T
           AGT$
           $
           AGT$
           GT
           $
           AGT$
           
     Logic:
        shesellssea$
        11, 10, 9, 4, 2, 1, 5, 6, 8, 3, 0, 7
        0, 0, 0, 1, 1, 0, 0, 1, 0, 2, 1, 1

        shesellssea$
        012345678901
        ['shesellssea$', 'hesellssea$', 'esellssea$', 'sellssea$', 'ellssea$', 'llssea$', 'lssea$', 'ssea$', 'sea$', 'ea$', 'a$', '$']
        $', 'a$', 'ea$', 'ellssea$', 'esellssea$', 
        'hesellssea$', 'llssea$', 'lssea$', 'sea$', 'sellssea$', 
        'shesellssea$', 'ssea$']

        $
        a$
        ea$
         llssea$
         sellssea$
        hesellssea$
        llssea$
         ssea$
        se
          a$
          llssea$
         hesellssea$
         sea$
'''

import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_9_8_data_set04.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

in_text=""
in_order=[]
in_edge=[]
line=0
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(len(ldata)==0):
        break;
    elif(line==0):
        in_text =ldata
    elif(line==1):
        in_order=map(int,ldata.split(", "))
        #print in_order 
    elif(line==2):
        in_edge=map(int,ldata.split(", "))
        #print in_edge 
    line+=1

#print in_text
#print in_order
#print in_edge    
#print ''
#NOT DONE, RE DO CODE
def CreateTree(itxt):
    in_text = itxt                 
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
    #print trie
    print>>ou_file, trie
    #print ''
CreateTree(in_text)

def GetOrder(itxt):
    pos=1
    tlen =len(itxt)
##    found=True
##    while(found):
##        found=False
##        for i in range(0,tlen/2):
##            ipa = itxt[i:pos+i]
##            if(ipa in itxt[pos+i:]):
##                #print "  ", trie
##                pos+=1
##                found=True
##    #print pos
    trie=[]            
    for i in range(0,tlen):
        #trie.append(itxt[i:pos+i])
        trie.append(itxt[i:])
    #print "done"
    print ''
    print trie
    print sorted(trie)
    print [i[0] for i in sorted(enumerate(trie), key=lambda x:x[1])]
    print ''
    #print>>ou_file, [i[0] for i in sorted(enumerate(trie), key=lambda x:x[1])]
    

#GetOrder(in_text)

iord=0
tlen = len(in_text)
trees=[]
while(iord<len(in_order)):
    #print "s ", iord
    pos = in_order[iord]
    edg = in_edge[iord]
    print iord, edg,pos, in_text[in_order[iord]:] 
    if (edg==0):
        zedg=[]
        tiord=iord
        for e in range(iord+1,len(in_edge)):
            nedg=in_edge[e]
            tiord=e
            if (edg==nedg):
                break
            else:
                zedg.append(nedg)
                #print " ",nedg
        #print " AR", zedg, len(zedg),tiord,iord,len(in_order)
        if(len(zedg)==0):
            #print "  SV0",in_text[pos:tlen]
            trees.append(in_text[pos:tlen])
            if (tiord==iord):
                tiord+=1
        else:
            print " AR", zedg, len(zedg)#,tiord,iord,len(in_order)
            medg = min(zedg)
            zedg.append(0)
            k = zedg[0]
            if(k>0):
                stxt = in_text[pos:]
                if(medg!=k):
                    mtxt =stxt[:k]
                    print "  SV10",stxt, mtxt[:medg],mtxt[medg:] ,stxt[k:], medg, k
                    trees.append(mtxt[:medg])
                    trees.append(mtxt[medg:])
                else:    
                    print "  SV11",stxt, stxt[:k], stxt[k:], medg, k
                    trees.append(stxt[:k])
                trees.append(stxt[k:])
            for j in range(0,len(zedg)-1):
                k=zedg[j]
                jc = zedg[j]
                jn = zedg[j+1]
                spos=in_order[iord+j+1]
                print "   MV",j, jc, jn, iord+j+1,spos, k," - " ,
                print in_text[spos:],in_text[spos+k:], 
                if(jn>jc):
                    stxt = in_text[in_order[iord+j+1]+k:]
                    print stxt[:jn-jc], stxt[jn-k:],">"
                    trees.append(stxt[:jn-jc])
                    trees.append(stxt[jn-k:])
                elif(jn==jc):
                    print in_text[spos+k:], "="
                    #print>>ou_file, spos, jc, jn, in_text[spos+k:], "="
                    trees.append(in_text[spos+k:])
                elif(jn<jc):
                    stxt = in_text[spos:]
                    print stxt[jc:], "<"
                    trees.append(stxt[jc:])
        iord=tiord
        #print " e", iord
    else:
        iord+=1

for i,ip in enumerate(trees):
    print>>ou_file, ip


def PrintTree(trees):
    for i,ip in enumerate(in_order):
         print>>ou_file, in_text[ip:]
        
#PrintTree(trees)
##Compare Purpose        
def CompareResult(trees):
    in_file1 = open('w_9_8_data_set04_res.txt', 'r')
    in_res=[]
    for in_data in in_file1:
        ldata = in_data.strip(' \t\n\r')
        if(len(ldata)==0):
            break;
        else:
            in_res.append(ldata)
    print len(in_res)

    print len(trees)
    print ''
    for i,ip in enumerate(trees):
        if (ip in in_res):
            #print ip
            in_res.remove(ip)
        else:
            print " " , ip        
        print len(in_res)
    print ''
    #print len(in_res)   

#CompareResult(trees)
    
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"



#withour Tree - improved solution
'''
import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_9_8_data_set04.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

in_text=""
in_order=[]
in_edge=[]
line=0
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(len(ldata)==0):
        break;
    elif(line==0):
        in_text =ldata
    elif(line==1):
        in_order=map(int,ldata.split(", "))
        #print in_order 
    elif(line==2):
        in_edge=map(int,ldata.split(", "))
        #print in_edge 
    line+=1

#print in_text
#print in_order
#print in_edge    
#print ''
#NOT DONE, RE DO CODE
def CreateTree(itxt):
    in_text = itxt                 
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
    #print trie
    print>>ou_file, trie
    #print ''
CreateTree(in_text)

def GetOrder(itxt):
    pos=1
    tlen =len(itxt)
##    found=True
##    while(found):
##        found=False
##        for i in range(0,tlen/2):
##            ipa = itxt[i:pos+i]
##            if(ipa in itxt[pos+i:]):
##                #print "  ", trie
##                pos+=1
##                found=True
##    #print pos
    trie=[]            
    for i in range(0,tlen):
        #trie.append(itxt[i:pos+i])
        trie.append(itxt[i:])
    #print "done"
    print ''
    print trie
    print sorted(trie)
    print [i[0] for i in sorted(enumerate(trie), key=lambda x:x[1])]
    print ''
    #print>>ou_file, [i[0] for i in sorted(enumerate(trie), key=lambda x:x[1])]
    

#GetOrder(in_text)

iord=0
tlen = len(in_text)
trees=[]
while(iord<len(in_order)):
    #print "s ", iord
    pos = in_order[iord]
    edg = in_edge[iord]
    print iord, edg,pos, in_text[in_order[iord]:] 
    if (edg==0):
        zedg=[]
        tiord=iord
        for e in range(iord+1,len(in_edge)):
            nedg=in_edge[e]
            tiord=e
            if (edg==nedg):
                break
            else:
                zedg.append(nedg)
                #print " ",nedg
        #print " AR", zedg, len(zedg),tiord,iord,len(in_order)
        if(len(zedg)==0):
            #print "  SV0",in_text[pos:tlen]
            trees.append(in_text[pos:tlen])
            if (tiord==iord):
                tiord+=1
        else:
            print " AR", zedg, len(zedg)#,tiord,iord,len(in_order)
            medg = min(zedg)
            zedg.append(0)
            k = zedg[0]
            if(k>0):
                stxt = in_text[pos:]
                if(medg!=k):
                    mtxt =stxt[:k]
                    print "  SV10",stxt, mtxt[:medg],mtxt[medg:] ,stxt[k:], medg, k
                    trees.append(mtxt[:medg])
                    trees.append(mtxt[medg:])
                else:    
                    print "  SV11",stxt, stxt[:k], stxt[k:], medg, k
                    trees.append(stxt[:k])
                trees.append(stxt[k:])
            for j in range(0,len(zedg)-1):
                k=zedg[j]
                jc = zedg[j]
                jn = zedg[j+1]
                spos=in_order[iord+j+1]
                print "   MV",j, jc, jn, iord+j+1,spos, k," - " ,
                print in_text[spos:],in_text[spos+k:], 
                if(jn>jc):
                    stxt = in_text[in_order[iord+j+1]+k:]
                    print stxt[:jn-jc], stxt[jn-k:],">"
                    trees.append(stxt[:jn-jc])
                    trees.append(stxt[jn-k:])
                elif(jn==jc):
                    print in_text[spos+k:], "="
                    #print>>ou_file, spos, jc, jn, in_text[spos+k:], "="
                    trees.append(in_text[spos+k:])
                elif(jn<jc):
                    stxt = in_text[spos:]
                    print stxt[jc:], "<"
                    trees.append(stxt[jc:])
        iord=tiord
        #print " e", iord
    else:
        iord+=1

for i,ip in enumerate(trees):
    print>>ou_file, ip


def PrintTree(trees):
    for i,ip in enumerate(in_order):
         print>>ou_file, in_text[ip:]
        
#PrintTree(trees)
##Compare Purpose        
def CompareResult(trees):
    in_file1 = open('w_9_8_data_set04_res.txt', 'r')
    in_res=[]
    for in_data in in_file1:
        ldata = in_data.strip(' \t\n\r')
        if(len(ldata)==0):
            break;
        else:
            in_res.append(ldata)
    print len(in_res)

    print len(trees)
    print ''
    for i,ip in enumerate(trees):
        if (ip in in_res):
            #print ip
            in_res.remove(ip)
        else:
            print " " , ip        
        print len(in_res)
    print ''
    #print len(in_res)   

#CompareResult(trees)
    
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"

'''
