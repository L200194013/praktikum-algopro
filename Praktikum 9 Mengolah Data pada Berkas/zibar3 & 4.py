import shelve

F = shelve.open('L200194013.data')
F['nama'] = ['Zanzibar Ahmad Awwalu']
F['nim'] = ['L200194013']
F['ttl'] = ['Surakarta, 07-06-2001']
F.close()

F = shelve.open('L200194013.data')
print('nama:', F['nama'][0])
print('nim:', F['nim'][0])
print('tempat tanggal lahir: ', F['ttl'][0])
F.close()
      
