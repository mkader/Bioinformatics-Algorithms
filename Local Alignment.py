'''
You might still be wondering how we can take these free taxi rides through the align- ment graph. 
The point is that you are in charge of designing whatever Manhattan-like DAG you like, as long as 
it adequately models the specific alignment problem at hand. Transformations like free taxi rides 
will become a common theme in this chapter; various alignment problems can be solved by constructing 
an appropriate DAG with as few edges as possible (to minimize runtime), assigning edge weights to 
model the requirements of the problem, and then finding a longest path in this DAG.

     Input: Two protein strings written in the single-letter amino acid alphabet.
           MEANLY
           PENALTY
      Output: The maximum score of a local alignment of the strings, followed by a local alignment of these
     strings achieving the maximum score. Use the PAM250 scoring matrix and indel penalty s = 5.
           15
           EANL-Y
           ENALTY
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_6_3_data_set0.txt', 'r')
in_table = open('6_6_PAM250_1.txt', 'r')
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

#for i,sv in enumerate(score):
#    print sv, score[sv]


indel=5
sa={}
for i in range(0,len(in_s)+1):
    sa[i]=map(int,list('0'*(len(in_t)+1)))

   
bt={}
for i in range(0,len(in_s)+1):
    bt[i]=list('-'*(len(in_t)+1))


#print sa 
for i in range(1,len(in_s)+1):
    iv=in_s[i-1]
    for j in range(1,len(in_t)+1):
        jv =in_t[j-1]
        simj = sa[i-1][j]-indel
        sijm = sa[i][j-1]-indel
        sij  = 0
        fs = int(score[iv][score['0'].index(jv)])
        if (iv!=jv):
           sij = sa[i-1][j-1]+fs
           #sij = sa[i-1][j-1]+1
        if(iv==jv):
           sij = sa[i-1][j-1]+fs
           #sij = sa[i-1][j-1]+1
        sa[i][j]=max(0,simj,sijm,sij)
       #print i,j,iv,jv,fs,sa[i-1][j-1],sij,simj,sijm, sa[i][j]
        if (sa[i][j]==sa[i-1][j]-indel):
           bt[i][j] = "D"
        elif (sa[i][j]==sa[i][j-1]-indel):
            bt[i][j] = "R"
        elif (sa[i][j]==sa[i-1][j-1]+indel):
            bt[i][j] = "C"

mv = -1
mi=0
mj=0
for i in range(0,len(in_s)+1):
    for j in range(0,len(in_t)+1):
        if(sa[i][j]>mv):
            mv=sa[i][j]
            mi=i
            mj=j
#print mi,mj,mv, sa[len(in_s)][len(in_t)]
##
##for i in range(0,len(in_s)):
##    print i, bt[i]
    
def OUTPUTLCS(i,j):
    if(i==0 or j==0):
        return ''
    #print i,j,bt[i][j],in_s[i-1],in_t[j-1]
    if (bt[i][j] == "D" ):
        return OUTPUTLCS(i - 1, j)+in_s[i-1]+"-";
    elif (bt[i][j] == "R"):
        return OUTPUTLCS(i, j - 1)+"-"+in_t[j-1]
    else:
        return OUTPUTLCS(i - 1, j - 1)+in_s[i-1]+in_t[j-1];
   
res = OUTPUTLCS(mi, mj) #len(in_s), len(in_t));
#print res
tend = datetime.datetime.now()
res1=''
res2=''
for i in range(0,len(res),2):
    res1+=res[i]
    res2+=res[i+1]
    #print res[i],res[i+1]
print sa[mi][mj]
print res1
print res2
ou_file.write(str(sa[mi][mj]) +"\n")
ou_file.write(res1 +"\n")
ou_file.write(res2 +"\n")
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"

#6_6_PAM250_1
'''
   A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3
C -2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0
D  0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4
E  0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4
F -3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7
G  1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5
H -1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0
I -1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1
K -1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4
L -2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1
M -1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2
N  0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2
P  1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5
Q  0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4
R -2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4
S  1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3
T  1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3
V  0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2
W -6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0
Y -3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10
'''
