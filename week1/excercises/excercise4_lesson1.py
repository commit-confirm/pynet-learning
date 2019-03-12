show_cisco_version = ' show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " '
show_juniper_version = "JUNOS Software Release [15.1X49-D110.4]"

print("-" *20)
print(show_cisco_version.strip()) 

cisco_fields = show_cisco_version.split()
cisco_model = cisco_fields[3]
cisco_serial = cisco_fields[4]

vendor_cisco = 'cisco' in cisco_model.lower()
print("Checking if model contains Cisco: {}".format(vendor_cisco))

cisco_model_881 = '881' in cisco_model
print("Checking if mdoel contains 881: {}".format(cisco_model_881))

print("Serial Number {}".format(cisco_serial))
print("Model: {}".format(cisco_model)) 
print()
print("-" *20)

print(show_juniper_version.strip())

juniper_fields = show_juniper_version.split()
juniper_model = juniper_fields[3]

vendor_juniper = 'juniper' in juniper_model.lower()
print("Checking if model contains juniper: {}".format(vendor_juniper))

juniper_model_15 = '15.1' in juniper_model
print("Checking if mdoel contains 15.1: {}".format(juniper_model_15))

print("Model: {}".format(juniper_model))
print()
print("-" *20)

