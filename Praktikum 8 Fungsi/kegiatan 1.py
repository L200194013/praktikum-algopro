x = {'name':'Zanzibar',
     'Nim':'L200194013',
     'address':'Karanganyar',
     'nationality':'Indonesia',
     'religion':'moslem',
     'born':'7 june',
     'year':'2001'}


def Nama():
    print(x['name'])
def Nomor():
    print(x['Nim'])
def Alamat():
    print(x['address'])
def Kewarganegaraan():
    print(x['nationality'])
def Agama():
    print(x['religion'])
def Lahir():
    print(x['born'])
def Tahun():
    print(x['year'])

def pilihan():
    ('''pilihan yang tersedia:
    b. Nomor
    c. Alamat
    d. Kewarganegaraan
    e. Agama
    f. Lahir
    g. Tahun''')

pilihan()
a = input('pilihan anda:')
while a != 'z':
    if a == 'a':
        Nama()
        a = input('pilihan anda:')
    elif a == 'b':
        Nomor()
        a = input('pilihan anda:')
    elif a == 'c':
        Alamat()
    elif a == 'd':
        Kewarganegaraan()
        a = input('pilihan anda:')
    elif a == 'e':
        Agama()
        a = input('pilihan anda:')
    elif a == 'f':
        Lahir()
        a = input('pilihan anda:')
    elif a == 'g':
        Tahun()
        a = input('pilihan anda:')
    elif a == 'z':
        z()
        break
    else:
        print('perintah tidak dikenal')
        a = input('pilihan anda:')
    
    
