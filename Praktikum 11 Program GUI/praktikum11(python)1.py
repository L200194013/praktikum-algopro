#Activity 1

from tkinter import Tk, Label, StringVar
from tkinter import LEFT, RIGHT

my_app = Tk(className = 'Data Diri')

L1 = Label(my_app, text = 'Data Diri')
font=('Data Diri_Arial', 30)
L1.grid(row=0, column=0)
L2 = Label(my_app, text = 'Nama          Zanzibar Ahmad Awwalu')
L2.grid(row=1, column=0)
L3 = Label(my_app, text = 'NIM           L200194013')
L3.grid(row=3, column=0)
L4 = Label(my_app, text = 'Buku Favorit  25 Kisah Rasul')
L4.grid(row=4, column=0)
L5 = Label(my_app, text = 'Idola di kalangan sahabat  Abu Bakar Ali')
L5.grid(row=5, column=0)
L6 = Label(my_app, text = 'Motto         Belajar dari kegagalan')
L6.grid(row=6, column=0)

my_app.quit()



