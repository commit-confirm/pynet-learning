
#Variable Declarations:
mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet5"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

#List of variables
mac_list = [mac1, mac2, mac3]

print(f"{'IP Addr':>20}{'MAC Addr':>20}{'Interface':>20}")
print("-" *60)
for mac in mac_list:
    mac = mac.split()
    ip_addr = mac[1]
    mac_addr = mac[3]
    interface = mac[-1]
    print("{:>20}{:>20}{:>20}".format(ip_addr, mac_addr, interface))
