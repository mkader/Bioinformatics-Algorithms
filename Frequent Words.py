'''
     Input: A string Text and an integer k.
             ACGTTGCATGTCGCATGATGCATGAGAGCT
             4
     Output: All most frequent k-mers in Text. => CATG GCAT
'''
import collections   
import datetime

file = open('w1_1_data_set0.txt', 'r')
#file = open('Hidden-Messages-in-the-Replication-Origin-2_Vibrio_cholerae.txt', 'r')

line = 1
kstr = "";
kmer = 12
for ldate in file:
    if (line==1):
        kstr = ldate.strip("\n")
    elif (line==2):	
        kmer = int(ldate)
    line+=1    	

#print kstr, kmer 	
#kstr = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
#kmer = 4

#slower version    
def v1():
    tstart = datetime.datetime.now()
    ou_file = open('v1.txt', 'w')
    #for kmer in range(0,len(kstr)/2):
    for kmer in range(0,100): 
        words = [kstr[i:i+kmer] for i in range(0, len(kstr), 1) if kmer == len(kstr[i:i+kmer]) ] 

        from collections import Counter
        word = Counter(words)
        times = word.values()
        mtimes = max(times)
        tmtimes = times.count(mtimes)
        fwords  = word.most_common(tmtimes)
        #print fwords
        #for fword in fwords:
        #    print fword[0] 
        tend = datetime.datetime.now()        
        #print kmer, str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
        print>>ou_file, kmer, "\t", str(tend-tstart)
    ou_file.close()       

#fast version
def v2():
    #ou_file = open('v2.txt', 'w')
    #tstart = datetime.datetime.now()

    #for kmer in range(0,len(kstr)/2):
    #for kmer in range(0,100):
    #for km in range(0,1):
        count = 0
        words = collections.defaultdict(list)
        mwords=[]
        for i in range(0, len(kstr)-kmer+1):
            word =  kstr[i:i+kmer]
            if len(word)==kmer:
                if word in words:
                    words[word] = words[word]+1
                    if words[word] > count :
                        count = words[word]
                        mwords=[]
                        mwords.append(word)
                    elif words[word] == count:
                        mwords.append(word)
                else:
                    words[word] = 1
        print words
        #print count,
        for w in mwords:
            print w
        #tend = datetime.datetime.now()        
        #print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
        #print>>ou_file, kmer, "\t", str(tend-tstart)
    #ou_file.close()  
#print "v1"
#v1()

#print "v2"
v2()
#print "done"
