'''
Edit distance between two strings.
     Input: Two strings.
             PLEASANTLY
             MEANLY
     Output: The edit distance between these strings.
             5    
'''

import collections   
import itertools
import datetime
import sys

#This is very good example and coding week6 code also
sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_7_2_data_set1.txt', 'r')
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
    for i in range(len(in_s),-1,-1):
        sv =in_s[i:i+1]
        if(len(sv)==0):
            print "  ",
        else:
            print sv+" ",
        for j in range(0,len(in_t)+1):
            print str(dist[i][j])+"-"+back[i][j]+"\t" ,
            #print str(dist[i][j])+"\t" ,
        print ""
    print "     \t",    
    for i in range(0,(len(in_t)+1)):
        print in_t[i:i+1]+"\t" ,
    print ""

def PrintBackTrackTable():
    for i in range(len(in_s),-1,-1):
        sv =in_s[len(in_s)-i:len(in_s)-i+1]
        if(len(sv)==0):
            print "  ",
        else:
            print sv+" ",
        for j in range(0,len(in_t)+1):
            print str(back[i][j])+"\t" ,
        print ""
    print "     \t",    
    for i in range(0,(len(in_t)+1)):
        print in_t[i:i+1]+"\t" ,
    print ""
    
dist={}
back={}
for i in range(0,(len(in_s)+1)):
    dist[i]=map(int,list('0'*(len(in_t)+1)))
    back[i]=list(' '*(len(in_t)+1))

for i in range(len(in_s),-1,-1):
     dist[i][0]= i

for i in range(0,(len(in_t)+1)):
    dist[0][i]= i

for i in range(1,(len(in_s)+1)):
    for j in range(1,(len(in_t)+1)):
        dimj = dist[i-1][j]+1
        dijm = dist[i][j-1]+1
        dimjm = dist[i-1][j-1]
        svi = in_s[i-1:i]
        tvj = in_t[j-1:j]
        if (svi!=tvj):
            dimjm+=1
        elif (svi==tvj):
            dimjm+=0    
        #else:
        #    dimjm+=0
        dist[i][j]=min(dimj, dijm, dimjm)
##        if (dist[i][j]==dimj):
##            back[i][j]="2"
##        elif (dist[i][j]==dijm):
##            back[i][j]+="1"
##        elif (dist[i][j]==dimjm):
##            back[i][j]+="0"
        if (dist[i][j]==dimj):
            back[i][j]="D"
        if (dist[i][j]==dijm):
            back[i][j]+="I"
        if (dist[i][j]==dimjm):
            back[i][j]+="S"

        #print i,j,dimj, dijm, dimjm, svi, tvj ,dist[i][j]

print dist[len(in_s)][len(in_t)]

#Not Used for this problem

#PrintDistanceTable()
#print ""
#PrintBackTrackTable()

def OUTPUTLCS(i,j):
    #print i,j, back[i][j]
    #if(i==0 or j==0):
    if(i==0 and j!=0):
        return +"*"+in_t[j-1:j]
    elif(i!=0 and j==0):
        return in_s[i-1:i]+"*"
    elif(i==0 and j==0):
        return in_s[i-1:i]+in_t[j-1:j]    
    if (back[i][j].find("I")!=-1):
        #print " I", " -" +in_t[j-1:j]
        return OUTPUTLCS(i,j-1)+"*"+in_t[j-1:j]
    elif (back[i][j].find("D")!=-1):
        #print " D", in_s[len(in_s)-i:len(in_s)-i+1]+"- "
        return OUTPUTLCS(i-1,j)+in_s[i-1:i]+"*"
    #if (back[i][j].find("S")!=-1):
    else:    
        #print " S", in_s[len(in_s)-i:len(in_s)-i+1]+"-"+in_t[j-1:j]
        return OUTPUTLCS(i-1,j-1)+in_s[i-1:i]+in_t[j-1:j]
    
res = OUTPUTLCS(len(in_s), len(in_t));
#print res
res1=''
res2=''
count=0
for i in range(0,len(res),2):
    res1+=res[i]
    res2+=res[i+1]
    if (res[i]!=res[i+1]):
       count+=1; 
    #print res[i],res[i+1]
#print res1
#print res2
print count
ou_file.write(res1 +"\n")
ou_file.write(res2 +"\n")

tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
