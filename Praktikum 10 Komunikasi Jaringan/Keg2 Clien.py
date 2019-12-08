import socket
import platform
hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(hostname, 50001)
print 'Mesin penjawab otomatis sudah siap'
while pesan.lower() != 'quit':
    pesan = raw_input('command:')
    s.send(pesan)
    if pesan.lower() == 'quir':
        response = s.recv(1024)
        print ''
    elif pesan.lower() != 'quit':
        response = s.recv(1024)
        print 'Response:', response
s.close()
    
