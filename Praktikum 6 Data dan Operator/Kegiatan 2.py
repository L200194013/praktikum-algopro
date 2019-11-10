## Program akun
## Dibuat ole Zanzibar L2001994013
import random
angka = random.randint(0,1000)

Nama = 'Zanzibar Ahmad Awwalu'
print(Nama)
TanggalLahir = '7 Juni 2001'
print(TanggalLahir)
NamaSingkat = Nama[0]+ '. ' + Nama[9] + '. ' + Nama[15:20]
print(NamaSingkat)
Username = Nama[0] + TanggalLahir[0] + TanggalLahir[7:10]
print(Username)
Password = Nama[0:3] + str(angka)
print(Password)
