'''
Implement LINEAR SPACE ALIGNMENT to solve the Global Alignment Problem for a large dataset.
     Input: Two long (10000 amino acid) protein strings written in the single-letter amino acid alphabet.
         PLEASANTLY
         MEANLY
     Output: The maximum alignment score of these strings, followed by an alignment achieving this maximum score. 
     Use the BLOSUM62 scoring matrix and indel penalty s = 5.
         8
         PLEASANTLY
         -MEA--N-LY
'''

# -*- coding: utf-8 -*-
import collections   
import itertools
import datetime
import sys

##Need to rewrite used 7_6_GA code
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
in_so = ""
in_to = ""

for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(line==0):
        in_s = ldata;
        in_so = in_s;
    elif(line==1):
        in_t = ldata;
        in_to =in_t;
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

##def PrintTable():
##    for i in range(0,len(in_s)+1):
##        sv =in_s[i-1:i]
##        if(len(sv)==0):
##            print "  ",i,
##        else:
##            print sv+" ",i,
##        for j in range(0,len(in_t)+1):
##            #print str(dist[i][j])+"-"+back[i][j]+"\t" ,
##            print str(upper[i][j])+'~'+str(middle[i][j])+'~'+str(lower[i][j])+"\t" ,
##        print ""
##    print "     \t\t",    
##    for i in range(0,(len(in_t)+1)):
##        print in_t[i:i+1]+"\t" ,
##    print ""
##
##def PrintBackTrackTable():
##    print "     \t",
##    for i in range(0,(len(in_t)+1)):
##        print in_t[i:i+1]+"\t" ,
##    print ""
##    for i in range(0,len(in_s)+1):
##        sv =in_s[i-1:i]
##        if(len(sv)==0):
##            print "  ",i,
##        else:
##            print sv+" ",i,	
##        for j in range(0,len(in_t)+1):
##            print str(back[i][j])+" " +str(j)+"\t",
##        print ""
##    
 
##dist={}
##dist2={}
##fback={}
##sback={}
##msov = msoi=msoj=0
def MiddleEdgeLinear():
    global msov, msoi, msoj
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
            if (dist2[i][j]==dimj):
                sback[i][j]="v"
            elif (dist2[i][j]==dijm):
                sback[i][j]=">"
            elif (dist2[i][j]==dimjm):
                sback[i][j]="\\"   
            #print i,j,svi, tvj, dimj, dijm, dimjm


    for i in range(0,(len(in_s)+1)):
        d = dist[i][len(in_t)/2]
        d2 = dist2[len(in_s)-i][len(in_t)/2+1]
        d3 = dist[len(in_s)-i][len(in_t)/2]
        d4 = dist2[i][len(in_t)/2+1]
        if((d+d2)>msov):
            msov = d+d2
            msoi =i
            msoj = len(in_t)/2


##def SplitValue(res):
##    res1=''
##    res2=''
##    count=0
##    for i in range(0,len(res),2):
##        res1+=res[i]
##        res2+=res[i+1]
##    #print " ",res1
##    #print " ",res2
##        
##    ou_file.write(res1 +"\n")
##    ou_file.write(res2 +"\n\n")
    
##def OUTPUTLCS(bt,i,j,s,e):
##    #print i,j, s,e,bt[i][j]
##    #if(i==0 or j==0):
##    if(i==s and j!=e):
##        return +"-"+in_t[j-1:j]
##    elif(i!=s and j==e):
##        return in_s[i-1:i]+"-"
##    elif(i==s and j==e):
##        return in_s[i-1:i]+in_t[j-1:j]    
##    if (bt[i][j].find(">")!=-1):
##        return OUTPUTLCS(bt,i,j-1,s,e)+"-"+in_t[j-1:j]
##    elif (bt[i][j].find("v")!=-1):
##        return OUTPUTLCS(bt,i-1,j,s,e)+in_s[i-1:i]+"-"
##    else:    
##        return OUTPUTLCS(bt,i-1,j-1,s,e)+in_s[i-1:i]+in_t[j-1:j]
##
##
##def OUTPUTLCSB(bt,i,j,s,t):
##    #print i,j, s,t,bt[i][j]
##    #if(i==0 or j==0):
##    if(i==0 and j!=0):
##        return +"-"+in_t[t-1:t]
##    elif(i!=0 and j==0):
##        return in_s[s-1:s]+"-"
##    elif(i==0 and j==0):
##        return in_s[s-1:s]+in_t[t-1:t]    
##    if (bt[i][j].find(">")!=-1):
##        return OUTPUTLCSB(bt,i,j-1,s,t-1)+"-"+in_t[t-1:j]
##    elif (bt[i][j].find("v")!=-1):
##        return OUTPUTLCSB(bt,i-1,j,s-1,t)+in_s[s-1:s]+"-"
##    else:    
##        return OUTPUTLCSB(bt,i-1,j-1,s-1,t-1)+in_s[s-1:s]+in_t[t-1:+t]

def MiddleNode(top, bottom, left, right):
    if (top<0):
        top=0
    return dist[top][left]

def MiddleEdge(top, bottom, left, right):
    if (top<0):
        top=0
    return fback[top][left]

def LINEARSPACEALIGNMENT(p,top, bottom, left, right):
    #print p,top, bottom, left, right
    if (left == right):
        #print "alignment formed by bottom - top vertical edges"
        #print in_s[0:bottom-top],"-"
        return
        #return alignment formed by bottom - top vertical edges
    middle = (left + right)/2
    midNode = MiddleNode(top, bottom, left, right)
    midEdge = MiddleEdge(top, bottom, left, right)
    print middle, midNode, midEdge
    LINEARSPACEALIGNMENT(1, top, midNode, left, middle)
    #output midEdge
    if midEdge == ">" or midEdge == "\\":
        middle = middle + 1
    if midEdge == "v" or midEdge =="\\":
        midNode = midNode + 1
    LINEARSPACEALIGNMENT(2,midNode, bottom, middle, right)

dist={}
dist2={}
fback={}
sback={}
msov = msoi=msoj=0
MiddleEdgeLinear()
bottom = msoi
top = msoi
if(bottom==0):
    bottom=len(in_s)
else:
    bottom+=1

right = msoj
left = msoj
if(left==0):
    right=len(in_t)
else:
    right+=1
meoi=bottom
meoj=right
while (True):
    print in_s, in_t, msoi, msoj
    LINEARSPACEALIGNMENT(0,top, bottom, left, right)
    if (msoi==0 or msoj==0):
        break
    in_s=in_s[0:msoi]
    in_t=in_t[0:msoj]
    dist={}
    dist2={}
    fback={}
    sback={}
    msov = msoi=msoj=0
    MiddleEdgeLinear()
    bottom = msoi
    top = msoi
    if(bottom==0):
        bottom=len(in_s)
    else:
        bottom+=1

    right = msoj
    left = msoj
    if(left==0):
        right=len(in_t)
    else:
        right+=1   


in_s=in_so[meoi-1:len(in_so)]
in_t=in_to[meoj-1:len(in_to)]
dist={}
dist2={}
fback={}
sback={}
msov = msoi=msoj=0
while (True):
    print in_s, in_t, msoi, msoj
    MiddleEdgeLinear()
    bottom = msoi
    top = msoi
    if(bottom==0):
        bottom=len(in_s)
    else:
        bottom+=1

    right = msoj
    left = msoj
    if(left==0):
        right=len(in_t)
    else:
        right+=1    
    LINEARSPACEALIGNMENT(0,top, bottom, left, right)
    if (msoi==0 or msoj==0):
        break
    in_s=in_s[0:msoi]
    in_t=in_t[0:msoj]
    dist={}
    dist2={}
    fback={}
    sback={}
    msov = msoi=msoj=0
    
#print len(in_s),len(in_t) ,len(in_s)/2+1   
#res = OUTPUTLCS(fback, top, left,0,0);
#print res
#SplitValue(res)

#res = OUTPUTLCSB(sback, bottom, right,len(in_s),len(in_t));
#print res
#SplitValue(res)
    
#print len(in_s),len(in_t),msov, top, left ,bottom, right

#print msik, msii, msij
#print>>ou_file,"(",top, left,") (" ,bottom, right, ")"
print>>ou_file,dist
print>>ou_file,""
print>>ou_file,dist2
print>>ou_file,""
print>>ou_file,fback
print>>ou_file,""
print>>ou_file,sback
 
tend = datetime.datetime.now()
#print len(res),res
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"


#7_6_GA code
'''
import collections   
import itertools
import datetime
import sys

sys.setrecursionlimit(10000)

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_7_6_data_set2.txt', 'r')
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
        #print iv, jv
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
    #global res
    #if(i==-1 or j==-1 or (i==0 and j==0)):
    #    return ''
    if(i==0 and j!=0):
        return +"-"+in_t[t-1:t]
    elif(i!=0 and j==0):
        return in_s[s-1:s]+"-"
    elif(i==0 and j==0):
        return in_s[s-1:s]+in_t[t-1:t] 
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
#print sa[len(in_s)][len(in_t)]
#print res1
#print res2
ou_file.write(str(sa[len(in_s)][len(in_t)]) +"\n")
ou_file.write(res1 +"\n")
ou_file.write(res2 +"\n")
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
ou_file.close()
print "Done"

'''
