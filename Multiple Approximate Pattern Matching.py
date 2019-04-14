'''
Multiple Approximate Pattern Matching
     Input: A string Text, followed by a collection of strings Patterns, and an integer d.
            ACATGCTACTTT
            ATT GCC GCTA TATT
            1
     Output: All positions where one of the strings in Patterns appears as a substring of Text with  at most d mismatches.
            2 4 4 6 7 8 9
     Logic:
        0  1 ACATGCTACTTT$
        1  1 CATGCTACTTT$A
        2  2 ATGCTACTTT$AC
        3  1 TGCTACTTT$ACA
        4  1 GCTACTTT$ACAT
        5  2 CTACTTT$ACATG
        6  2 TACTTT$ACATGC
        7  3 ACTTT$ACATGCT
        8  3 CTTT$ACATGCTA
        9  3 TTT$ACATGCTAC
        10 4 TT$ACATGCTACT
        11 5 T$ACATGCTACTT
        12 1 $ACATGCTACTTT

        12 1 $ACATGCTACTTT 1 1 4T1T$
        0  1 ACATGCTACTTT$ 1 1 1T1$A
        7  2 ACTTT$ACATGCT 2 1 2C2TA
        2  3 ATGCTACTTT$AC 1 1 1A1CA 
        1  1 CATGCTACTTT$A 1 1 1$1AC
        5  2 CTACTTT$ACATG 1 1 3T1GC
        8  3 CTTT$ACATGCTA 2 1 2T2AC
        4  1 GCTACTTT$ACAT 3 1 3A3TG x
        11 1 T$ACATGCTACTT 4 0 5T4TT x
        6  2 TACTTT$ACATGC 2 0 1G2CT
        3  3 TGCTACTTT$ACA 3 0 1C3AT
        10 4 TT$ACATGCTACT 5 0 3C5TT x
        9  5 TTT$ACATGCTAC 3 0 2A3CT x

                             t     t        a
        7  2 ACTTT$ACATGCT 2 1->0->1->0[0]->0->1[1]
        2  3 ATGCTACTTT$AC 1 1->1->1->1[2]->0->1[3] 
        8  3 CTTT$ACATGCTA 2 1->1->1->1[2]->1->0[2]
        9  5 TTT$ACATGCTAC 3 0->1->0->1[2]->1->1[3]

        12 1 $ACATGCTACTTT 1 1
        0  1 ACATGCTACTTT$ 1 1
        7  2 ACTTT$ACATGCT 2 1
        2  3 ATGCTACTTT$AC 1 1 
        1  1 CATGCTACTTT$A 1 1
        5  2 CTACTTT$ACATG 1 1
        8  3 CTTT$ACATGCTA 2 1
        4  1 GCTACTTT$ACAT 3 1
        11 1 T$ACATGCTACTT 4 0
        6  2 TACTTT$ACATGC 2 0
        3  3 TGCTACTTT$ACA 3 0
        10 4 TT$ACATGCTACT 5 0
        9  5 TTT$ACATGCTAC 3 0

        12 1 $ACATGCTACTTT 1 0 1
        0  1 ACATGCTACTTT$ 1 1 2 
        7  2 ACTTT$ACATGCT 2 0 1
        2  3 ATGCTACTTT$AC 1 1 2  
        1  1 CATGCTACTTT$A 1 1 2
        5  2 CTACTTT$ACATG 1 1 2
        8  3 CTTT$ACATGCTA 2 1 2
        4  1 GCTACTTT$ACAT 3 0 1
        11 1 T$ACATGCTACTT 4 0 0
        6  2 TACTTT$ACATGC 2 1 1
        3  3 TGCTACTTT$ACA 3 1 1
        10 4 TT$ACATGCTACT 5 0 0
        9  5 TTT$ACATGCTAC 3 1 1

        12 1 $ACATGCTACTTT 1 0 1
        0  1 ACATGCTACTTT$ 1 1 1
        7  2 ACTTT$ACATGCT 2 1 1
        2  3 ATGCTACTTT$AC 1 2 2 
        1  1 CATGCTACTTT$A 1 2 3
        5  2 CTACTTT$ACATG 1 1 2
        8  3 CTTT$ACATGCTA 2 1 2
        4  1 GCTACTTT$ACAT 3 1 2
        11 1 T$ACATGCTACTT 4 0 1
        6  2 TACTTT$ACATGC 2 2 3
        3  3 TGCTACTTT$ACA 3 2 3
        10 4 TT$ACATGCTACT 5 1 2
        9  5 TTT$ACATGCTAC 3 2 3

        2 7 8 9
        12,11,6,10
        -------------------
        panamabananas

         0 panamabananas$
         1 anamabananas$p
         2 namabananas$pa
         3 amabananas$pan
         4 mabananas$pana
         5 abananas$panam
         6 bananas$panama
         7 ananas$panamab
         8 nanas$panamaba
         9 anas$panamaban
        10 nas$panamabana
        11 as$panamabanan
        12 s$panamabanana
        13 $panamabananas  

        smnpbnnaaaaa$a

         0 0  $panamabananas  1   13  13
         1 1  abananas$panam  1    5   8     
         2 2  amabananas$pan  1    3   9
         3 3  anamabananas$p  1    1  12
         4 4  ananas$panamab  1    7   7
         5 5  anas$panamaban  2    9  10
         6 6  as$panamabanan  3   11  11 
         7 1  bananas$panama  1    6   1
         8 1  mabananas$pana  2    4   2
         9 1  namabananas$pa  3    2   3
        10 2  nanas$panamaba  4    8   4
        11 3  nas$panamabana  5   10   5
        12 1  panamabananas$  1    0  13
        13 1  s$panamabanana  6   12   6
        f  sp sv	   ev rsp oo  ltf
                    rp	

        a				
         0 1  $panamabananas  1   13  13 1 
         1 1  abananas$panam  1    5   8 0     
         2 2  amabananas$pan  1    3   9 0
         3 3  anamabananas$p  1    1  12 0
         4 4  ananas$panamab  1    7   7 0
         5 5  anas$panamaban  2    9  10 0
         6 6  as$panamabanan  3   11  11 0 
         7 1  bananas$panama  1    6   1 1
         8 1  mabananas$pana  2    4   2 1
         9 1  namabananas$pa  3    2   3 1
        10 2  nanas$panamaba  4    8   4 1
        11 3  nas$panamabana  5   10   5 1
        12 1  panamabananas$  1    0  13 1
        13 1  s$panamabanana  6   12   6 1
        f  sp sv	   ev rsp oo  ltf
                    rp

        n				
         0 0  $panamabananas  1   13  13 1 2
         1 1  abananas$panam  1    5   8 1 2     
         2 2  amabananas$pan  1    3   9 1 2
         3 3  anamabananas$p  1    1  12 1 2
         4 4  ananas$panamab  1    7   7 1 2
         5 5  anas$panamaban  2    9  10 1 2
         6 6  as$panamabanan  3   11  11 1 2 
         7 1  bananas$panama  1    6   1 1 1
         8 1  mabananas$pana  2    4   2 1 1
         9 1  namabananas$pa  3    2   3 0 0
        10 2  nanas$panamaba  4    8   4 0 0
        11 3  nas$panamabana  5   10   5 0 0
        12 1  panamabananas$  1    0  13 1 2
        13 1  s$panamabanana  6   12   6 1 1
        f  sp sv	   ev rsp oo  ltf
                    rp

        d				
         2 2  amabananas$pan  1    3   9 1 
         5 5  anas$panamaban  2    9  10 1
         6 6  as$panamabanan  3   11  11 1 
        f  sp sv	   ev rsp oo  ltf
                    rp	
        panamabananas	
        0123456789012

        {'p1': '$1', 's1': 'a6', 'n1': 'a3', 'a1': 'm1', 'a3': 'p1', 'a2': 'n1', 'a5': 'n2', 'a4': 'b1', 'b1': 'a1', 'a6': 'n3', 'm1': 'a2', 'n2': 'a4', 'n3': 'a5', '$1': 's1'}
        {'p1': '$1', 's1': 'a6', 'n1': 'a3', 'a1': 'm1', 'a3': 'p1', 'a2': 'n1', 'a5': 'n2', 'a4': 'b1', 'b1': 'a1', 'a6': 'n3', 'm1': 'a2', 'n2': 'a4', 'n3': 'a5', '$1': 's1'}           
'''

import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_10_7_data_set9.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

in_text=""
line=0
in_mismatch=0
patterns=[]
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(len(ldata)==0):
        break;
    elif(line==0):
        in_text =ldata
    elif(line==1):
        patterns=ldata.split(' ')
    else:
        in_mismatch= int(ldata)
    line+=1

#print in_text

def TotalMismatch(fv,ifv):
    #print fv, ifv
    mm=0
    for i,f in enumerate(fv):
        if (f!=ifv[i]):
            mm+=1
        if (mm>in_mismatch):
            return mm
    return mm

def PrintBWTEnd(bwtae):
    #print bwtae.keys()
    for i, lev in enumerate(sorted(bwtae.keys())):
        #print lev,
        print lev+":"+ str(bwtae[lev])+", ",
    print ""
        
def MethodBWT():
    itext=in_text+'$'

    tlen =len(itext)
    pos=10
    found=True
    while(found):
        found=False
        for i in range(0,tlen/2):
            ipa = itext[i:pos+i]
            if(ipa in itext[pos+i:]):
                #print "  ", trie
                pos+=1
                found=True
    print pos
    trie=[]            
    for i in range(0,tlen):
        #print itext[i:pos+i]+itext[i-1]
        trie.append(itext[i:pos+i]+itext[i-1])
        #trie.append(itext[i:]+itext[:i])

##    for i,rt in enumerate(sorted(trie)):
##        print rt
        
    rdict={}
    trieo={}
    #bwtae={}
    for i,rt in enumerate(sorted(trie)):
        if (rt[0] not in rdict.keys()):
            rdict[rt[0]]=1
        else:
            rdict[rt[0]]=rdict[rt[0]]+1
        #print i, rt, trie.index(rt)   
        trieo[rt[0]+str(rdict[rt[0]])]= trie.index(rt) 

    #print trieo
    #PrintBWTEnd(trieo)
    rdict={}
    idict={}
    bwta={}
    bwtae={}
    for i,srt in enumerate(sorted(trie)):
        rt=srt[0]
        if (rt not in rdict.keys()):
            rdict[rt]=1
        else:
            rdict[rt]=rdict[rt]+1
        it =srt[-1]    
        if (it not in idict.keys()):
            idict[it]=1
        else:
            idict[it]=idict[it]+1
        bwta[rt+str(rdict[rt])]=it+str(idict[it])
        #bwtae[it+str(idict[it])]=0
    #PrintBWTEnd(bwta)

    plen =0
    for i, p in enumerate(patterns):
        if (len(p)>plen):
            plen=len(p)
    #print plen
    #print bwta
            
##    mkvalue=[]
##    #dpos={}
##    for i, lev in enumerate(bwta.keys()):
##        pos = 0
##        #nval = lev
##        mval = ''
##        dpos=[]
##        while(pos<plen):
##            mval=lev[0]+mval
##            dpos.append(trieo[bwta[lev]])
##            #print " ", pos, lev, bwta[lev], bwta[bwta[lev]], trieo[bwta[lev]]
##            lev = bwta[lev]
##            pos+=1
##            #print bwta[lev][0]+lev[0],bwta[lev], lev[0],bwta[lev][0]
##        #print i,mval, dpos#, mval[::-1]
##        #mkvalue[mval]=dpos[i]
##        #mval = mval[::-1]
##        for j, p in enumerate(patterns):
##            lp = len(p)
##            bwt =mval[len(mval)-lp:]
##            tm = TotalMismatch(bwt,p)
##            if(tm<=in_mismatch):
##                mkvalue.append(dpos[lp-2])
##                #print p, mval, bwt, tm, dpos, dpos[::-1], lp, dpos[lp-2]
##    #print sorted(mkvalue)

##    mkvalue=[]
##    for i, p in enumerate(patterns):
##        #print i, p
##        p=p[::-1]
##        for j, lev in enumerate(bwta.keys()):
##            tm=0
##            #print " ", j, p,lev,len(p)
##            #if(lev[0]
##            pos = 0
##            olev=''
##            while(pos<len(p)):
##                if(p[pos]!=lev[0]):
##                    tm+=1
##                #print "  " ,pos, tm ,olev, lev, lev[0], bwta[lev], trieo[bwta[lev]]
##                if(tm>in_mismatch or len(p)-1==pos):
##                    break
##                olev=lev
##                lev = bwta[lev]
##                pos+=1
##            if(tm<=in_mismatch):
##                mkvalue.append(trieo[bwta[olev]])
##                #print "     " ,tm,  olev, bwta[olev], trieo[bwta[olev]]

    mkvalue=[]
    #dbwta={}
    for i, ilev in enumerate(bwta.keys()):
        pos = 0
        #dbwta[i]=[]
        #dbwta={}
        lev=ilev
        #print i
        bpatterns = [True] * len(patterns)
        bwtpos=[-1]*len(patterns)
        dbwta=[0]*len(patterns)
        #print bpatterns, bwtpos
        #olev =''
        while(pos<plen):
            for j in range(0,len(patterns)):
                rpatterns = patterns[j][::-1]
                if (bpatterns[j]):
                    #if (j not in dbwta.keys()):
                    #    dbwta[j]=0
                    if (pos<len(patterns[j])):
                        bwtpos[j] = trieo[lev]
                        if (rpatterns[pos]!=lev[0]):
                        #    dbwta[j]+=0
                        #else:
                            dbwta[j]+=1
                        #bwtpos[j]=trieo[bwta[lev]]    
                    if(dbwta[j]>in_mismatch):
                        bpatterns[j]=False
                        #bwtpos[pos]=-1
                    #else:
                    #    if(len(olev)>0):
                    #        print " P" ,pos
                            #bwtpos[j]=trieo[bwta[olev]]
                    #print " ", pos, lev, olev, j, lev[0],bwta[lev],  trieo[lev], dbwta, bpatterns, bwtpos
            #olev=lev
            lev = bwta[lev]
            pos+=1
        for j in range(0,len(patterns)):
            if (bpatterns[j]):
                #print "  ", bpatterns, bwtpos[j]
                mkvalue.append(bwtpos[j])
        
    for i,p in enumerate(sorted(mkvalue)):
        print>>ou_file,p,
#1 - 0:01:50.54
#not fast
#MethodBWT()



def FindMatch(spa):
    apos=[]
    for i,spv in enumerate(spa.keys()):
        k=pos = 0
        fv=bv=''
        if(spa[spv][0]!=''):
            #fv =FrontPattern(spa, 0,i)
            fv = spa[spv][0]
        #if(i!=len(spa)-1):
        if(spa[spv][1]!=''):    
            #bv =FrontPattern(spa, i+1,len(spa))
            bv= spa[spv][1]
        #print>>ou_file, " S",i,spv,"-", fv,"-", bv
        while(k<len(in_text) and pos>=0):
            pos = in_text.find(spv,k,len(in_text))
            #print>>ou_file, "   P",pos
            if (pos!=-1):
                bpos=-1
                fmm=bmm=0
                if (len(fv)>0):
                    ifv = in_text[pos-len(fv):pos]
                    if (len(ifv)==len(fv)):
                        fmm = TotalMismatch(fv,ifv)
                        bpos =pos-len(ifv)
                        #print>>ou_file, "   F",k, bpos, ifv, fmm
                if (len(bv)>0 and fmm<=in_mismatch):
                    ifv = in_text[pos+len(spv):pos+len(spv)+len(bv)]
                    if (len(ifv)==len(bv)):
                        bmm = TotalMismatch(bv,ifv)
                        if (bpos==-1):
                            bpos =pos
                        #print>>ou_file, "   B",k, bpos, ifv, bmm
                if(bmm+fmm<=in_mismatch):
                    if (bpos!=-1 and bpos not in apos):
                        apos.append(bpos)
                        #print " Pos", pos
            k = pos+1
    return apos

def MethodSeed():
    mpos=[]
    for i,ip in enumerate(patterns):
        #if (ip[:4]=="GAGC"):
        #    print>>ou_file, ip
        sp = int(round(len(ip)/(in_mismatch+1.0)))
        #print i,ip,in_mismatch, sp, len(ip)
        k=0
        j=0
        spal=[]
        while(k<in_mismatch+1):
            if (k==in_mismatch):
                spv = ip[j:]
                spal.append(spv)
                #print k, ip[j:], in_mismatch+1
            else:
                spv = ip[j:j+sp]
                spal.append(spv)
                #spa.append(ip[j:j+sp])
            #spa[spv]=[ip[:j],ip[j+sp:]]
                #print k, ip[j:j+sp], in_mismatch+1
            k+=1
            j+=sp
        spa={}
        #spa[spal[0]]=['',spal[1]+spal[2]]
        #spa[spal[1]]=[spal[0],spal[2]]
        #spa[spal[2]]=[spal[0]+spal[1],'']
        for i,s in enumerate(spal):
            #for i in rangeenumerate(spal):
            #if (i==0):
            spa[s]=[''.join(spal[:i]),''.join(spal[i+1:])]
            #print i, s, ''.join(spal[:i]),''.join(spal[i+1:])
        #print spal
        #print spa
        mpos+=FindMatch(spa)
##        #print spa
        #mpos =FindMatch(spa)
##        #print>>ou_file, ip, sorted(mpos)    

    #print>>ou_file,""    
    #print>>ou_file, sorted(mpos)
    #print>>ou_file,len(in_text),len(patterns[0])
    #print>>ou_file,patterns[0]
    #print>>ou_file,""
    for i,p in enumerate(sorted(mpos)):
        print>>ou_file,p,

#1- 0:00:00.752000
#2 - 0:00:20.798000
#3 - 0:07:48.321000
MethodSeed()

#print [m.start() for m in re.finditer('test', 'testatest test test')]

def CheckOutput():
    mpos=[]
    for j,p in enumerate(patterns):
        cmpos=[]
        lp = len(p)
        for i in range(0,len(in_text)):
            spt =in_text[i:i+lp]
            if (len(spt)==lp):
                mm = TotalMismatch(p,spt)
                if (mm<=in_mismatch):
                    cmpos.append(i);
                    ##print>>ou_file," ",i,spt, mm
        mpos+=cmpos
        cmpos=sorted(cmpos)
        if (len(cmpos)>0 and cmpos[0]==0):
            print i, p
            break
    for i,p in enumerate(sorted(mpos)):
        print>>ou_file,p,
#2 - 0:58:57.788000        
#CheckOutput()


        
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
