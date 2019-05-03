from netmiko import Netmiko
import getpass
import xmltodict
from pprint import pprint

'''
Messy script to conncet to home lab switchs and check for VLAN 10 as statically defined. 
Plan is to break this up into functions for later.
'''

#Define device parameters (creds are for lab only, so passwords are fine)
left_device = {
    'host': '192.168.0.67',
    'username': 'python',
    'password': 'Python',
#   'password': getpass
    'device_type': 'juniper'
}

right_device = {
    'host': '192.168.0.68',
    'username': 'python',
    'password': 'Python',
#   'password': getpass
    'device_type': 'juniper'
}


left_conn = Netmiko(**left_device)
right_conn = Netmiko(**right_device)

connections = [left_conn, right_conn]

for conn in connections:
    print(conn.host)
    cmd = conn.send_command("show configuration vlans | display xml")
    xml_test = xmltodict.parse(cmd)
    vlan_list = xml_test['rpc-reply']['configuration']['vlans']['vlan']
    '''
    For loop to search through xml rpc response for a vlan ID as defined
    '''
    for item in vlan_list:
        vlan_check = False
        item_num = int(item['vlan-id'])
        if item_num == 10:
            vlan_check = True
            break 
            #print("VLAN ID:", item['vlan-id'], " exists as: ", item['name'], "\n")

    msg_id = "VLAN ID: "
    msg_name = "VLAN Name: "
    item_id = item['vlan-id']
    item_name = item['name']
    msg_none = "VLAN Does Not Exist"
    if vlan_check is True:
        print("-" *40)
        print("{:>20}{:<20}".format(msg_id, item_id))
        print("{:>20}{:<20}".format(msg_name, item_name))
        print("-" *40, "\n")
    elif vlan_check is False:
        print("-" *40)
        print("{:^20}".format(msg_none))
        print("-" *40)


## Known issues
#1) "ExpatError: no element found: line 1, column 0
# This is returned if you run the script in ipython and then run it again, for some reason the third time it works without error.