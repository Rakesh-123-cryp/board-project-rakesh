import tkinter as tk


def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


root = tk.Tk()

canvas = tk.Canvas(root, width=950)
canvas.place(x=250, y=100)

frame = tk.Frame(canvas, height=0)

frame.bind("<Configure>", on_configure)

canvas.create_window(0, 0, window=frame)
scrolly = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
scrolly.place(x=20, y=0, relheight=1, anchor="ne")
canvas.configure(yscrollcommand=scrolly.set)


z = 1
q = 35


def click():
    global z, q

    def delete(stuff1_name, stuff1_name1, stuff1_name2):
        stuff1_name.grid_forget()
        stuff1_name1.grid_forget()
        stuff1_name2.grid_forget()

    stuff1_name = tk.Entry(frame, width=57, font=("calibre", 15))
    stuff1_name.grid(row=z, column=0)

    def delete1():
        delete(stuff1_name, stuff1_name1, stuff1_name2)

    stuff1_name1 = tk.Button(frame, font=("calibre", 15))
    stuff1_name1.grid(row=z, column=4)
    if z > 5:
        stuff1_name1.config(command=delete1)
    stuff1_name2 = tk.Entry(frame, width=57, font=("calibre", 15))
    stuff1_name2.grid(row=z, column=1)
    if z <= 3:
        canvas.config(height=q)
    z += 1
    q += 25


but = tk.Button(root, command=click)
but.pack()

"""
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root)


def delete():
    global canvas
    canvas.grid_forget()


but = tk.Button(root, text="click me", command=delete)
but.grid(row=0, column=1)
entry = tk.Entry(root)
entry.grid(row=0, column=2)
"""

root.mainloop()
