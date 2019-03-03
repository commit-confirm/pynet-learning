from __future__ import print_function, unicode_literals

ip_addr1 = "10.1.1.1" 
ip_addr2 = "172.16.0.1"
ip_addr3 = "192.168.0.1"

print("\n")
#print - 80 times
print("-" * 80)
#make each field a column of 26(80/3) wide with middle alignment
#using named arguements ipn=ip_addrn
print("{ip1:^26}{ip2:^26}{ip3:^26}".format(ip1=ip_addr1, ip2=ip_addr2, ip3=ip_addr3))
print("-" * 80)
print("\n")
