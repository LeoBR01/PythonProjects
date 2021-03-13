import socket
import sys
import time

s = socket.socket()

host = socket.gethostname()
print('Server irá iniciar no host:',host)
port = 1234
s.bind((host,port))
print('Server conectado com sucesso')
s.listen(1)
conn,addr = s.accept()
print(addr,'Está conectado')

while 1:
    mensagem = input(str('Voce: '))
    mensagem = mensagem.encode()
    conn.send(mensagem)
    messagem_enviada = conn.recv(1024)
    messagem_enviada = messagem_enviada.decode()
    print('Amigo:', messagem_enviada)


