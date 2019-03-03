#Porting over the ipcalc linux utility 
# - Lee Dowdells

ip_prefix = input("Enter your IP Prefix:\t")
octets = ip_prefix.split(".")

#Octet split and print loop:
binary_list = []
hex_list = []
for i in octets:
    int_i = int(i)
    bin_i = bin(int_i)
    binary_list.append(bin_i)
    hex_i = hex(int_i)
    hex_list.append(hex_i)

#Formatting octets to 8 bit binary and removing 0b prefix
"""
  [2:] - removes first 2 chars (0b)
  .zfill(8) - pads variable to length 8
"""
b_oct_1 = binary_list[0][2:].zfill(8)
b_oct_2 = binary_list[1][2:].zfill(8)
b_oct_3 = binary_list[2][2:].zfill(8)
b_oct_4 = binary_list[3][2:].zfill(8)

h_oct_1 = hex_list[0]
h_oct_2 = hex_list[1]
h_oct_3 = hex_list[2]
h_oct_4 = hex_list[3]

#print(f"Address:{ip_prefix:^20}{b_oct_1:>16}.{b_oct_2}.{b_oct_3}.{b_oct_4}")
print("-" *80)
print(f"{'Octet 1':^20}{'Octet 2':^20}{'Octet 3':^20}{'Octet 4':^20}")
print("-" *80)
print(f"{octets[0]:^20}{octets[1]:^20}{octets[2]:^20}{octets[3]:^20}")
print(f"{b_oct_1:^20}{b_oct_2:^20}{b_oct_3:^20}{b_oct_4:^20}")
print(f"{h_oct_1:^20}{h_oct_2:^20}{h_oct_3:^20}{h_oct_4:^20}")
print("-" *80)


