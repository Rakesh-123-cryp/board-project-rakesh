import tkinter as tk
import os
from PIL import ImageTk,Image
import time

prg=tk.Tk()
prg.title("Billing Counter")

img=ImageTk.PhotoImage(Image.open("fruits1.jpg"))
bg=tk.Canvas(prg,width=100,height=100)
bg.create_image(20,20,image=img,anchor='nw')

#bg=tk.Canvas(prg,height=500,width=500,bg='maroon')
#bg.pack()

entry=tk.Entry(prg,width=10,bd=5)
entry.pack()
tk.mainloop()
