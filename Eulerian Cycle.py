'''
     Input: The adjacency list of an Eulerian directed graph.
             0 -> 3
             1 -> 0
             2 -> 1,6
             3 -> 2
             4 -> 2
             5 -> 4
             6 -> 5,8
             7 -> 9
             8 -> 7
             9 -> 6
     Output: An Eulerian cycle in this graph.
            6->8->7->9->6->5->4->2->1->0->3->2->6
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_4_5_data_set4.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_adjacency=[]
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (len(ldata)==0):
        break
    else:
        ls = ldata.split()
        adj1= ls[0]
        adj2=ls[1]
        for i,e in enumerate(ls[2].split(",")):
            in_adjacency.append(adj1 + " " + e)
 
#print in_adjacency
i=0            
tot_iadj = len(in_adjacency)            
while (i<tot_iadj):
    ia = in_adjacency[i]
    ias = ia.split()
    end_ias =  ias[-1]
    tot_jadj = len(in_adjacency)
    j=0
    #print "I ", ias, end_ias #i,,j,tot_jadj
    match = False
    while (j<tot_jadj):
        ja = in_adjacency[j]
        sta_jas = (ja.split())[0]
        if (end_ias==sta_jas and ja != ia):
            #print "J ", ja, " - " , end_ias #,sta_jas, j
            match= True
            ia = ia +  ja[len(sta_jas):]
            in_adjacency[i]= ia
            #ias = ja.split()
            #end_ias =  ias[len(ias)-1]
            end_ias = (ja.split())[-1]
            #print "K    ",ia, " - " , end_ias
            in_adjacency.remove(ja)
            tot_jadj-=1
            j=-1
           # print in_adjacency
        j+=1
    #if (match):
        #i=-1
    tot_iadj = len(in_adjacency)
    #print in_adjacency
    i+=1

###print in_adjacency
#for i,d in enumerate(in_adjacency):
###    print d.find("0")
##    #ias = in_adjacency.split()
#    ou_file.write(d + "\n")
##
###ou_file.write("\n\n\n")
##   
i=0            
tot_iadj = len(in_adjacency)            
while (i<tot_iadj):
    ia = in_adjacency[i]
    ias = ia.split()
    end_ias =  ias[len(ias)-1]
    tot_jadj = len(in_adjacency)
    j=0
    #print i, ias, end_ias, tot_jadj, j
    match = False
    while (j<tot_jadj):
        ja = in_adjacency[j]
        jas = in_adjacency[j].split()
        if ((end_ias in jas) and ja != ia):
            #print "1 ", end_ias ,' - ' , jas ,' - ' , ia
            #ou_file.write(" 1 "+end_ias + ' - ' + jas + ' - ' + ia +"\n") 
            ljas = jas[jas.index(end_ias)+1:]
            rjas = jas[1:jas.index(end_ias)+1]
            njas= ljas + rjas
            #print "2 ", rjas, ljas, ' '.join(njas)
            match= True
            ia = ia +' '+  ' '.join(njas)
            #ou_file.write(ia + "\n")
            #ou_file.write(" 2 "+rjas + ' - ' + ljas + '  ' + ia +"\n")
            in_adjacency[i]= ia
            ias = ja.split()
            end_ias =  ias[len(ias)-1]
            in_adjacency.remove(ja)
            tot_jadj-=1
            j=-1
            #print in_adjacency
            #print " "
        j+=1
    if (match):
        i=-1
        tot_iadj = len(in_adjacency)
    #print i,in_adjacency
    i+=1
##
###ou_file.write("\n\n")    
###print in_adjacency
#for i,d in enumerate(in_adjacency):
###    print d.find("0")
##    #ias = in_adjacency.split()
##    ou_file.write(d + "\n")
##
###ou_file.write("\n\n")
##
##    
#print len(in_adjacency)
i=0            
tot_iadj = len(in_adjacency)            
while (i<tot_iadj):
    ia = in_adjacency[i]
    ias = ia.split()
    end_ias =  ias[0]
    tot_jadj = len(in_adjacency)
    j=0
    #print i, ias, end_ias, tot_jadj, j
    #print "I =",i , end_ias ,tot_jadj
    match = False
    while (j<tot_jadj):
        ja = in_adjacency[j]
        jas = in_adjacency[j].split()
        if ((end_ias in jas) and ja != ia):
            #print "1TEST ", end_ias ,' - ' , jas ,' - ' , ia
            #ou_file.write(" 1 "+end_ias + ' - ' + jas + ' - ' + ia +"\n") 
            if (jas[0]==jas[len(jas)-1]):
                ljas = jas[jas.index(end_ias)+1:]
                rjas = jas[1:jas.index(end_ias)]
            else:
                ljas = jas[jas.index(end_ias)+1:]
                rjas = jas[0:jas.index(end_ias)]
            njas= ljas + rjas
            #print "2TEST ", rjas, ljas, ' '.join(njas)
            match= True
            ia = ' '.join(njas) + ' '+ ia
            ##ou_file.write(" 2 "+rjas + ' - ' + ljas + '  ' + ia +"\n")
            in_adjacency[i]= ia
            ias = ja.split()
            end_ias =  ias[0]
            in_adjacency.remove(ja)
            tot_jadj-=1
            j=-1
            #print len(in_adjacency)
            #print " "
        j+=1
    if (match):
        i=-1
        tot_iadj = len(in_adjacency)
    #print i,in_adjacency
    i+=1

#print len(in_adjacency)
i=0            
tot_iadj = len(in_adjacency)            
while (i<tot_iadj):
    ia = in_adjacency[i]
    ias = ia.split()
    for f, n in enumerate(ia.split()):
        end_ias =  n
        tot_jadj = len(in_adjacency)
        j=0
        #print i, ias, end_ias, tot_jadj, j
        #print "I =",i , end_ias,' -' ,ia
        match = False
        while (j<tot_jadj):
            ja = in_adjacency[j]
            jas = in_adjacency[j].split()
            if ((end_ias in jas) and ja != ia):
                #print "1TEST ", jas
                if (ias[0]==ias[len(ias)-1]):
                    lias = ias[ias.index(end_ias):]
                    rias = ias[1:ias.index(end_ias)]
                else:
                    lias = ias[ias.index(end_ias):]
                    rias = ias[0:ias.index(end_ias)]
                nias= lias + rias
                #print "2TEST ", rias, lias, ' '.join(nias)
                match= True
                ljas = jas[jas.index(end_ias):]
                rjas = jas[0:jas.index(end_ias)]
                #print "3TEST ", rjas, ljas
                njas = ' '.join(rjas) + ' '+ ' '.join(nias) + ' ' + ' '.join(ljas)
                #print "4TEST ", njas
                in_adjacency[j]= njas
                in_adjacency.remove(ia)
                #print len(in_adjacency)
                break
            j+=1
        if (match):
          i=-1
          tot_iadj = len(in_adjacency)
          break
    #print i,in_adjacency
    i+=1
#print   in_adjacency
#for i,d in enumerate(in_adjacency):
    #print d.find("0")
#    ou_file.write(d +"\n")

fo =''
for i,d in enumerate(in_adjacency[0].split()):
    fo+= d + '->'
#fo+=(in_adjacency[0].split())[0]
#print fo
ou_file.write(fo +"\n")
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

