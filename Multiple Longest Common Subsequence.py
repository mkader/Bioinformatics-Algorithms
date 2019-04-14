'''
In the Multiple Longest Common Subsequence Problem, the score of a column of the alignment matrix is equal to 1 if all of the 
column’s symbols are identical, and 0 if even one symbol disagrees.

CODE CHALLENGE: Solve the Multiple Longest Common Subsequence Problem.
     Input: Three DNA strings.
             ATATCCG
             TCCGA
             ATGTACTG
     Output: The length of a longest common subsequence of these three strings, followed by a multiple alignment of the three strings corresponding to such an alignment.
             3
             ATATCC-G-
             ---TCC-GA
             ATGTACTG-
'''
import collections   
import itertools
import datetime
import sys

#This is very good example and coding week6 code also
sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_7_7_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 0
in_s = ""
in_t = ""
in_k = ""
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(line==0):
        in_s = ldata;
    elif(line==1):
        in_t = ldata;
    elif(line==2):
        in_k = ldata;     
    line+=1

#print in_s, in_t, len(in_s), len(in_t)
#print ""

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
    

#print in_k 
dist={}
back={}

for i in range(0,(len(in_s)+1)):
    #dist[i]= map(int,list('0'*(len(in_t)+1)))
    for j in range(0,(len(in_t)+1)):
        for k in range(0,(len(in_k)+1)):
            #print i,j,k
            dist[i,j,k]=0
#print dist

##for i in range(0,(len(in_s)+1)):
##    dist[i]=map(int,list('0'*(len(in_t)+1)))
## 
##for i in range(0,(len(in_s)+1)):
##    dist[i][0]= i*d
##    dist2[i][0]= i*d
##    if(i!=0):
##        fback[i][0]= "v"
##        sback[i][0]= "v"
##
##for j in range(0,(len(in_t)+1)):
##   dist[0][j]= j*d
##   dist2[0][j]= j*d
##   if(i!=0):
##        fback[0][j]= ">"
##        sback[0][j]= ">"
##
##     
###print in_s, in_t,len(in_t), len(in_t)/2, fh, sh
###print first
###print second
##
for i in range(1,(len(in_s)+1)):
    for j in range(1,(len(in_t)+1)):
        for k in range(1,(len(in_k)+1)):
            svi = in_s[i-1:i]
            tvj = in_t[j-1:j]
            kvk = in_k[j-1:j]
            sc=0
            di1jk = dist[i-1,j,k]+sc
            dij1k = dist[i,j-1,k]+sc
            dijk1 = dist[i,j,k-5]+sc
##        dijm = dist[i][j-1]+d
##        dimjm = dist[i-1][j-1]+fs
## 
##        dist[i][j]=max(dimj, dijm, dimjm)
##       
##        if (dist[i][j]==dimj):
##            fback[i][j]="v"
##        elif (dist[i][j]==dijm):
##            fback[i][j]=">"
##        elif (dist[i][j]==dimjm):
##            fback[i][j]="\\"    
##        #print i,j,dimj, dijm, dimjm,  dist[i][j],back[i][j]
##
##
##for i in range(1,(len(in_s)+1)):
##    for j in range(1,(len(in_t)+1)):
##        svi = in_s[len(in_s)-i:len(in_s)-i+1]
##        tvj = in_t[len(in_t)-j:len(in_t)-j+1]
##        fs = int(score[svi][score['0'].index(tvj)])
##        dimj = dist2[i-1][j]+d
##        dijm = dist2[i][j-1]+d
##        dimjm = dist2[i-1][j-1]+fs
## 
##        dist2[i][j]=max(dimj, dijm, dimjm)
####        if (dist[i][j]==dimjm):
####            back[i][j]="0"
####        elif (dist[i][j]==dimj):
####            back[i][j]="2"
####        elif (dist[i][j]==dijm):
####            back[i][j]="1"
##        #print i,j,svi, tvj, dimj, dijm, dimjm
##
##msov = 0
##msoi=msii=0
##msoj=msij=0
##msik = 0
##for i in range(0,(len(in_s)+1)):
##    d = dist[i][len(in_t)/2]
##    d2 = dist2[len(in_s)-i][len(in_t)/2+1]
##    d3 = dist[len(in_s)-i][len(in_t)/2]
##    d4 = dist2[i][len(in_t)/2+1]
##    if((d+d2)>msov):
##        msov = d+d2
##        msoi =i
##        msoj = len(in_t)/2
##
##        
##print msov, msoi, msoj ,msoi+1, msoj+1
###print msik, msii, msij
##print>>ou_file,"(",msoi, msoj,") (" ,msoi+1, msoj+1, ")"
##
##        
###print>>ou_file,dist
###print>>ou_file,''
###print>>ou_file,dist2
###print>>ou_file,''
###print>>ou_file,fback    
###print>>ou_file,''
####print>>ou_file,uback


 
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"
