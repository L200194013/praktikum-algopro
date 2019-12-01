berkas=open('L220194013.txt','w')
berkas.write('L200194013\n')
berkas.write('Surakarta, 07-06-2001\n')
berkas.write('Zanzibar Ahmad Awwalu')
berkas.close()

for line reversed (list(open('L200194013.txt'))):
    print(line.rstrip())
