import tkinter as tk

app = tk.Tk()


frame = tk.Frame(app)
frame.pack()


var1 = tk.StringVar()
Options = ['Hi', 'Hello', 'Gm']

scrollbar = tk.Scrollbar(frame, orient = "vertical")


dd = tk.OptionMenu(frame, var1,value = Options, yscrollcommand = scrollbar.set)

dd.pack()

scrollbar.config(command = dd.yview)
scrollbar.pack(side = "RIGHT", fill = "y")