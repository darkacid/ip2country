import re
#import netaddr
import csv
#import ipaddress
class ip2country:
    def __init__(self,dbPath):
        self.dbPath = dbPath
    
    def compareIPs(self,firstIP,secondIP):
        '''
        Return true if the first IP is greater than the second
        Return false otherwise.
        '''
        #firstAddr = ipaddress.ip_address(firstIP)
        #secondAddr = ipaddress.ip_address(secondIP)

        #print(firstAddr>secondAddr)
        #return (firstAddr>secondAddr)
        try:

            firstList = firstIP.split(".")
            secondList =secondIP.split(".")
        except ipSplit:
            "Error converting given IPv4 address to list"


        if int(firstList[0]) > int(secondList[0]):

            return True
        else:
            if(int(firstList[0]) != int(secondList[0])):
                return False
        if int(firstList[1]) > int(secondList[1]):

            return True
        else:
            if(int(firstList[1]) != int(secondList[1])):
                return False
        
        if int(firstList[2]) > int(secondList[2]):

            return True

        else:
            if(int(firstList[2]) != int(secondList[2])):
                return False
            
        if int(firstList[3]) > int(secondList[3]):

            return True
        return False


    def resolve(self,ipAddr):
        '''
        Given the ip address returns the country
        '''
        with open(self.dbPath,'r') as dbFile:
            reader = csv.reader(dbFile)
            if(self.compareIPs(ipAddr,"224.0.0.0")):
                return "Unknown"
            for row in reader:
                #1.7 sec
                if (self.compareIPs(ipAddr,row[1])):          
                    continue
                #Execute when Range End >= givenIP


                answer = self.short2long(row[2])
                return (answer)
               # ipRange = netaddr.IPRange(row[0],row[1])             
               # if netaddr.IPAddress(ipAddr) in ipRange:            
               #     answer = self.short2long(row[2])                    
               #     return (answer)
        return "Unknown"

    def short2long(self,shortCountryName):
        '''
        Converts a short country name (two letters) to a long name
        '''
        longDb = open("short-long-db", 'r').read().split('\n')
        countryPattern = "value=\"("+shortCountryName+")\".*>(.*)</option>"
        for line in longDb:
            patternResult = re.search(countryPattern,line)
            if(patternResult):
                patternResult=patternResult.group(2)
                return(patternResult)
