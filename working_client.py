import socket
import threading


def read_sok():
    while 1:
        data = sor.recv(1024)
        print(data.decode('utf-8'))


server = 'skopcovs1.fvds.ru', 9090
alias = input("Nickname: ")
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0))

sor.sendto((alias+' connected to server').encode('utf-8'), server)
read_thread = threading.Thread(target=read_sok)
read_thread.start()

while True:
    mensahe = input()
    sor.sendto(('['+alias+'] ' + mensahe).encode('utf-8'), server)
