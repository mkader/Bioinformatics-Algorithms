'''
     Input: Two protein strings written in the single-letter amino acid alphabet.
           PLEASANTLY
           MEANLY
     Output: The maximum alignment score of these strings followed by an alignment achieving this
     maximum score. Use the BLOSUM62 scoring matrix and indel penalty s = 5.
           8
           PLEASANTLY
           -MEA--N-LY
'''
import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_6_3_data_set0.txt', 'r')
in_table = open('6_5_BLOSUM62.txt', 'r')
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

print in_s, in_t, len(in_s), len(in_t)

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


sa={}
for i in range(0,len(in_s)+1):
    sa[i]=map(int,list('0'*(len(in_t)+1)))

for i in range(1,len(in_s)+1):
    sa[i][0]=sa[i-1][0]-5

#for i in range(0,len(in_s)+1):
#    print i, sa[i]

for i in range(1,(len(in_t)+1)):
    #print i,
    sa[0][i]=sa[0][i-1]-5
    #print i, sa[0][i]
    
bt={}
for i in range(0,len(in_s)+1):
    bt[i]=list('-'*(len(in_t)+1))
    
#print sa 
for i in range(1,len(in_s)+1):
    iv=in_s[i-1]
    for j in range(1,len(in_t)+1):
        jv =in_t[j-1]
        simj = sa[i-1][j]-5
        sijm = sa[i][j-1]-5
        sij  = 0
        fs = int(score[iv][score['0'].index(jv)])
        if (iv!=jv):
           sij = sa[i-1][j-1]+fs
        if(iv==jv):
           sij = sa[i-1][j-1]+fs
        sa[i][j]=max(simj,sijm,sij)
        #print i,j,iv,jv,fs,sa[i-1][j-1],sij,simj,sijm
        if (sa[i][j]==sa[i-1][j]-5):
           bt[i][j] = "D"
        elif (sa[i][j]==sa[i][j-1]-5):
            bt[i][j] = "R"
        elif (sa[i][j]==sa[i-1][j-1]+fs):
        #else:
            bt[i][j] = "C"

 
##for i in range(0,len(in_s)+1):
##    print i, sa[i]
##
#for i in range(0,len(in_s)):
#    print i, bt[i]
    
#res=''
def OUTPUTLCS(i,j):
    global res
    if(i==-1 or j==-1 or (i==0 and j==0)):
        return ''
    #print i,j,bt[i][j],in_s[i-1],in_t[j-1]
    if (bt[i][j] == "D" ):
        return OUTPUTLCS(i - 1, j)+in_s[i-1]+"-";
    elif (bt[i][j] == "R"):
        return OUTPUTLCS(i, j - 1)+"-"+in_t[j-1]
    elif(bt[i][j] == "C"):
        return OUTPUTLCS(i - 1, j - 1)+in_s[i-1]+in_t[j-1];
    elif (bt[i][j] == "-" and i==0 and j!=0):
        return OUTPUTLCS(i - 1, j - 1)+"-"+in_t[j-1];
    elif (bt[i][j] == "-" and j==0 and i!=0):
        return OUTPUTLCS(i - 1, j - 1)+in_s[i-1]+"-";
   
res = OUTPUTLCS(len(in_s), len(in_t));
#print res
tend = datetime.datetime.now()
res1=''
res2=''
for i in range(0,len(res),2):
    res1+=res[i]
    res2+=res[i+1]
    #print res[i],res[i+1]
print sa[len(in_s)][len(in_t)]
print res1
print res2
ou_file.write(str(sa[len(in_s)][len(in_t)]) +"\n")
ou_file.write(res1 +"\n")
ou_file.write(res2 +"\n")
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"

#6_5_BLOSUM62
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
