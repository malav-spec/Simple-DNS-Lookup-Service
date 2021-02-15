import socket
from sys import argv


DNS_table = {}

def fileToDict():
    f = open("PROJI-DNSTS.txt", "r")
    Lines = f.readlines()

    for line in Lines:
        new_list = []
        line = line.strip()
        pairs = line.split(' ')
        hostname = pairs[0]
        ip_addr = pairs[1]
        cmd = pairs[2]
        new_list.append(ip_addr)
        new_list.append(cmd)
        DNS_table[hostname] = new_list

    f.close()

def checkHostInDict(host):
    if host in DNS_table.keys():
        return True
    else:
        return False

def toString(host):
    hname = host
    ip = str(DNS_table[host][0])
    cmd = str(DNS_table[host][1])
    name = hname+" "+ip+" "+cmd
    return name

def sendErrorMsg(host):
    hname = str(host)
    err = hname + " - Error:HOST NOT FOUND"
    return err



fileToDict()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("[TS]: Socket successfully created")
except socket.error as err:
    print ("[TS]: Socket creation failed with error %s" %(err))

port = int(argv[1])
host = socket.gethostname()
server_binding = ('', port)

try:
    s.bind(server_binding)
    print("[TS]: Socket bind successfull")
except socket.error as err:
    print("[TS]: Socket bind fail with error %s" %(err))

s.listen(1)

csockid, addr = s.accept()
print ("[TS]: Got a connection request from a client at {}".format(addr))

while True:
    data = csockid.recv(1024).decode()
    data = str(data)
    data = data.lower()

    if not data:
        break;

    if checkHostInDict(str(data)) is True:
        
        msg = toString(str(data))
    else:
        msg = sendErrorMsg(str(data))

    csockid.send(msg.encode('utf-8'))

s.close()
