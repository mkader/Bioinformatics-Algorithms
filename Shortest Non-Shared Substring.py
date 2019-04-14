'''
     Input: Strings Text1 and Text2.
             CCAAGCTGCTAGAGG
             CATGCTGGGCTGGCT
     Output: The shortest substring of Text1 that does not appear in Text2.
              AA
     
     Logic:
            CCAAGCTGCTAGAGG

            CC, CAA, AA, AG, GCTGC, CTGC, TGCTA, GCTA, CTA, TA, AG, GA, AG, GG[x]
            {'A': ['TGCTGGGCTGGCT'], 'C': ['ATGCTGGGCTGGCT', 'TGGGCTGGCT', 'TGGCT', 'T'], 'T': ['GCTGGGCTGGCT', 'GGGCTGGCT', 'GGCT', ''], 'G': ['CTGGGCTGGCT', 'GGCTGGCT', 'GCTGGCT', 'CTGGCT', 'GCT', 'CT']}
            {'A': 
              {'T': ['GCTGGGCTGGCT']}, 
             'C': 
              {'A': ['TGCTGGGCTGGCT'], 
               'T': 
                {'G': 
                  {'G': 
                    {'C': ['T'], 
                     'G': ['CTGGCT']}}}}, 
             'T': 
              {'G': 
                {'C': ['TGGGCTGGCT'], 
                 'G': 
                  {'C': ['T'], 
                   'G': ['CTGGCT']}}}, 
             'G': 
              {'C': 
                {'T': 
                  {'G': 
                    {'G': 
                      {'C': 
                        ['T'], 
                       'G': ['CTGGCT']}}}}, 
              'G': 
                {'C': 
                  {'T': 
                    {'G': ['GCT']}
                  }, 
                 'G': ['CTGGCT']}}}


            CATGCTGGGCTGGCT

            CAT, AT, TGCTA, GCTGC, CTGC, TGC, GG[x], GG[x],GCTGC, CTGC, TGC, GG[x],GCT[x],CT[x],T[x] 

            {'A': ['AGCTGCTAGAGG', 'GCTGCTAGAGG', 'GAGG', 'GG'], 'C': ['CAAGCTGCTAGAGG', 'AAGCTGCTAGAGG', 'TGCTAGAGG', 'TAGAGG'], 'T': ['GCTAGAGG', 'AGAGG'], 'G': ['CTGCTAGAGG', 'CTAGAGG', 'AGG', 'G', '']} 

            {'A': 
              {'A': ['GCTGCTAGAGG'], 
               'G': 
                {'A': ['GG'], 
                 'C': ['TGCTAGAGG'], 
                 'G': ['']}
               }, 
             'C': 
              {'A': ['AGCTGCTAGAGG'], 
               'C': ['AAGCTGCTAGAGG'], 
               'T': 
                {'A': ['GAGG'], 
                 'G': ['CTAGAGG']}
               }, 
             'T': 
              {'A': ['GAGG'], 
               'G': ['CTAGAGG']}, 
             'G': 
              {'A': ['GG'], 
               'C': 
                {'T': 
                  {'A': ['GAGG'], 
                   'G': ['CTAGAGG']}
                }, 
               'G': ['']}
             } 



            for example data set
            CCAAGCTGCTAGAGG
            CATGCTGGGCTGGCT
            tree for 'C' = > 
            'C':
                 {'A': ['TGCTGGGCTGGCT'],
                  'T':
                      {'G':
                          {'G':
                              {'C': ['T'],
                                'G': ['CTGGCT']}}}},  
 
'''

import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(1000000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_9_6_data_set2.txt', 'r')
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

in_text = in_texts[1]                 
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


    def PREFIXTRIEMATCHING(t,otr):
        found=False
        oip=''
        tpos=0
        tr=otr
        while(not found):
            #print "  ",tr,oip,len(tr),tpos
            #print " ",tpos, len(t)
            #print>>ou_file,len(t),len(tr),oip
            #print lastlen, len(oip)
            if(len(oip)+1>lastlen-1 or len(oip)+1>len(in_texts[0])/2):
                return ''
            #print lastlen, len(oip)
            if(len(t)==tpos):
                return ''
            if (isinstance(tr, list)):
                #print tr[0], len(tr[0]),t,len(t)
                if(len(tr[0])==0):
                    return oip+t[tpos]
            #print ''
            fbreak=False
            for i,ip in enumerate(tr):
                #print "  F  ", ip, ip[0],t[tpos]
                if(ip[0]==t[tpos]):
                    #t=t[1:]
                    tpos+=1
                    oip+=ip[0]
                    fbreak=True
                    if (isinstance(tr, dict)):
                        tr = tr[ip]
                        #return PREFIXTRIEMATCHING(t,tr[ip],oip+ip[0])
                        #break
                    else:
                        return oip+t[tpos]
                        #tr = [ip[1:]]
                        #print "    E1 ",tr,ip
                        #tr = ''.join(ip[1:])
                        #print "    E2 ",tr,ip
                        #print "   " ,[ip[1:]]
                        #return PREFIXTRIEMATCHING(t,[ip[1:]],oip+ip[0])
                        #break
                    break
            if(not fbreak):
                #oip+=t[tpos]
                return oip+t[tpos]  
        #return ''
    #print in_text
    print len(in_text)
    print ''
    in_text =in_texts[0]
    lshared=[]
    lastlen =len(in_text)
    for i in range(0,len(in_text)):
        t =in_text[i:]
        #print>>ou_file, i, t
        #print i, t
        #print i
        res = PREFIXTRIEMATCHING(t, trie)
        #print " ",res
        if(len(res)>0):# and res not in lshared):
            lastlen =len(res)
            lshared.append(res)
        #print ''
        #print in_text[i:]
    print''
    print len(lshared)
    #for j,jp in enumerate(lshared):
        #print jp
    #    print>>ou_file,jp
    print lshared[len(lshared)-1]
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
    #pass
##def PREFIXTRIEMATCHING(t, tr,p):
##    #global mlpos
##    #print>>ou_file, p,t#, tr
##    #print p,t#, tr
##    symbol = t[0]
##    v=tr
##    found=False
##    pos=0
##    matsys=""
##    while(not found):
##        found=True
##        #print>>ou_file, "  1p ",p, symbol, v
##        #print "  1p ",p, symbol, v
##        if(isinstance(v, list)):
##            for i,ip in enumerate(v):
##                #print len(ip),i
##                tmatsys = matsys
##                tpos = pos
##                #print "   1p ",ip, symbol, v, tmatsys
##                for k,kp in enumerate(list(ip)):
##                    #print "    2lp ", i,kp, symbol
##                    if(kp==symbol):
##                        tmatsys+=kp
##                    else:
##                        tmatsys+=t[tpos]
##                        break
##                    if(tpos+1>=len(t)):
##                        break
##                    else:
##                        tpos+=1
##                        symbol=t[tpos]
##                if(len(ip)>0):
##                    #print "   3lp ", tmatsys
##                    lshared.append(tmatsys)
##        else:
##            for i,ip in enumerate(v):
##                #print>>ou_file, "   2p ", i,ip
##                #print "   2p ", i,ip, symbol
##                if(ip==symbol):
##                    matsys+=ip
##                    #print>>ou_file, "   3p ", ip,symbol,pos,v[ip],len(v[ip]), len(t)
##                    #print "   3p ", ip,symbol,pos,v[ip],len(v[ip]), len(t)
##                    if (len(t)==pos+1 and len(v[ip])>0):
##                        found=True
##                        break
##                    if(len(v[ip])>0):
##                        pos+=1
##                        symbol=t[pos]
##                    v= v[ip]
##                    #print "     4p ", v
##                    found=False
##                    break
##            if(found):
##                if (t!=matsys):
##                    matsys+=t[pos]
##                    lshared.append(matsys)
##                    #print matsys, found,p, pos, t, len(t)
##in_text =in_texts[0]        
##p=0
##mlpos=[]
##lshared=[]
##while len(in_text)>0:
##    PREFIXTRIEMATCHING(in_text, trie, p)
##    in_text =in_text[1:len(in_text)]
##    p+=1
##
##
###for j,jp in enumerate(mlpos):
##    #print jp
##    #print>>ou_file,jp,
##
##lp=lshared[0]
##lv=len(lp)
##for j,jp in enumerate(lshared):
##    if(len(jp)<9):
##        print>>ou_file, jp
###    if(len(jp)<lv):
####        lv=len(jp)
####        lp=jp    
###print>>ou_file, lp

tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
