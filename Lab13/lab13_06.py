# https://www.tutorialspoint.com/python3/tk_button.htm
# zmodyfikuj program, aby na dole okna pojawiała się informacja, która pobierana jest z pola typu Entry

from tkinter import *

top = Tk()
L1 = Label(top, text = "User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)

top.mainloop()
