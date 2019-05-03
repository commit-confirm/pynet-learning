import json
from pprint import pprint
from collections import Counter

with open("tshark-json", "r") as f:
    tshark_output = json.load(f)

pipe = "|"

print("-" *85)
for item in tshark_output:
    ip_src = item['_source']['layers']['ip.src_host'][0]
    ip_dst = item['_source']['layers']['ip.dst_host'][0]

    '''
    Check keys to get TCP or UDP destination port
    '''
    for key in item['_source']['layers'].keys():
        port_type = ""
        dst_port = ""
        key_list = []
        key_list.append(key)
        if "tcp.dstport" in key_list:
            port_type = "tcp"
            dst_port = item['_source']['layers']['tcp.dstport'][0]
        elif "udp.dstport" in key_list:
            port_type = "udp"
            dst_port = item['_source']['layers']['udp.dstport'][0]
        #print(port_type)

    #print ip src,dst and tcp/udp destination port
    print(" {:^20} | {:^20} | {:^20} | {:^20} ".format(ip_src, ip_dst, port_type.upper(), dst_port))
print("-" *85)
print("")

'''
Generator to loop through list and create a new src list
'''
new_src_list = []

def src_createGenerator(x):
    src_list = []
    for src in x:
        src_list = src['_source']['layers']['ip.src_host'][0]
        yield src_list

mysrcgenerator = src_createGenerator(tshark_output) # create a generator

for i in mysrcgenerator:
    new_src_list.append(i)


'''
Function to do most common count on list
'''
def most_frequent(x):
    occurence_count = Counter(x)
    return occurence_count.most_common(5)

msg1 = "IP:"
msg2 = "Count:"
print(" Source IPs ")
print("| {:^20} | {:^20} |".format(msg1, msg2))
for i in most_frequent(new_src_list):
    src_ip = i[0]
    count = i[1]
    print("| {:^20} | {:^20} |".format( src_ip, count))
print("")
'''
Generator to loop through list and create a new dst list
'''
new_dst_list = []

def dst_createGenerator(x):
    dst_list = []
    for dst in x:
        dst_list = dst['_source']['layers']['ip.dst_host'][0]
        yield dst_list

mydstgenerator = dst_createGenerator(tshark_output) # create a generator

for i in mydstgenerator:
    new_dst_list.append(i)


'''
Function to do most common count on list
'''
def most_frequent(x):
    occurence_count = Counter(x)
    return occurence_count.most_common(5)

msg1 = "IP:"
msg2 = "Count:"
print(" Destination IPs")
print("| {:^20} | {:^20} |".format(msg1, msg2))
for i in most_frequent(new_dst_list):
    dst_ip = i[0]
    count = i[1]
    print("| {:^20} | {:^20} |".format( dst_ip, count))
print("")



### Personal Notes
##Tshark Command
'''
sudo tshark -i any -n -c 100 -f "ip"  -T fields -e ip.src_host -e ip.dst_host -e tcp.dstport -e udp.dstport -T json
 * -i any = any interface
 * -n = no resolve
 * -c = count
 * -f "ip" = Filter for only IP traffic
 * -T fields = only give the following fields
 * -e = field declartion
 * -T json = Output to json
'''
