'''
     Input: A collection of k-mers Patterns.
             ATG
             ATG
             TGT
             TGG
             CAT
             GGA
             GAT
             AGA
     Output: All contigs in DeBruijn(Patterns).
             AGA ATG ATG CAT GAT TGGA TGT
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_5_5_data_set3.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 0
in_kmer=[]
bkmer=[]
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (len(ldata)==0):
        break
    else:
        in_kmer.append(ldata)
    line+=1

#print in_kmer
bkmer=[False]*len(in_kmer)
nkmer=[]
pos = len(in_kmer[0])-1
inout=[]
print pos
for i,im in enumerate(in_kmer):
    #print bkmer
    #if(not bkmer[i]):
    sim = im[0:pos]
    eim = im[len(im)-pos:len(im)]
    #print im,sim,eim
    ii = 0
    io = 0
    for j,jm in enumerate(in_kmer):
        #if(not bkmer[j]):
        sjm = jm[0:pos]
        ejm = jm[len(jm)-pos:len(jm)]
        if(sim==sjm):
            ii+=1
        if(sim==ejm):
            io+=1
    #print im,sim,eim  ,ii ,io
    if(ii==1 and io==1):
        inout.append(im)
    else:
        if(not bkmer[i]):
            bkmer[i]=True
            nkmer.append(im)

   
i=0
while(len(inout)>0):
#for i,iv in enumerate(inout):
    #print " i",i
    iv=inout[i]
    #print>>ou_file, iv , iv[pos:len(iv)]
    liv = iv[0:pos]
    for x in nkmer:
        if liv in x:
            #jv=x
            #rjv = jv[len(jv)-pos:len(jv)]
            nkmer.append(x+iv[pos:len(iv)])
            nkmer.remove(x)
            inout.remove(iv)
            i=-1
            break
    i+=1
        
    
#print>>ou_file,"\nTtest\n"    
#print sorted(nkmer)
for i,im in enumerate(sorted(nkmer)):
    #print(im);
    ou_file.write(im+ "\n")

tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

