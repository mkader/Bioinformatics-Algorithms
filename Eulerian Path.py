'''
     Input: The adjacency list of a directed graph that has an Eulerian path.
             0 -> 2
             1 -> 3
             2 -> 1
             3 -> 0,4
             6 -> 3,7
             7 -> 8
             8 -> 9
             9 -> 6
     Output: An Eulerian path in this graph.
            6->7->8->9->6->3->0->2->1->3->4
     Logic:
            0 -> 
            1 -> 
            2 -> 
            3 -> 0,4
            6 -> 3,7
            7 -> 8
            8 -> 9
            9 -> 6
            0-2-1-3-0
            0-2-1-3-4
            1-3-0-2-1
            1-3-4
            2-1-3-0-2
            2-1-3-4
            3-9-2-1-3-4
            3-4
            6-3-0-2-1-3-4
            6-7-8-9-6-3-0-2-1-3-4
''''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_5_1_data_set7.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_node=[]
#in_bnode={}
rnode=set([])
lnode=set([])
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (len(ldata)==0):
        break
    else:
        ls = ldata.split()
        adj1= ls[0]
        #adj2=ls[1]
        for l,lv in enumerate(ls[2].split(",")):
            in_node.append([adj1,lv])
            rnode.add(adj1)
            lnode.add(lv)
            #print adj1,l,lv
        #in_node[adj1]=ls[2].split(",")
        #in_bnode[adj1]=[False]*(len(ls[2].split(",")))

#print rnode
#print lnode
#print in_node
#print in_bnode
#print ''

def MergeEdge():
    global path
    for i,iv in enumerate(path):
        for j,jv in enumerate(in_node):
            if (iv[1]==jv[0] and iv!=jv):
                tmp=[]
                tmp=list(path[0:i+1])
                if (tmp[0][0]== path[-1][1]):
                    del path[0:i+1]
                    path=path+tmp
                    path.append(jv)
                    in_node.remove(jv)
                    return True
 
    return False        

def PrintPathEdges():
    print>>ou_file, len(path)
    #for j,jv in enumerate(path):
    print>>ou_file, path
    ou_file.write("\n\n") 

def PrintEdges():
    print>>ou_file, len(spath)
    for j,jv in enumerate(spath):
        print>>ou_file, jv
    ou_file.write("\n\n")  

def FindLastEdge():
    for i,nv in enumerate(lnode):
        if(nv not in rnode):
            #print i,nv
            return nv


def MergePathNew():
    #for i,iv in enumerate(spath):
    i=0
    while(len(spath)>1):
        pathmerge=False
        iv=spath[i]
        for ii,iiv in enumerate(iv):
            #print>>ou_file,iiv
            #print>>ou_file, i,iv
            for j,jv in enumerate(spath):
                pathmerge=False
                if(iv!=jv):
                    if(iv[0][0]==jv[-1][1]):
                        #[1630,x1]....[y,1630]..[1630,y]......[x,y]
                        #[y,z] ........ [x2,1630]
##                        print i,"path 00=-11" ,len(spath)
##                        print>>ou_file,"path 00=-11"    
##                        print>>ou_file, iv[0], jv[-1]
##                        print>>ou_file, iv
##                        print>>ou_file, jv
##                        print>>ou_file, jv+iv,"\n"
                        spath[i]=jv+iv
                        #spath.remove(iv)
                        spath.remove(jv)
                        pathmerge=True
                        x=-1
                        #PrintEdges()
                        break    
                    #print>>ou_file, x, y
                    elif(iv[-1][1]==jv[0][0]):
                        #[x,y]....[y,1630]..[1630,y]......[x1,1630]
                        #[1630,x2] ........ [y,z]
##                        print x,"path -11=00" ,len(spath)
##                        print>>ou_file,"path -11=00"    
##                        print>>ou_file, iv[-1], jv[0]
##                        print>>ou_file, iv
##                        print>>ou_file, jv
##                        print>>ou_file, iv+jv,"\n"
                        #spath.append(iv+jv)
                        spath[i]=iv+jv
                        #spath.remove(iv)
                        spath.remove(jv)
                        pathmerge=True
                        x=-1
                        #PrintEdges()
                        break
                    else:
                        for jj,jjv in enumerate(jv):
                            pathmerge=False
                            #print i
                            #print>>ou_file, " " , jjv
                            #if(len(spath)==57):
                            
                                    
                            if(iiv[0]==jjv[1]):
                                #print>>ou_file, iiv,jjv, "rwaR"
                                if(iv[0][0]==iv[-1][1] and
                                   jv[0][0]!=jv[-1][1]):
                                   liv=iv[0:ii]
                                   riv=iv[ii:len(iv)]
                                   spath[i]=jv+riv+liv
                                   spath.remove(jv)
##                                   print>>ou_file,iv
##                                   print>>ou_file,jv
##                                   print>>ou_file,liv
##                                   print>>ou_file,riv
##                                   print>>ou_file,spath[i],"\n"
                                   pathmerge=True
                                   break
                                #   ii+1<len(iv) and iiv[1]==iv[ii+1][0]):
                            elif(iiv[1]==jjv[0]):
                                #if(len(spath)==57):
                                #print>>ou_file, iiv,jjv
                                #print i
                                if(jjv[0]==jv[0][0] and jjv[0]==jv[-1][1] and
                                   ii+1<len(iv) and iiv[1]==iv[ii+1][0]):
                                   #print len(spath) 
                                   #print>>ou_file, i,j, iiv, jjv,iv[ii+1], jv[-1]
                                   liv=iv[0:ii+1]
                                   riv=iv[ii+1:len(iv)]
                                   spath[i]=liv+jv+riv
                                   spath.remove(jv)
                                   #print>>ou_file,jv
                                   #print>>ou_file,spath[i],"\n"
                                   #spath.append(liv+jv+riv)
                                   pathmerge=True
                                   #i=-1
                                   break
                                elif (jv[0][0]==jv[-1][1] and ii+1<len(iv) and iiv[1]==iv[ii+1][0]):
                                   #print len(spath) 
                                   #print>>ou_file, i,j,  jv[0], jv[-1] ,iiv,jjv,iv[ii+1]
                                   ljv=jv[0:jj]
                                   rjv=jv[jj:len(jv)]
                                   njv=rjv+ljv
                                   liv=iv[0:ii+1]
                                   riv=iv[ii+1:len(iv)]
                                   spath[i]=liv+njv+riv
                                   spath.remove(jv)
##                                   print>>ou_file,jv
##                                   print>>ou_file,ljv
##                                   print>>ou_file,rjv
##                                   print>>ou_file,njv
##                                   print>>ou_file,spath[i],"\n"
                                   #spath.append(liv+jv+riv)
                                   pathmerge=True
                                   #i=-1
                                   break
                        if(pathmerge):
                            #i=-1
                            break
            if(pathmerge):
                i=-1
                break
        i+=1
        #if(len(spath)==2):
        #    PrintEdges()
        #    break
        #print i, len(spath)
               
LastEdge = FindLastEdge()
print LastEdge
reach=False
i=in_node[0][1]
path=[]
spath=[]
path.append(in_node[0])
in_node.remove(in_node[0])
while(len(in_node)>0):#not reach):
    #print i
    found=False
    for j,jv in enumerate(in_node):
        if(jv[0]==i):
           path.append(jv)
           in_node.remove(jv)
           i=jv[1]
           #print j, jv
           found=True
           break
    if(not found):
        me=MergeEdge()
        if(me):
            i=path[-1][1]
        else:
            #print "SPath"
            #PrintPathEdges()
            ##break
##            MergePath()
##            reach=False
            spath.append(path)
            i=in_node[0][1]
            path=[]
            path.append(in_node[0])
            in_node.remove(in_node[0])
    if(len(in_node)==0):
        spath.append(path)
        path=[]
        
print "MergePath"
print len(spath),len(path),len(in_node)
if (len(spath)>1):
    #PrintPathEdges()
    #PrintEdges()
    MergePathNew()
    #PrintEdges()
    print len(spath),len(path),len(in_node)

###print path
###print spath
###print in_node
path=list(spath[0])

for j,jv in enumerate(path):
    if (j+1<len(path) and jv[1]!=path[j+1][0]):
        print "check", jv[0],jv[1]

fo =str(path[0][0])+"->"+str(path[0][1])
for j,jv in enumerate(path):
    if(j>0):
        fo+="->"+str(jv[1])
#print fo
ou_file.write(fo +"\n")

tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

