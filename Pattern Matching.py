'''
Find all occurrences of a pattern in a string.
     Input: Two strings, Pattern and Genome.
               ATAT
               GATATATGCATATACTT
     Output: All starting positions where Pattern appears as a substring of Genome.
              1 3 9
'''

in_file = open('w1_3_data_set0.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_Pattern = ''
in_Genome = ''
in_Result = '';
for in_data in in_file:
    if (line==1):
    	in_Pattern = in_data.strip(' \t\n\r')
    elif (line==2):
    	in_Genome = in_data.strip(' \t\n\r')	
    elif (line==4):
    	in_Result = in_data.strip(' \t\n\r')
    line+=1

ou_str = ""
for n in xrange(len(in_Genome)):
    #print n
    if (in_Genome.find(in_Pattern, n) == n):
        #print n, in_Genome.find(in_Pattern, n)
        ou_str+=str(n) + ' ' 
    
print in_Pattern
print in_Genome
print in_Result
print ou_str
#if(ou_str==res_in_str):
#    print "yes"
ou_file.write(ou_str)    
ou_file.close()
