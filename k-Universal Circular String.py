'''
     Input: An integer k. => 4
     Output: A k-universal circular string. =>     0000110010111101
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

ou_file = open('data_set_out.txt', 'w')

in_binary= 19

last_binary ='1'*in_binary

bin_int = int(last_binary, 2)
print in_binary 
#print bin_int   

in_adjacency = []
for i in range(0,bin_int+1):
    in_adjacency.append(bin(i)[2:].zfill(in_binary))

print len(in_adjacency) 
self= in_adjacency[-1] 
#print in_adjacency
#print ''

res_adjacency = []
res_adjacency.append(in_adjacency[0])
lpos = in_binary-1
last_before = "1"+('0'*lpos)
first = '0'*in_binary
in_adjacency.remove(last_before)
ia = in_adjacency[0]
in_adjacency.remove(ia)
reach = False
ja = ''
etia =''
while(not reach):
    end_ia = ia[1:lpos+1]
    match=True
    while(match):
        #ja = ''
        #etia =''
        match = False
        if (end_ia+"1" in in_adjacency):
            ja = in_adjacency[in_adjacency.index(end_ia+"1")]
            etia = ja[1:lpos+1]
            if (etia+"1" in in_adjacency or etia+"0" in in_adjacency):
                match= True
        if (not match and end_ia+"0" in in_adjacency):
            ja = in_adjacency[in_adjacency.index(end_ia+"0")]
            etia = ja[1:lpos+1]
            if (etia+"0" in in_adjacency or etia+"1" in in_adjacency):
                match= True
        if (match):
            in_adjacency.remove(ja)
            res_adjacency.append(ja)
            if (etia+"1"==self):
                in_adjacency.remove(etia+"1")  
                res_adjacency.append(etia+"1")
            end_ia = etia
        tot_jadj = len(in_adjacency)
        if(tot_jadj==1):
            match=True
            break
    #tot_iadj = len(in_adjacency)
    if(not match):
        k=len(res_adjacency)-1
        #print "k " , res_adjacency[k-1]
        ra_adj=[]
        while(k>=0):
            ra = res_adjacency[k]
            kmatch = False
            lbit = ""
            #print "k " ,k, ra, ra[0:lpos], ktot
            if (ra[0:lpos]+"1" in in_adjacency):
                lbit = "1"
                kmatch = True
            elif(ra[0:lpos]+"0" in in_adjacency):
                lbit = "0"
                kmatch = True
            ra_adj.append(ra)
            if (kmatch):
                #print "kr ", ra_adj
                ia = ra[0:lpos]+lbit
                for rai, rav in enumerate(ra_adj):
                    res_adjacency.remove(rav)
                    in_adjacency.append(rav)
                res_adjacency.append(ia)
                in_adjacency.remove(ia)
                break
            #print "k " ,k, ra, ra[0:lpos], ktot
            k-=1
        #print match
    if(len(in_adjacency)==1):
        reach =True
res_adjacency.append(in_adjacency[0])    
res_adjacency.append(last_before)    
#print len(in_adjacency)
#print in_adjacency
print len(res_adjacency)
ou_res =''
for i,d in enumerate(res_adjacency):
   ou_res+=d[0]

ou_file.write(ou_res + "\n")    
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

