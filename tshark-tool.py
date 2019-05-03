import json
from pprint import pprint
from collections import Counter

# ______________________________________________________________ #

with open("tshark-json", "r") as f:
    tshark_output = json.load(f)

# ______________________________________________________________ #


def capture_summary(x):
    """
    Function to print out the key fields of a capture in a standard
    table format.

    x = python variable of tshark output.
    """
    print("-" * 85)
    for packet in x:
        # Get IP Src value from nested list
        ip_src = packet["_source"]["layers"]["ip.src_host"][0]
        # Get IP Dst value from nested list
        ip_dst = packet["_source"]["layers"]["ip.dst_host"][0]

        """
        Check keys to get TCP or UDP destination port
        This is a little convoluted but seems to work
        """
        for key in packet["_source"]["layers"].keys():
            # Create 2 empty variables and a list
            port_type = ""
            dst_port = ""
            key_list = []
            # Populate the list with all json dict keys
            key_list.append(key)
            if "tcp.dstport" in key_list:
                # if term matches then set variable to tcp
                port_type = "tcp"
                # set variable to destination port depending on key
                dst_port = packet["_source"]["layers"]["tcp.dstport"][0]
            elif "udp.dstport" in key_list:
                # if term matches then set variable to tcp
                port_type = "udp"
                # set variable to destination port depending on key
                dst_port = packet["_source"]["layers"]["udp.dstport"][0]

        # Print formated table of results
        print(
            " {:^20} | {:^20} | {:^20} | {:^20} ".format(
                ip_src, ip_dst, port_type.upper(), dst_port
            )
        )
    print("-" * 85)
    print("")


# ______________________________________________________________ #
"""
Generator to loop through list and create a new src list
"""


def src_createGenerator(x):
    src_list = []
    for src in x:
        src_list = src["_source"]["layers"]["ip.src_host"][0]
        yield src_list


def dst_createGenerator(x):
    dst_list = []
    for dst in x:
        dst_list = dst["_source"]["layers"]["ip.dst_host"][0]
        yield dst_list


# ______________________________________________________________ #

"""
Function to do most common count on list
"""


def most_frequent(x):
    occurence_count = Counter(x)
    return occurence_count.most_common(5)


# ______________________________________________________________ #

top_dsts = {}
top_srcs = {}


def top_talkers():
    """
    Funtion to create two lists of top talkers (src & dst)
    """
    msg1 = "IP:"
    msg2 = "Count:"

    # get top 5 dsts using most_frequent function
    # Store in dict with IP as key and count as value
    # Insertion order will be top first so no need for OrdDict
    for dst in most_frequent(new_dst_list):
        dst_ip = dst[0]
        count = dst[1]
        top_dsts[dst_ip] = count

    # get top 5 Srcs using most_frequent function
    for src in most_frequent(new_src_list):
        src_ip = src[0]
        count = src[1]
        top_srcs[src_ip] = count


def print_top_talkers():
    """
    A function to print a table of table talkers (src & destination)
    """
    src_title = "Top Sources IPs"
    dst_title = "Top Destination IPs"
    src_msg = "SRC IP"
    dst_msg = "DST IP"
    count_msg = "Occurances"

    print("=" * 45)
    print("| {:^41} |".format(src_title))
    print("=" * 45)
    print("| {:^20} {:^20} |".format(src_msg, count_msg))
    for src_ip, src_count in top_srcs.items():
        print("| {:^20} {:^20} |".format(src_ip, src_count))
    print("=" * 45)

    print("\n")
    print("=" * 45)
    print("| {:^41} |".format(dst_title))
    print("=" * 45)
    print("| {:^20} {:^20} |".format(dst_msg, count_msg))
    for dst_ip, dst_count in top_dsts.items():
        print("| {:^20} {:^20} |".format(dst_ip, dst_count))
    print("=" * 45)


# ______________________________________________________________ #


capture_summary(tshark_output)  # Run capture summary function

mysrcgenerator = src_createGenerator(tshark_output)  # create a generator
# Iterate over generator and store list
new_src_list = []
for i in mysrcgenerator:
    new_src_list.append(i)


mydstgenerator = dst_createGenerator(tshark_output)  # create a generator
# Iterate over generator and store list
new_dst_list = []
for i in mydstgenerator:
    new_dst_list.append(i)

# Calling the top talkers function
top_talkers()


# Call top talker print function
print_top_talkers()


# ______________________________________________________________ #

### Personal Notes
##Tshark Command
"""
sudo tshark -i any -n -c 100 -f "ip"  -T fields -e ip.src_host -e ip.dst_host -e tcp.dstport -e udp.dstport -T json
 * -i any = any interface
 * -n = no resolve
 * -c = count
 * -f "ip" = Filter for only IP traffic
 * -T fields = only give the following fields
 * -e = field declartion
 * -T json = Output to json
"""

## Possible issues
"""
 1)
Total amount of occurences in top talkers is not equal to the amount of packets captured. 
I suspect this is due to the ip filter in the tshark command. L2 packets may count towards the 
capture count but be filtered out from the results and thus not stored/analysed by the script

"""

## To Do List
"""
1) Call tshark directly
"""