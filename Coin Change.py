'''
     Input: An integer money and an array coins = (coin1, …, coind).
             40
             50,25,20,10,5,1
     Output: The minimum number of coins with denominations coins that changes money.
              2
    The DPCHANGE pseudocode:
    DPCHANGE(money, coins)
     MinNumCoins(0) ? 0
     for m ? 1 to money
            MinNumCoins(m) ? 8
            for i ? 1 to |coins|
                if m = coini
                    if MinNumCoins(m - coini) + 1 < MinNumCoins(m)
                        MinNumCoins(m) ? MinNumCoins(m - coini) + 1
        output MinNumCoins(money)
'''

import collections   
import itertools
import datetime

tstart = datetime.datetime.now()
print str(tstart)

in_file = open('w_6_1_data_set1.txt', 'r')
ou_file = open('data_set_out.txt', 'w')

line = 0
in_money = 0
in_coins=[]
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if(line==0):
        in_money = int(ldata);
    elif(line==1):
        in_coins = map(int, ldata.split(","));    
    elif (len(ldata)==0):
        break
    line+=1

MinNumCoins={}

MinNumCoins[0] = 0

for m in range(1,in_money+1):
    #print m
    MinNumCoins[m]=float("inf")
    for i, ci in enumerate(in_coins):
        #print m, ci, (m >= int(ci))
        if (m >= ci):
            #print m, ci, m - ci, MinNumCoins[m - ci],(MinNumCoins[m - ci] + 1 < MinNumCoins[m])
            if (MinNumCoins[m - ci] + 1 < MinNumCoins[m]):
                #print m, ci, (MinNumCoins[m - ci] + 1 )
                MinNumCoins[m] = MinNumCoins[m - ci] + 1

print MinNumCoins[in_money]     
#print in_money
#print in_coins

#ou_file.write(fo +"\n")
tend = datetime.datetime.now()        
print str(tstart), " - " , str(tend) , " - ", str(tend-tstart)
print "Done"
ou_file.close()

