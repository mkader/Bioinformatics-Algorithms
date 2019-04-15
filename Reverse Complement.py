'''
Given a nucleotide p, we denote its complementary nucleotide as p. The reverse complement of a string Pattern = p1…pn is 
the string Pattern = pn … p1 formed by taking the complement of each nucleotide in Pattern, then reversing the resulting string. 
Reverse Complement Problem: Reverse complement a nucleotide pattern.
     Input: A DNA string Pattern. => AAAACCCGGT
     Output: Pattern, the reverse complement of Pattern. => ACCGGGTTTT
'''
import datetime

in_file = open('w1_2_data_set2.txt', 'r')
ou_file = open('v1.txt', 'w')

line = 1
in_str = ''
for in_data in in_file:
    if (line==1):
    	in_str = in_data.strip(' \t\n\r')
    elif (line==3):
    	res_in_str = in_data.strip(' \t\n\r')
    line+=1

def v1():
    tstart = datetime.datetime.now()
   
    ou_str = ''
    for v in in_str:
        if (v == "A"):
            ou_str+="T"
        elif (v == "T"):
            ou_str+="A"
        elif (v == "G"):
            ou_str+="C"
        elif (v == "C"):
            ou_str+="G"

    ou_str = ou_str[::-1]
    #print ou_str
    ou_file.write(ou_str)    
    tend = datetime.datetime.now()        
    print str(tend-tstart)
                          

def v2():
    tstart = datetime.datetime.now()
    ou_str = in_str
    ou_str = ou_str.replace("A","1")
    ou_str = ou_str.replace("G","2")
    ou_str = ou_str.replace("T","A")
    ou_str = ou_str.replace("1","T")
    ou_str = ou_str.replace("C","G")
    ou_str = ou_str.replace("2","C")
    #print ou_str[::-1]
    ou_file.write(ou_str[::-1])    
    tend = datetime.datetime.now()        
    print str(tend-tstart)
    
#print "v1"
#v1()
#ou_file.write("\n")
print "v2"
v2()
ou_file.close()
print "done"
                
                      

