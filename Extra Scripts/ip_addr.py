#!/usr/bin/python3.6
from os import popen

# Get output from ip addr command
ip_addr = popen("ip addr").read()

tracker1, tracker2, tracker3 = (False, False, False)

int_name = []
mac_addr = []

msg1 = "|" 
header1 = "Interface"
header2 = "Mac Address"
header3 = "IP Address"

print("-" *62)
print("{}{:^20}{:^20}{:^20}{}".format(msg1, header1, header2, header3, msg1))
print("=" *62)
#Loop through each line of the output
for line in ip_addr.splitlines():
    #Look for line containing mtu statement
    fields = line.split()
    if "mtu" in line:
        int_name = fields[1].replace(":","")
        #print(int_name)
        tracker1 = True
    #Look for line containing inet statement
    if "link/ether" in line:
        mac_addr = fields[1].upper()
        #print(mac_addr)
        tracker2 = True
        continue
    if "inet " in line:
        ip_addr = fields[1]
        tracker3 = True 
    else:
        tracker2 = False
        continue
    #
    # Triny to print if link is virtual based on mac not being present but not working
    if tracker2 is not tracker1:
        mac_addr = "virtual link"
        #print("virtual link")
    print("{}{:^20}{:^20}{:^20}{}".format(msg1, int_name, mac_addr, ip_addr, msg1))
print("-" *62)

