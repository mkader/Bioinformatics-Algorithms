'''
Let’s follow the 5’ ? 3’ direction of DNA and walk along the chromosome from terC to oriC (along a reverse half-strand) 
and continue on from oriC to terC (along a forward half-strand). In our previous discussion, we saw that the skew is 
decreasing along the reverse half-strand and increasing along the forward half-strand. Thus, the skew should achieve a 
minimum at the position where the reverse half-strand ends and the forward half-strand begins, which is exactly the location of oriC!

We have just developed an insight for a new algorithm for locating oriC: it should be found where the skew attains a minimum:

Minimum Skew Problem: Find a position in a genome minimizing the skew.
     Input: A DNA string Genome. => TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT
     Output: All integer(s) i minimizing Skew(Prefixi (Text)) among all values of i (from 0 to |Genome|). => 11 24
'''

#import collections   

in_file = open('w1_5_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_genome = "";
in_result=""
ou_result =""
for in_data in in_file:
    if (line==1):
    	in_genome = in_data.strip(' \t\n\r')
    elif (line==3):
    	in_result = in_data.strip(' \t\n\r')	
    line+=1    	

#ou_file.write(in_genome+"\n")
#ou_file.write(in_result+"\n")
#print in_genome
print in_result

count_c =0
count_g =0
max_diff = 0
pos_diff = ""
for i,v in enumerate(in_genome):
    if (v=="C"):
        count_c+=1
    elif(v=="G"):    
        count_g+=1
    diff_cg = count_c - count_g
    #skew diagram
    #print v,count_c, count_g, (count_g-count_c)
    if (diff_cg>0 and diff_cg > max_diff):
        pos_diff = str(i+1) + " "
        max_diff = diff_cg
    elif (diff_cg == max_diff):    
        pos_diff += str(i+1) + " "
    #print v,"\t",count_c,"\t", count_g,"\t", diff_cg,"\t", max_diff,"\t", pos_diff
     
ou_result = pos_diff
print ou_result
###if(ou_str==res_in_str):
###    print "yes"
###ou_file.write(ou_result)    
ou_file.close()
