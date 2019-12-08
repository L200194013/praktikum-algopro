# nama berkas: p_tcpli.py
# TCP Server untuk client p_tcpcli.py
import socket

hostname = 'localhost'
pesan = ' '
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50001))
print ('Mesin Penjawab otomatis sudah siap')
while pesan.lower() != 'q':
    pesan = raw_input('Pernyataan: ')
    s.send(pesan)
    if pesan.lower() != 'q' :
        response = s.recv(1024)
        print ('Jawaban:', response)
s.close
