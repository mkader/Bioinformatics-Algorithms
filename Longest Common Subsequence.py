'''
     Input: Two strings s and t.
             AACCTTGG
             ACACTGTGA
     Output: A longest common subsequence of s and t.
             AACTGG

    OUTPUTLCS(backtrack, v, i, j)
        if i = 0 or j = 0
            return
        if backtracki, j = ?
            OUTPUTLCS(backtrack, v, i - 1, j)
        else if backtracki, j = ?
            OUTPUTLCS(backtrack, v, i, j - 1)
        else
            OUTPUTLCS(backtrack, v, i - 1, j - 1)
            output vi
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_6_3_data_set0.txt', 'r')

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

print in_s, in_t, len(in_s), len(in_t)

#for i in range(0,len(in_s)):
#sa = [map(int,list('0'*len(in_t)))] * len(in_s)
bt = [list('-'*len(in_t))] * len(in_t)

sa={}
for i in range(0,len(in_s)):
    sa[i]=map(int,list('0'*len(in_t)))

bt={}
for i in range(0,len(in_s)):
    bt[i]=list('-'*len(in_t))
    
#print sa 
for i in range(1,len(in_s)):
    iv=in_s[i-1]
    for j in range(1,len(in_t)):
        jv =in_t[j-1]
        #print i,j,isv,jtv
        simj = sa[i-1][j]
        sijm = sa[i][j-1]
        sij  = 0
        if (iv==jv):
           sij = sa[i-1][j-1]+1
        sa[i][j]=max(simj,sijm,sij)
        #print sa
        #print i, j,sij,sa[i][j],sa[i-1][j]
        if (sa[i][j]==sa[i-1][j]):
           bt[i-1][j-1] = "D"
        elif (sa[i][j]==sa[i][j-1]):
            bt[i-1][j-1] = "R"
        elif (sa[i][j]==(sa[i-1][j-1]+1)):
            bt[i-1][j-1] = "C"

for i in range(0,len(in_s)):
    print i, sa[i]
    
for i in range(0,len(in_s)):
    print i, bt[i]
    
res=''
def OUTPUTLCS(i,j):
    global res
    if(i==0 or j==0):
        return
    #print i,j,bt[i][j]
    if (bt[i][j] == "D"):
        OUTPUTLCS(i - 1, j);
    elif (bt[i][j] == "R"):
        OUTPUTLCS(i, j - 1);
    else:
        OUTPUTLCS(i - 1, j - 1);
        #print i,in_s[i:i+1]
        res += in_s[i:i+1];
    #print res

OUTPUTLCS(len(in_s)-1, len(in_t)-1);
tend = datetime.datetime.now()
print res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
