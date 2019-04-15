'''
Input: 0 113 128 186 241 299 314 427
Output: 186-128-113 186-113-128 128-186-113 128-113-186 113-186-128 113-128-186
Pseudocode: 
    CYCLOPEPTIDESEQUENCING(Spectrum)
        List ? {0-peptide}
        while List is nonempty
            List ? Expand(List)
            for each peptide Peptide in List
                if Cyclospectrum(Peptide) = Spectrum
                    output Peptide
                    remove Peptide from List
                else if Peptide is not consistent with Spectrum
                    remove Peptide from List
'''

import collections   
import itertools
import datetime
import re

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_2_4_data_set1.txt', 'r')
in_mass = open('w_2_3_integer_mass_table.txt', 'r')
ou_file = open('data_set_out0.txt', 'w')

line = 1
in_spectrum = "";
in_result=""
ou_result =""
for in_data in in_file:
    if (line==1):
    	in_spectrum = in_data.strip(' \t\n\r')
    elif (line==3):
    	in_result = in_data.strip(' \t\n\r')
    line+=1    	

ou_file.write(in_result+"\n\n")
ou_file.write(in_spectrum+"\n\n")
#print in_spectrum
#print in_result
print ""

masss ={}
for in_data in in_mass:
    line = (in_data.strip(' \t\n\r')).split()
    if len(line)==2:
        masss[line[0]]=line[1]

masss_value = masss.values()     
#print masss
#print masss_value
#print ""

#convert mass letter to number and "-" each letter between
#IKW 113-128-186
def Total(mc):
    tot = ''
    for j,p in enumerate(mc):
        tot  += masss[p]+ '-'
    return tot[:len(tot)-1]

#check the value and return mass key
def MassKey(p):
    for k, v in masss.items():
        #print k,v,p
        if(v==p):
            return k
        
#sum of mass number
def Sum(mc):
    tot = 0
    for j,p in enumerate(mc):
        tot  += int(masss[p])
    return tot

in_spectrum_a = (in_spectrum.strip(' \t\n\r')).split()
in_spectrum_s = ''

#print "a " ,in_spectrum_a

#Get all the >0 value of spectrum
#113 2 I, 128 2 K, 186 1 W = >IKW

for j,p in enumerate(in_spectrum_a):
    #print j,p, masss_value.count(p), MassKey(p)
    if (masss_value.count(p)>0):
         in_spectrum_s+=MassKey(p)

print in_spectrum_s
#same mass key may be repeated, so assign each "in_spectrum_s" one letter
#{'a': 'I', 'c': 'W', 'b': 'K'}         
dic_spe={}
for i,p in enumerate(list(map(chr, range(97, 97+len(in_spectrum_s))))):
    #print p, in_spectrum_s[i]
    dic_spe[p]=in_spectrum_s[i]

#convert assigned value to mass value
#IKW abc, IWK acb
def DictValue(pq):
    dpq = ''
    for j,p in enumerate(pq):
        dpq  += dic_spe[p]
    return dpq

#Check sum of "I","IW", "IKW" mass in input spectrum
def Split(p):
    pp = p
    for i in range(0, len(pp)-1):
        mc = pp[i:i+len(p)-1]
        #print "   ", i, mc, Sum(mc), str(Sum(mc)) in in_spectrum_a
        if (not str(Sum(mc)) in in_spectrum_a):
            return False
    return True       


#print "dic " ,dic_spe
#print in_spectrum_s

#generate
#['a', 'b', 'c'] => ['ac', 'ab', 'ca', 'cb', 'ba', 'bc']
# => ['acb', 'abc', 'cab', 'cba', 'bac', 'bca']
#Check sum of "I","IW", "IKW" mass in input spectrum
ou_spectrum_s = list(dic_spe.keys())
in_spectrum_d = list(dic_spe.keys())
print ou_spectrum_s, in_spectrum_d
#for k in range(0,3):
for k in range(0,len(in_spectrum_s)-1):
    #ou_spectrum_s = list(in_spectrum_s)
    tmp =[]
    for i,p in enumerate(ou_spectrum_s):
        for j,q in enumerate(in_spectrum_d):
            #print p, q,p.find(q)
            if(p.find(q)<0):
                dp = DictValue(p)
                dq = DictValue(q)
                #print " " ,dp,dq, Split(dp+dq), Sum(dp+dq), str(Sum(dp+dq)) in in_spectrum_a
                if(Split(dp+dq) and str(Sum(dp+dq)) in in_spectrum_a ):
                    tmp.append(p+q)
    ou_spectrum_s =list(tmp)
    #print ou_spectrum_s

#print     ou_spectrum_s
#convert assinged letter to mass letter
uou_spectrum_s = []
for j, p in enumerate(sorted(ou_spectrum_s)):
    pd =DictValue(p)
    #print pd, p
    if(not pd in uou_spectrum_s):
        uou_spectrum_s.append(pd)

#convert mass letter to number and "-" each letter between
#IKW 113-128-186, IWK 113-186-128, KIW 128-113-186, KWI 128-186-113
#print uou_spectrum_s
for j, pd in enumerate(sorted(uou_spectrum_s)):
    #ou_file.write(pd + "  " + Total(pd)+" \n")
    #ou_file.write(Total(pd)+" ")
    print pd, Total(pd)

tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

