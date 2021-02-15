from sys import argv
import socket

root_server_location = argv[1]
root_server_port = int(argv[2])
top_server_port = int(argv[3])

try:
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created for RS port")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()


def checkCMD(cmd):

    pairs = cmd.split(' ')
    if pairs[2] == "NS":
        return True

    return False


server_addr = (root_server_location, root_server_port)
client_sock.connect(server_addr)
connected = 0

try:
    client_sock_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created for TS port")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

with open("example.txt", 'w') as write_file:
    for line in open("PROJI-HNS.txt", 'r'):
        line = line.strip()


        if line:
            client_sock.sendall(line.encode('utf-8'))
            answer = client_sock.recv(512)
            answer = answer.decode('utf-8')
            if checkCMD(answer):
                temp = answer.split(' ')

                if connected == 0:
                    ts_ip = socket.gethostbyname(temp[0])
                    ts_addr = (ts_ip , top_server_port)
                    client_sock_1.connect(ts_addr)
                    connected = 1

                client_sock_1.sendall(line.encode('utf-8'))
                answer = client_sock_1.recv(512)
                answer = answer.decode('utf-8')

            write_file.write(answer + '\n')
