#!/usr/bin/env python3
from ip2country import ip2country
from time import time
from time import sleep
# Database downloaded from https://db-ip.com/db/ #
ipcountry = ip2country("dbip-country-2017-11.csv")

#ip = "223.255.252.0" 
#without ipaddress 7 sec
#ipaddress optimized to 3 sec


t0 = time()
ip = "10.1.1.1"

#print(ipcountry.resolve(ip))


try :
    ipFile = open ('ipfile',mode='r').read().strip().split('\n')
except:
    print("IP File not present, quitting..")
    quit()
try :
    resolvedFileR = open('resolvedfile',mode='r').read().strip().split('\n')
    resolvedFileA = open('resolvedfile',mode='a')
    #resolvedFile.seek(0)
except:
    print("Resolved File not present, creating..")
    resolvedFileA = open('resolvedfile',mode='a+')
    resolvedFileR = open('resolvedfile',mode='r').read().strip().split('\n')

for ip in ipFile:

    
    if(ip in resolvedFileR):
        print("IP IN RESOLVED FILE")
        print(ip)
    if (ip not in resolvedFileR):
        print("IP NOT IN RESOLVED FILE")
        print (ip)
   
    if (ip not in resolvedFileR):
        result = ip+'\n'
        resolvedFileA.write(result)


t1 = time()
tD = t1-t0
print("Total Execution time: ",tD)
#print(ipcountry.compareIPs("218.22.198.212","218.30.62.255"))
#sleep(5)
