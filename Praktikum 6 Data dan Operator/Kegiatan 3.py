Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Zanzibar Ahmad Awwalu'
>>> Nim = 'L200194013'
>>> X = '1' + Nim[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> #because the 'X' data had changed to integer data type
>>> type(b)
<class 'int'>
>>> #because the 'Nama' data has a 'len'intruction
>>> a / b
48.23809523809524
>>> #because the result of 1013 devided by 21 is 48.23809523809524
>>> a // b
48
>>> #because the meaning of '//' is division with rounding down
>>> 10 * (a-999)
140
>>> #because the value of 'a' minus 999 is 10, after that it will multipled
>>> b ** 2
441
>>> #because the value of 'b' square is 441
>>> a % b
5
>>> #because the meaning of '%' is the remainder of the division result
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #because the 'c' data is a float
>>> a / c
81.04
>>> #because the result of 1013 devided by 12.5 is 81.04
>>> a // c
81.0
>>> #because the meaning '//' is division with rounding down
>>> a % c
0.5
>>> #because the meaning of '%' is the reminder of the division result
>>> c > b
False
>>> #because the value of 'c' < value of 'b'
>>> type(c > b)
<class 'bool'>
>>> #because the 'c > b' data had changed to boolean data type
>>> a > b and b > c
True
>>> #because 'a > b' is true and 'b > c' is true
>>> a > 1100 or b < 10
False
>>> #because 'a > 1100' is false or 'b < 10' is false
