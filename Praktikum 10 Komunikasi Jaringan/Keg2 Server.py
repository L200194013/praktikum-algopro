import socket
import platform
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 50001))
s.listen(5)
print ('Program komunikasi tentang server')
data = ' '
base = {'machine': platform.machine(),
        'release': platform.release(),
        'system': platform.system(),
        'version': platform.version(),
        'node': platform.node()}
while data.lower() != 'q':
    komm, addr = s.accept()
    while data.lower() != 'q':
        data = komm.recv(1024)
        if data.lower() == 'q':
            s.close()
            break
        print ('command:'), data
        if base.has_key(data):
            komm.send(base[data]):
        else:
            komm.send('unknown command.')

        
