import napalm
driver = napalm.get_network_driver("junos")

sw01_re = driver(hostname="172.16.99.10", username="python", password="Pythonenms")
sw02_re = driver(hostname="172.16.99.11", username="python", password="Pythonenms")
sw03_re = driver(hostname="172.16.99.12", username="python", password="Pythonenms")

access_switches = [sw01_re, sw02_re, sw03_re ] 

sw01_re.open()
sw02_re.open()
sw03_re.open()
