'''
Generate the theoretical spectrum of a cyclic peptide.
     Input: An amino acid string Peptide. =>      LEQN
     Output: Cyclospectrum(Peptide). => 0 113 114 128 129 227 242 242 257 355 356 370 371 484
     Logic:
         0 	113 	114 	128 	129 	227 	242 	242 	257 	355 	356 	370 	371 	484
         L 	N 	  Q 	  E 	  LN 	  NQ 	  EL 	  QE 	  LNQ 	ELN 	QEL 	NQE 	NQEL
'''

#import collections   
#import itertools
import datetime
#import re

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_2_3_data_set1.txt', 'r')
in_mass = open('w_2_3_integer_mass_table.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 1
in_peptide = "";
in_result=""
ou_result =""
for in_data in in_file:
    if (line==1):
    	in_peptide = in_data.strip(' \t\n\r')
    elif (line==3):
    	in_result = in_data.strip(' \t\n\r')
    line+=1    	

ou_file.write(in_result+"\n\n")
print in_peptide
print in_result
print ""

masss ={}
for in_data in in_mass:
    line = (in_data.strip(' \t\n\r')).split()
    if len(line)==2:
        masss[line[0]]=line[1]
#print masss
#print ""

def Total(mc):
    tot = 0
    for j,p in enumerate(mc):
        tot  += int(masss[p])
    return tot

lin_peptide_n = []
lin_peptide = []

lp = len(in_peptide)
pep_cycli =  in_peptide + in_peptide[:lp-2]
print in_peptide, pep_cycli
lin_peptide =  [pep_cycli[j:j+i+1] for i in range(0,lp-1,1) for j in range(0, lp, 1)]
lin_peptide_n = [Total(i) for i in lin_peptide]
lin_peptide.append(in_peptide)
lin_peptide_n.append(Total(in_peptide))
lin_peptide_n.append(0)

print lin_peptide
print lin_peptide_n   
print sorted(lin_peptide_n)

for j, p in enumerate(sorted(lin_peptide_n)):
    print p,
    #ou_file.write(str(p)+" ")

tend = datetime.datetime.now()        
print
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

#mass table
'''
G 57
A 71
S 87
P 97
V 99
T 101
C 103
I 113
L 113
N 114
D 115
K 128
Q 128
E 129
M 131
H 137
F 147
R 156
Y 163
W 186
'''

#generate mass communication table 
'''
import collections   
import itertools
import datetime
import re

tstart = datetime.datetime.now()
print str(tstart)

in_mass = open('w_2_3_integer_mass_table.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

masss ={}
for in_data in in_mass:
    line = (in_data.strip(' \t\n\r')).split()
    if len(line)==2:
        masss[line[0]]=line[1]
#print masss
#print ""

def Total(mc):
    tot = 0
    for j,p in enumerate(mc):
        tot  += int(masss[p])
    return tot

massline = ''
for j,p in enumerate(masss):
    massline+=p

#print massline

##for i in range(0,len(lin_peptide)):
##    mass_com = map("".join, itertools.product(massline, repeat=i+1))
##    for j,mc in enumerate(mass_com):
##        ou_file.write(mc+"\n")

#not done 6
i= 6
mass_com = map("".join, itertools.product(massline, repeat=i))
for j,mc in enumerate(mass_com):
    ou_file.write(mc+ " "  + str(Total(mc)) +"\n")
    
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()


'''
