#! usr/bin/python


import nmap

print("Scanning for Hosts in your network..!!!!")

nm = nmap.PortScanner()

nm.scan('192.168.122.0/24', '20-1024')

for host in nm.all_hosts():
    print("-----------------------------------------------------")
    print("Hosts: %s (%s)" %(host, nm[host].hostname()))
    print("State: %s" % nm[host].state())

    for proto in nm[host].all_protocols():
        print("---------------------------------")
        print("Protocol: %s" %proto)

        open_ports = nm[host][proto].keys()
        open_ports.sort()

        for port in open_ports:
            print("port: %s\t state : %s" %(port, nm[host][proto][port]['state']))
