Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Zanzibar Ahmad Awwalu'
>>> Nim = 1013
>>> Tinggi = 1.70
>>> Berat = 75
>>> TahunLahir = 2001
>>> Aku =(TahunLahir, Berat, Tinggi, Nim, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, Nim, Nama]
>>> type(Aku)
<class 'tuple'>
>>> #because the 'aku' data is written in perentheses
>>> Aku[0]
2001
>>> #because the first object in 'Aku' data is 'TahunLahir', the value of 'TahunLahir' is 2001
>>> a = Nim % 4 ; Aku[a]
75
>>> #because the remaining result of 1013 devided by 4 is 1, so the result of Aku[1] is 75
>>> type(Aku[a])
<class 'int'>
>>> #because the value of 'Berat' is 1, 1 is an integer data type
>>> Aku[a:4]
(75, 1.7, 1013)
>>> #because the object in 'Aku' start from 'Berat, Tinggi, Nim, Nama'
>>> type(Aku[4])
<class 'str'>
>>> #because the 'Aku[4]' data is string
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #because 'Aku' data type is tuple, so can't changed with another data
>>> type(Data[4])
<class 'str'>
>>> #because the value of 'Data[4]' data is string
>>> type(Data)
<class 'list'>
>>> #because the 'Data' data is written in brackets
>>> Data[4][5]
'b'
>>> #because 'Data[4][5]' is 'b'
>>> Data [4][a:6]
'anzib'
>>> #because in value 'Data[4]' object in the value start from 'a' until '5' is 'anzib'
>>> Data[0] = 'ok';Data
['ok', 75, 1.7, 1013, 'Zanzibar Ahmad Awwalu']
>>> #because the first object has changed by 'ok', and it call all list in 'Data'
>>> Data[-1]
'Zanzibar Ahmad Awwalu'
>>> #because it is call from rear list
>>> range(1)
range(0, 1)
>>> #because range of 1 is (0,1)
