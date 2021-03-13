import socket
import sys
import time

s = socket.socket()

host = input(str('Entre com o nome do Host:'))
port = 1234
try:
    s.connect((host,port))
    print('Conectado no server')
except:
    print('Coneção com server falhou ')
while 1:
    messagem_enviada = s.recv(1024)
    messagem_enviada = messagem_enviada.decode()
    print('Server:', messagem_enviada)
    mensagem = input(str('Voce:'))
    mensagem = mensagem.encode()
    s.send(mensagem)


