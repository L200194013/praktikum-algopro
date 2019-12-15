#Activity 3

from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter import Tk, LEFT, RIGHT

my_app = Tk(className = 'Tabel')

L1 = Label(my_app, text = 'Bangun Geomatri', font=('Arial', 17))
L1.grid(row=0, column=0, sticky='W')
L2 = Label(my_app, text = 'Bola merupakan bangun ruang tiga dimensi yang dibentuk oleh tak hingga lingkaran berjari-jari sama panjang dan berpusat pada satu titik yang sama. Bola hanya memiliki 1 sisi.')
L2.grid(row=1, column=0, sticky='W')
L3 = Label(my_app, text = 's1:')
L3.grid(row=2, column=0, sticky='W')
str1 = StringVar()
E3 = Entry(my_app, textvariable=str1)
E3.grid(row=1, column=3, columnspan=2)
L4 = Label(my_app, text = 's2:')
L4.grid(row=3, column=0, sticky='W')
str2 = StringVar()
E4 = Entry(my_app, textvariable=str1)
E4.grid(row=0, column=1, columnspan=3)


def luas():
    'Menghitung luas bola'
    s1 = float (str1.get()):
    s2 = float (str2.get()):
    l = float(4 * 180 * 1/2)
    L = float(l)
    B.config(text='Luas='+L)

B = Button(my_app, text = 'hitung luas', command = luas)
B.grid(row=5, column=0)

my_app.mainloop()




           
