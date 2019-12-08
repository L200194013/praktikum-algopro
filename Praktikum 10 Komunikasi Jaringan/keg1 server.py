# nama berkas: p_tcpser.py
# TCP Server untuk client p_tcpcli.py
import socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',50001))
s.listen(5)
print ("Server penjawab otomatis sudah siap")
data=''
kamus={'nama':'Zanzibar Ahmad Awwalu',
       'umur':'18',
       'alamat':'Karanganyar, Surakarta',
       'nim':'L200194013',
       'angkatan':'2019',
       'motto':'Ojo kemlinti masio koe pinter elingo kabeh kui gur titipan e Gusti Allah',
       'kuliah':'Informatika UMS',
       'keluar':'Siap Bosku!!!'}
while data.lower() !='q':
    komm, addr = s.accept()
    while data.lower() !='q':
        data = komm.recv(1024)
        if data.() == 'q':
            s.close()
            break
        print 'Pertanyaan:', data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Pertanyaan anda tidak relevan')
        
