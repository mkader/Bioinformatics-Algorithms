'''
     Input: Two amino acid strings v and w (each of length at most 100).
             PRTEINS
             PRTWPSEIN
     Output: The maximum alignment score between v and w, followed by an alignment of v and w
     achieving this maximum score. Use the BLOSUM62 scoring matrix, a gap opening penalty of 11, and
     a gap extension penalty of 1.
           8
           PRT---EINS
           PRTWPSEIN-
           
    Input:
         YHFDVPDCWAHRYWVENPQAIAQMEQICFNWFPSMMMKQPHVFKVDHHMSCRWLPIRGKKCSSCCTRMRVRTVWE
         YHEDVAHEDAIAQMVNTFGFVWQICLNQFPSMMMKIYWIAVLSAHVADRKTWSKHMSCRWLPIISATCARMRVRTVWE

    Output:
        144
        YHFDVPDCWAHRYWVENPQAIAQME-------QICFNWFPSMMMK-------QPHVFKV---DHHMSCRWLPIRGKKCSSCCTRMRVRTVWE
        YHEDV----AHE------DAIAQMVNTFGFVWQICLNQFPSMMMKIYWIAVLSAHVADRKTWSKHMSCRWLPI----ISATCARMRVRTVWE

'''

import collections   
import itertools
import datetime
import sys

#This is very good example and coding week6 code also
sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_7_4_data_set4.txt', 'r')
in_table = open('w_7_4_BLOSUM62.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 0
in_s = ""
in_t = ""
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(line==0):
        in_s = ldata;
    elif(line==1):
        in_t = ldata;    
    line+=1

#print in_s, in_t, len(in_s), len(in_t)
#print ""

score={}
line=0
for in_data in in_table:
    ldata = in_data.strip('\t\n\r')
    ldata = ldata.replace("  ", " ")
    sv = ldata.split(" ")
    if(line==0):
        s='0'
        sv.remove('')
        sv.remove('')
    elif(line>0):
        s=sv[0]
        sv.remove(s)
    score[s]=sv    
    line+=1    

def PrintTable():
    for i in range(0,len(in_s)+1):
        sv =in_s[i-1:i]
        if(len(sv)==0):
            print "  ",i,
        else:
            print sv+" ",i,
        for j in range(0,len(in_t)+1):
            #print str(dist[i][j])+"-"+back[i][j]+"\t" ,
            print str(upper[i][j])+'~'+str(middle[i][j])+'~'+str(lower[i][j])+"\t" ,
        print ""
    print "     \t\t",    
    for i in range(0,(len(in_t)+1)):
        print in_t[i:i+1]+"\t" ,
    print ""

def PrintBackTrackTable():
    print "     \t",
    for i in range(0,(len(in_t)+1)):
        print in_t[i:i+1]+"\t" ,
    print ""
    for i in range(0,len(in_s)+1):
        sv =in_s[i-1:i]
        if(len(sv)==0):
            print "  ",i,
        else:
            print sv+" ",i,	
        for j in range(0,len(in_t)+1):
            print str(back[i][j])+" " +str(j)+"\t",
        print ""
    
 
lower={}
upper={}
middle={}
mback={}
uback={}
lback={}
h=-1
g=-11
for i in range(0,(len(in_s)+1)):
    lower[i]=map(int,list('0'*(len(in_t)+1)))
    upper[i]=map(int,list('0'*(len(in_t)+1)))
    middle[i]=map(int,list('0'*(len(in_t)+1)))
    mback[i]=list('-'*(len(in_t)+1))
    uback[i]=list('-'*(len(in_t)+1))
    lback[i]=list('-'*(len(in_t)+1))

for i in range(0,(len(in_s)+1)):
    #global Alignment
    upper[i][0]=-float("inf")
    middle[i][0]=-float("inf")

for j in range(0,(len(in_t)+1)):
    #global alignment
    lower[0][j]=-float("inf")
    middle[0][j]=-float("inf")
    
for i in range(0,(len(in_s)+1)):
     lower[i][0]=h+g*i
     if(i!=0):
         lback[i][0]='v'
         mback[i][0]='v.'
     
for j in range(0,(len(in_t)+1)):
    upper[0][j]=h+g*j
    if(j!=0):
        uback[0][j]='>'
        mback[0][j]='>.'
    
middle[0][0] =0
#M(0,0) = 0, Ix(i,0)=h+g*i, Iy(0,j)=h+g*j

##print>>ou_file,(len(in_t)+1), (len(in_s)+1)
##print>>ou_file,''
##print>>ou_file,lower
##print>>ou_file,''
##print>>ou_file,upper
##print>>ou_file,''
##print>>ou_file,middle
##print>>ou_file,''


for i in range(1,(len(in_s)+1)):
    for j in range(1,(len(in_t)+1)):
        #global Alignment

        
        lie = lower[i-1][j]+h
        mis = middle[i-1][j]+g
        
        uje = upper[i][j-1]+h
        mjs = middle[i][j-1]+g
        
        lower[i][j]=max(lie, mis)
        upper[i][j]=max(uje, mjs)
     
        svi = in_s[i-1:i]
        tvj = in_t[j-1:j]
        fs = int(score[svi][score['0'].index(tvj)])
        #if (svi==tvj):
        #    fs =1
        #else:
        #    fs =-1
        lij = lower[i][j]
        uij = upper[i][j]
        mijfs = middle[i-1][j-1]+fs     
        middle[i][j]=max(lij, uij,mijfs)
        
        
        if (middle[i][j]==uij):
            mback[i][j]=">."
        elif (middle[i][j]==lij):
            mback[i][j]="v."
        elif (middle[i][j]==mijfs):
            mback[i][j]="\\"    

        #.v =0 and v =2    
        if (lower[i][j]==mis):
            lback[i][j]=".v"
        elif (lower[i][j]==lie):
            lback[i][j]="v"

        if (upper[i][j]==mjs):
            uback[i][j]=".>"
        elif (upper[i][j]==uje):
            uback[i][j]=">"    

        #print i,j, lij, uij, mijfs,  middle[i][j], mback[i][j]    
        #print i,j,svi, tvj, fs,' ~ ' , lower[i-1][j-1], upper[i-1][j-1], middle[i-1][j-1], ' ~ ', lij, uij, mijfs,  middle[i][j],back[i][j]
        #print '  L ',lie, mis ,lower[i][j]
        #print i,j, svi, tvj, '  U ',uje, mjs, upper[i][j], ' ~ ' , upper[i][j-1],g, middle[i][j-1],h,g 
        #print ''
        
print>>ou_file,middle
print>>ou_file,''
print>>ou_file,lower
print>>ou_file,''
print>>ou_file,upper
print>>ou_file,''
print>>ou_file,mback
print>>ou_file,''
print>>ou_file,lback    
print>>ou_file,''
print>>ou_file,uback

#PrintTable()
##print ""
###PrintBackTrackTable()

def SplitValue(res):
    res1=''
    res2=''
    count=0
    for i in range(0,len(res),2):
        res1+=res[i]
        res2+=res[i+1]
    #print " ",res1
    #print " ",res2
        
    ou_file.write(res1 +"\n")
    ou_file.write(res2 +"\n\n")

print ''

def OUTPUTLCS(i,j):
    #print i,j
    #if(j==0):
    #   return in_s[i-1:i]+"-"
    if(i==0 or j==0):
        return ""
    mv = middle[i][j]
    uv = upper[i][j]
    lv = lower[i][j]
    mul = max(mv,uv,lv)
    move="0"
    #if(mul==mv):
    move=mback[i][j]
    #el
    if(mul==mv):
         move=mback[i][j]
    elif(mul==uv):
         move=uback[i][j]
    elif(mul==lv):
         move=lback[i][j]

    print i, j , mul, move, in_s[i-1:i], in_t[j-1:j]
    if (move=="v."):
        move=lback[i][j]
        print ' v.' , move
    if (move==">."):
        move=uback[i][j]
        print ' >.' , move
         
    #print i, j ,mback[i][j], uback[i][j],lback[i][j], mv, uv, lv, mul, move, in_s[i-1:i], in_t[j-1:j]
    #print i, j , mul, move, in_s[i-1:i], in_t[j-1:j]
    
    if (move==">" or move==".>"):
        return OUTPUTLCS(i,j-1)+"-"+in_t[j-1:j]
    elif (move=="v" or move==".v"):
        return OUTPUTLCS(i-1,j)+in_s[i-1:i]+"-"
    else:    
        return OUTPUTLCS(i-1,j-1)+in_s[i-1:i]+in_t[j-1:j]
    
maxi=len(in_s)
maxj=len(in_t)
print>>ou_file,middle[maxi][maxj]
res = OUTPUTLCS(maxi, maxj)
#print res
SplitValue(res)

 
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"

#BLOSUM62.txt
'''
   A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
C  0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
D -2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
E -1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
F -2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
G  0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
H -2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
I -1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
K -1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
L -1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
M -1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
N -2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
P -1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
Q -1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
R -1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
S  1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
T  0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
V  0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
W -3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
Y -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7
'''
