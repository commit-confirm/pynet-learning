#Porting over the ipcalc linux utility 
# - Lee Dowdells

ip_prefix = input("Enter your IP Prefix:\t")
octets = ip_prefix.split(". /")
prefix = octets[-1]

#Octet split and print loop:
binary_list = []
for i in octets:
    int_i = int(i)
    int_i = bin(int_i)
    binary_list.append(int_i)

#Formatting octets to 8 bit binary and removing 0b prefix
"""
  [2:] - removes first 2 chars (0b)
  .zfill(8) - pads variable to length 8
"""
b_oct_1 = binary_list[0][2:].zfill(8)
b_oct_2 = binary_list[1][2:].zfill(8)
b_oct_3 = binary_list[2][2:].zfill(8)
b_oct_4 = binary_list[3][2:].zfill(8)


print("-" *90)
print(f"Address:{ip_prefix:^20}{b_oct_1:>16}.{b_oct_2}.{b_oct_3}.{b_oct_4}")
print("-" *90)


## Future Notes: ##
"""
Force command to take x.x.x.x/y format and use the split below to break it down to listed strings.
octets = ip_prefix.replace("/", ".").split(".")
This then allows for 'prefix = octets.pop(-1)' and further work on prefixes

""" 
