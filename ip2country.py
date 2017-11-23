import re
import netaddr
import csv

class ip2country:
    def __init__(self,dbPath):
        self.dbPath = dbPath
    
    def compareIPs(self,firstIP,secondIP):
        '''
        Return true if the first IP is greater than the second
        Return false otherwise.
        '''
        firstList = firstIP.split(".")
        secondList =secondIP.split(".")

        if int(firstList[0]) > int(secondList[0]):
            return True
        if int(firstList[1]) > int(secondList[1]):
            return True
        if int(firstList[2]) > int(secondList[2]):
            return True
        if int(firstList[3]) > int(secondList[3]):
            return True
        return False


    def resolve(self,ipAddr):
        '''
        Given the ip address returns the country
        '''
        with open(self.dbPath,'r') as dbFile:
            reader = csv.reader(dbFile)            
            for row in reader:
                if (self.compareIPs(ipAddr,row[1])):                 
                    continue

                if(row[0] == "0.0.0.0"):
                    continue
                if(row[0]=="::"):
                    break
                       
                ipRange = netaddr.IPRange(row[0],row[1])             
                if netaddr.IPAddress(ipAddr) in ipRange:            
                    answer = self.short2long(row[2])
                    print("Range contains : ",ipRange.size)
                    return (answer)
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
