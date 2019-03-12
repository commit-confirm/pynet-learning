from __future__ import print_function, unicode_literals

ip_addr = '192.168.0.1'
octets = ip_addr.split('.')

print("\n")
#print - 80 times
print("-" * 80)
# Take sequence of list elements and print format
print("{:10}{:10}{:10}{:10}".format(*octets))
print("-" * 80)
print("\n")
