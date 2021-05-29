# -*- coding: utf-8 -*-

import socket, re, time

TCP_IP = 'hostnameorip'
TCP_PORT = 9999
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data = re.findall(r'\d+', s.recv(BUFFER_SIZE).decode())

multi = int(data[0]) * int(data[1])
print(multi)
s.send(str(multi).encode())
time.sleep(2)
s.send(str(multi).encode())
data1 = s.recv(BUFFER_SIZE).decode()
print(data1)

s.close()
