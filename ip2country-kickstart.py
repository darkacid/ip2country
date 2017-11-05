#!/usr/bin/env python3


# Database downloaded from https://db-ip.com/db/ #


from ip2country import ip2country

ipcountry = ip2country("dbip-country-2017-11.csv")
ip = "255.255.255.254"
print(ipcountry.resolve(ip))