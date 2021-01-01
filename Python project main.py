import tkinter as tk
import PIL
import os

main=tk.Tk()


def changecolour():
       welcome_message.config(text=entry.get())

entry= tk.Entry(main, borderwidth=5)
entry.pack()

background=tk.Canvas(main, height=1000, width=1000, bg='white')
background.pack()

welcome_message=tk.Label(main, text='Welcome to billing process', font=('calibre','20','bold'))
welcome_message.place(x=370,y=350)

Bill_button=tk.Button(main,text='your bill', padx=10, pady=10)
Bill_button.pack()

Bill_button=tk.Button(main,text='change colour', padx=20, pady=10, fg='black', command= changecolour)
Bill_button.place(x=370,y=450)



main.mainloop()
