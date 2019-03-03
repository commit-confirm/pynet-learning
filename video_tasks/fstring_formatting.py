from __future__ import print_function, unicode_literals

ip_addr1 = "10.1.1.1" 
port1 = 80
ip_addr2 = "172.16.0.1"
port2 = 443
# String formating before the format method was created, depricated
print(f"iMy IP address is: {ip_addr1:^20} {port1:^2}")
print(f"iMy IP address is: {ip_addr2:^20} {port2:^2}")
