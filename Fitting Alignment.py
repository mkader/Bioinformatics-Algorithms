'''
     Input: Two nucleotide strings v and w, where v has length at most 1000 and w has length at most 100.
             GTAGGCTTAAGGTTA
             TAGATA
     Output: A highest-scoring fitting alignment between v and w. Use the simple scoring method in which
     matches count +1 and both the mismatch and indel penalties are 1.
           2
           TAGGCTTA
           TAGA--TA
'''
import collections   
import itertools
import datetime
import sys

#This is very good example and coding week6 code also
sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_7_2_data_set4.txt', 'r')
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

def PrintDistanceTable():
    for i in range(0,len(in_s)+1):
        sv =in_s[i-1:i]
        if(len(sv)==0):
            print "  ",i,
        else:
            print sv+" ",i,
        for j in range(0,len(in_t)+1):
            #print str(dist[i][j])+"-"+back[i][j]+"\t" ,
            print str(dist[i][j])+"\t" ,
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
    
 
    
dist={}
back={}
d=m=s=1
for i in range(0,(len(in_s)+1)):
    dist[i]=map(int,list('0'*(len(in_t)+1)))
    back[i]=list('0'*(len(in_t)+1))

for i in range(len(in_s),-1,-1):
     dist[i][0]= 0

for i in range(0,(len(in_t)+1)):
    dist[0][i]= -1*i*d
#in_s= in_s[::-1]
for i in range(1,(len(in_s)+1)):
    for j in range(1,(len(in_t)+1)):
        dimj = dist[i-1][j]-d
        dijm = dist[i][j-1]-d
        dimjm = dist[i-1][j-1]
        svi = in_s[i-1:i]
        tvj = in_t[j-1:j]
        if (svi!=tvj):
            dimjm-=s
        elif (svi==tvj):
            dimjm+=m    
        dist[i][j]=max(dimj, dijm, dimjm)
        if (dist[i][j]==dimjm):
            back[i][j]="0"
        elif (dist[i][j]==dimj):
            back[i][j]="2"
        elif (dist[i][j]==dijm):
            back[i][j]="1"
        #print i,j,dimj, dijm, dimjm,  dist[i][j],back[i][j]


#PrintDistanceTable()
print ""
#PrintBackTrackTable()


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

def OUTPUTLCS(i,j):
    #print i,j, back[i][j]
    if(i==0 or j==0):
        return ""
    if (back[i][j]=="1"):
        return OUTPUTLCS(i,j-1)+"-"+in_t[j-1:j]
    elif (back[i][j]=="2"):
        return OUTPUTLCS(i-1,j)+in_s[i-1:i]+"-"
    else:    
        return OUTPUTLCS(i-1,j-1)+in_s[i-1:i]+in_t[j-1:j]

maxv=0
maxi=0
maxj=len(in_t)
for i in range(0,(len(in_s)+1)):
  if(dist[i][len(in_t)]>maxv):
        maxv=dist[i][len(in_t)]
        maxi=i

print>>ou_file,dist[maxi][maxj]
res = OUTPUTLCS(maxi, maxj)
SplitValue(res)



tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
