'''
The Middle Edge in Linear Space Problem (for protein strings). Use the BLOSUM62 scoring matrix and a linear indel penalty equal to 5.
     Input: Two amino acid strings.
           PLEASANTLY
           MEASNLY

     Output: A middle edge in the alignment graph in the form “(i, j) (k, l)”, where (i, j) connects to (k, l).
     To compute scores, use the BLOSUM62 scoring matrix and a (linear) indel penalty equal to 5.
         (4, 3) (5, 4)
'''
import collections   
import itertools
import datetime
import sys

#This is very good example and coding week6 code also
sys.setrecursionlimit(10000)
tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_7_5_data_set0.txt', 'r')
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
    
 
dist={}
dist2={}
fback={}
sback={}
d=-5
fh = (len(in_t)/2)+1
sh = len(in_t)-fh+2
for i in range(0,(len(in_s)+1)):
    dist[i]=map(int,list('0'*(len(in_t)+1)))
    dist2[i]=map(int,list('0'*(len(in_t)+1)))
    fback[i]=list('.'*(len(in_t)+1))
    sback[i]=list('.'*(len(in_t)+1))
 
for i in range(0,(len(in_s)+1)):
    dist[i][0]= i*d
    dist2[i][0]= i*d
    if(i!=0):
        fback[i][0]= "v"
        sback[i][0]= "v"

for j in range(0,(len(in_t)+1)):
   dist[0][j]= j*d
   dist2[0][j]= j*d
   if(i!=0):
        fback[0][j]= ">"
        sback[0][j]= ">"

     
#print in_s, in_t,len(in_t), len(in_t)/2, fh, sh
#print first
#print second

for i in range(1,(len(in_s)+1)):
    for j in range(1,(len(in_t)+1)):
        svi = in_s[i-1:i]
        tvj = in_t[j-1:j]
        fs = int(score[svi][score['0'].index(tvj)])
        dimj = dist[i-1][j]+d
        dijm = dist[i][j-1]+d
        dimjm = dist[i-1][j-1]+fs
 
        dist[i][j]=max(dimj, dijm, dimjm)
       
        if (dist[i][j]==dimj):
            fback[i][j]="v"
        elif (dist[i][j]==dijm):
            fback[i][j]=">"
        elif (dist[i][j]==dimjm):
            fback[i][j]="\\"    
        #print i,j,dimj, dijm, dimjm,  dist[i][j],back[i][j]


for i in range(1,(len(in_s)+1)):
    for j in range(1,(len(in_t)+1)):
        svi = in_s[len(in_s)-i:len(in_s)-i+1]
        tvj = in_t[len(in_t)-j:len(in_t)-j+1]
        fs = int(score[svi][score['0'].index(tvj)])
        dimj = dist2[i-1][j]+d
        dijm = dist2[i][j-1]+d
        dimjm = dist2[i-1][j-1]+fs
 
        dist2[i][j]=max(dimj, dijm, dimjm)
##        if (dist[i][j]==dimjm):
##            back[i][j]="0"
##        elif (dist[i][j]==dimj):
##            back[i][j]="2"
##        elif (dist[i][j]==dijm):
##            back[i][j]="1"
        #print i,j,svi, tvj, dimj, dijm, dimjm

msov = 0
msoi=msii=0
msoj=msij=0
msik = 0
for i in range(0,(len(in_s)+1)):
    d = dist[i][len(in_t)/2]
    d2 = dist2[len(in_s)-i][len(in_t)/2+1]
    d3 = dist[len(in_s)-i][len(in_t)/2]
    d4 = dist2[i][len(in_t)/2+1]
    if((d+d2)>msov):
        msov = d+d2
        msoi =i
        msoj = len(in_t)/2

        
print msov, msoi, msoj ,msoi+1, msoj+1
#print msik, msii, msij
print>>ou_file,"(",msoi, msoj,") (" ,msoi+1, msoj+1, ")"

        
#print>>ou_file,dist
#print>>ou_file,''
#print>>ou_file,dist2
#print>>ou_file,''
#print>>ou_file,fback    
#print>>ou_file,''
##print>>ou_file,uback


 
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"

