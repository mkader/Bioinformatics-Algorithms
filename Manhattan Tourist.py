'''
Find the length of a longest path in the Manhattan Tourist Problem.
     Input: Integers n and m, followed by an n × (m + 1) matrix down and an (n + 1) × m matrix right.
     The two matrices are separated by the - symbol.
           4 4
           1 0 2 4 3
           4 6 5 2 1
           4 4 5 2 1
           5 6 8 5 3
           -
           3 2 4 0
           3 2 4 2
           0 7 3 3
           3 3 0 2
           1 3 2 2
     Output: The length of a longest path from source (0, 0) to sink (n, m) in the n × m rectangular grid
     whose edges are defined by the matrices down and right.
           34
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_6_2_data_set1.txt', 'r')

line = 0
in_n = 0
in_m = 0
in_matdown={}
in_matright={}
right=True
d=0
mt_tot ={}
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (len(ldata)==0):
        break
    elif(line==0):
        in_n = int(ldata);
    elif(line==1):
        in_m = int(ldata);    
    elif (ldata=="-"):
        d=0
        right= False
    elif(line>1 and right):
        #print map(int, ldata.split(" "));
        in_matdown[d] = map(int, ldata.split(" "));
        d+=1
    elif(not right):
        #print map(int, ldata.split(" ")), d
        in_matright[d] = map(int, ldata.split(" "));
        mt_tot[d]=map(int,list('0'*(in_m+1)))
        d+=1
    line+=1

#print in_m, in_n
#print in_matdown
#print in_matright
#print mt_tot
#print ''
mt_tot[0][0] = 0

#print mt_tot
#print ''
for i in range(0,in_n):
    mt_tot[i+1][0]=mt_tot[i][0]+in_matdown[i][0]

#print mt_tot
#print ''
for j in range(0,in_m):
    mt_tot[0][j+1]=mt_tot[0][j]+in_matright[0][j]

#print mt_tot
#print ''
for i in range(1,in_n+1):
  for j in range(1,in_m+1):
      sd = mt_tot[i-1][j]+in_matdown[i-1][j]
      sr = mt_tot[i][j-1]+in_matright[i][j-1]
      #print i, j, (i-1), "i" , mt_tot[i-1][j], in_matdown[i-1][j],sd
      #print i, j, (j-1),"j", mt_tot[i][j-1], in_matright[i][j-1], sr
      mt_tot[i][j] = max(sd,sr)
      #print mt_tot
      #print ''
#print mt_tot
print mt_tot[in_n][in_m]
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
