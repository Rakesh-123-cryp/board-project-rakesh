import tkinter as tk
from prettytable import PrettyTable
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector as mysql

# import opencv
# import pyzbar

# importing all data from sql tables

ms = mysql.connect(
    host="localhost", user="root", passwd="22072003Rraki", database="grocery_list"
)
cursor = ms.cursor()


# Chaning Background code

main = tk.Tk()
main.state("zoomed")
main.title("Super Market")
main.iconbitmap(r"bucket-clipart-fruit-15.ico")
c = 0


def bg():
    global c
    global bg1
    global img
    limg = [
        r"fruits1.jpg",
        r"fruits4.jpg",
        r"fruits5.jpg",
        r"fruits7.jpg",
        r"fruits8.jpg",
        r"fruits9.jpg",
    ]
    img = ImageTk.PhotoImage(Image.open(limg[c % 6]))
    bg1.configure(image=img)
    bg1.pack()
    main.after(5000, bg)
    c += 1


main.after(10, bg)
img = ImageTk.PhotoImage(Image.open(r"fruits1.jpg"))
bg1 = tk.Label(main, image=img, highlightthickness=0)
bg1.pack()

# ---------#---------#---------#---------#

# Heading Company Name

# ---------#---------#---------#---------#

# Enter Title, S.No and Name to Search for the item
title_img = tk.PhotoImage(file="TitleBgName.png")
title_label = tk.Label(main, image=title_img)
title_label.place(x=222.5, y=0)
s_no = tk.Entry(main, width=20, font="large_font")
s_no.place(x=15 + 30, y=150)
name = tk.Entry(main, width=75, font="large_font")
name.place(x=230 + 35, y=150)
s_no_text = tk.Label(main, text="S.No", font=("calibre", 10, "bold"), height=1)
s_no_text.place(x=0 + 10, y=150.35)
s_no_text = tk.Label(main, text="Name", font=("calibre", 10, "bold"), height=1)
s_no_text.place(x=222.5, y=150.35)


def name_focus(event):
    name.focus()


def s_no_focus(event):
    s_no.focus()


s_no.bind("<Right>", name_focus)
name.bind("<Left>", s_no_focus)

# ---------#---------#---------#---------#

# Total Box
tt = 0
total_box = tk.Canvas(main, height=173, bd=0, highlightthickness=0, width=429)
total_box.place(x=945, y=0)
total_l = tk.Label(main, text="₹" + str(tt), fg="red", font=("calibre", 75))
total_l.place(x=1000, y=30)

# ---------#---------#---------#---------#

# evrything to do with the list of items

ordinate = 27
o = 27
c1 = 0
l = []
l_nolist = []
l_qty = []

list_items = tk.Canvas(main, width=0, height=0, highlightthickness=0)
list_items.place(x=10, y=250)


def on_config(event):
    list_items.configure(scrollregion=list_items.bbox("all"))


main_frame = tk.Frame(list_items, height=0)
main_frame.bind("<Configure>", on_config)
list_items.create_window(0, 0, window=main_frame)
bar = tk.Scrollbar(main, orient="vertical", command=list_items.yview)
bar.place(x=800, y=50, relheight=1, anchor="ne")
list_items.configure(yscrollcommand=bar.set)

DOUBLE = 0


def rows(event):
    global tt, total_l, DOUBLE
    global t
    if s_no.get() != "":
        num = s_no.get()  # mysql fetch vraiable for sno
        all_details = cursor.execute("select * from items where s_no=" + num)
        data = cursor.fetchall()

    elif name.get() != "":
        name_initial = name_list.curselection()[0]  # mysql fetch vraiable for name
        name_final = name_list.get(name_initial)
        all_details = cursor.execute(
            "select * from items where name='" + name_final + "'"
        )
        data = cursor.fetchall()
        name_list.destroy()
        rate_list.destroy()

    elif data_state:
        all_details = cursor.execute(
            "select * from items where s_no=" + data_req.decode("utf-8")[0][-1:-6]
        )
        data = cursor.fetchall()
        data.pop(-1)

    global ordinate
    global o
    global c1
    global l_nolist
    if (
        s_no.get() > str(25000)
        and s_no.get() < str(25101)
        and int(s_no.get()) not in l_nolist
    ) or (name.get() != ""):

        name.delete(0, "end")
        n = ordinate
        l.append(data[0])
        fake = []

        for no in l:
            fake.append(no[0])
        l_nolist = fake
        fake = []
        s_no.delete(0, "end")

        stuff1_sno = tk.Entry(main_frame, width=30, font=("calibre", 15))
        stuff1_sno.insert(0, data[0][0])
        stuff1_sno.config(state="disabled")
        stuff1_sno.grid(row=DOUBLE, column=0)
        stuff1_name = tk.Entry(main_frame, font=("calibre", 15))
        stuff1_name.insert(0, data[0][1])
        stuff1_name.config(state="disabled")
        stuff1_name.grid(row=DOUBLE, column=1)
        stuff1_rate = tk.Entry(main_frame, font=("calibre", 15))
        stuff1_rate.insert(0, data[0][2])
        stuff1_rate.config(state="disabled")
        stuff1_rate.grid(row=DOUBLE, column=2)
        if len(l) <= 3:
            list_items.config(width=950, height=ordinate)
            main_frame.config(height=ordinate)

        def quantity(event):
            global main_frame

            global tt
            s_no.focus()

            def total(stuff1_sno, stuff1_name, stuff1_rate, stuff1_qty, stuff1_price):
                global tt
                global ordinate
                times = 0
                DOUBLE = 0
                # place_forget
                if c1 <= 7:
                    h = list_items.winfo_height()
                    # print(h)
                for bleh in l:
                    if str(stuff1_sno.get()) == str(bleh[0]):
                        l.remove(bleh)
                        l_qty.remove(float(stuff1_qty.get()))
                quan = stuff1_qty.get()
                pri = stuff1_price.get()
                tt -= float(pri[1:])
                print(l)
                ordinate = len(l) * 27
                print(ordinate)
                list_items.config(height=ordinate)
                total_l.config(text="₹" + str(tt))
                stuff1_sno.grid_forget()
                stuff1_name.grid_forget()
                stuff1_rate.grid_forget()
                stuff1_qty.grid_forget()
                stuff1_price.grid_forget()
                dlt.grid_forget()
                DOUBLE -= 1

            if stuff1_qty.get() == "":
                messagebox.showerror("QTY Error", "Please enter a quantity")
                stuff1_qty.focus()

            else:
                if stuff1_qty.get().isalpha():
                    messagebox.showerror("QTY Error", "Please enter a valid number")
                    stuff1_qty.focus()
                print(l)
                l_qty.append(float(stuff1_qty.get()))
                l[-1] += (stuff1_qty.get(),)
                print(l)

                def twofns():
                    total(
                        stuff1_sno, stuff1_name, stuff1_rate, stuff1_qty, stuff1_price
                    )

                stuff1_qty.config(state="disabled")
                stuff1_price.config(state="normal")
                stuff1_price.insert(
                    0, "₹" + str(int(data[0][2]) * float(stuff1_qty.get()))
                )
                total_l.config(
                    text="₹" + str(tt + int(data[0][2]) * float(stuff1_qty.get()))
                )
                stuff1_price.config(state="disabled")
                tt += int(data[0][2]) * float(stuff1_qty.get())
                dlt.config(command=twofns)
                # place(x=598+290,y=ordinate-24.75-27)

        stuff1_qty = tk.Entry(main_frame, width=10, font=("calibre", 15))
        stuff1_qty.focus()
        stuff1_qty.grid(row=DOUBLE, column=3)
        # place(x=378+264,y=ordinate-27)
        stuff1_qty.bind("<Return>", quantity)
        stuff1_price = tk.Entry(main_frame, font=("calibre", 15), state="disabled")
        stuff1_price.config(state="disabled")
        stuff1_price.grid(row=DOUBLE, column=4)
        dlt = tk.Button(main_frame, width=2, height=1, highlightthickness=0)
        dlt.grid(row=DOUBLE, column=5)
        DOUBLE += 1
        print(DOUBLE)
        # place(x=378+220+154,y=ordinate-27)

        def double(event):
            stuff1_qty.config(state="normal", bg="sky blue")
            stuff1_qty.focus()

        ordinate += 27
        o += 27
        c1 += 1

    else:
        messagebox.showerror("Name error", "Please check the serial number entered")
        s_no.delete(0, "end")


s_no.bind("<Return>", rows)

# search by name

l1 = [""]
space = 25
e1 = 0
double = 0
e2 = 0


def name_search(event):  # main function for searching by name
    global down
    global e2
    down = 0
    # print('whatup')
    global name_list
    global rate_list
    DOUBLE = 1
    global n_s
    n_s = name.get()
    cursor.execute("select * from items where name like '" + str(n_s) + "%'")
    data_name_search = cursor.fetchall()
    data_name_search = sorted(data_name_search, key=lambda x: x[1])
    l1.append(name.get())
    """if len(name.get())==2:
        print(n_s)
        n_s=n_s[0:-2]
        print(n_s)"""
    if (
        name.get() != "" and len(name.get()) == 1 and "" in l1
    ):  # creating the listbox at the start of search

        name_list = tk.Listbox(
            main,
            bg="white",
            height=len(data_name_search) * 1,
            width=50,
            font=("calibre", 13, "bold"),
            highlightthickness=0,
        )
        name_list.place(x=266, y=172)
        rate_list = tk.Listbox(
            main,
            bg="white",
            height=len(data_name_search) * 1,
            width=10,
            font=("calibre", 13, "bold"),
            highlightthickness=0,
        )
        rate_list.place(x=718, y=172)

        def double_change(event):
            global e2
            global double
            double = 0

        name_list.bind("<Return>", rows)
        for stuff in data_name_search:
            name_list.insert("end", stuff[1])
            rate_list.insert("end", stuff[2])
        double = 1
        l1.clear()

    elif (name.get() != "" and len(name.get()) > 1 and "" not in l1) or (
        e2 == 1
    ):  # continuing listbox data display
        l1.append(name.get())
        name_list.delete(0, "end")
        rate_list.delete(0, "end")
        name_list.config(height=len(data_name_search) * 1)
        rate_list.config(height=len(data_name_search) * 1)
        for stuff in data_name_search:
            name_list.insert("end", stuff[1])
            rate_list.insert("end", stuff[2])
        l1.clear()
        e2 = 0

    def binding(event):
        selection = name_list.curselection()
        t = name_list.get(selection[0])
        return t

    def godown(event):
        global down
        name_list.selection_set(down)
        name_list.activate(down)
        down += 1
        name_list.focus()

    def backspace(event):
        global e2
        if len(name.get()) == 2:
            e2 = 1
        if len(name.get()) == 1:
            name_list.destroy()
            rate_list.destroy()

    name.bind("<Down>", godown)  # binding key to name
    name.bind("<BackSpace>", backspace)
    # name.bind('<>',act)
    return DOUBLE

    if len(data_name_search) == 0:  # if wrongly typed
        messagebox.showerror("Name Error", "Please check your Entry")
        name.delete(0, "end")


name.bind("<KeyRelease>", name_search)

# MEMBERSHIP


def member():
    # bill()
    def checking(data_member):

        list_of_users = []
        list_of_no = []
        for i in data_member:
            list_of_users.append(i[0])
            list_of_no.append(i[1])
        print(list_of_users, list_of_no)

        if (
            entry_member_name.get() in list_of_users
            or entry_member_no.get() in list_of_no
        ):
            print("t")
            if entry_member_name.get() == "":
                print("y")
                for p in data_member:
                    if p[1] == entry_member_no.get():
                        user_Name = p[0]
                        entry_member_name.insert(0, p[0])
                        entry_member_name.config(state="disabled")
            else:
                print("yy", total_p2.cget("text"))
                for p in data_member:
                    if p[0] == entry_member_name.get():
                        user_No = p[1]
                        entry_member_no.insert(0, user_No)
                        entry_member_no.config(state="disabled")

            def discount_total():
                print(total_p2)
                ttt = float(total_l.cget("text")[1:])
                print(data_member)
                if ttt > 1500 and float(data_member[0][2]) > 0:
                    ttt -= (float(data_member[0][2] / 100)) * ttt
                    print(ttt)
                    cursor.execute(
                        "update users set discount=discount+0.7 where mobile_number='"
                        + data_member[0][1]
                        + "'"
                    )
                    ms.commit()
                elif ttt > 1000 and ttt <= 1500 and float(data_member[0][2]) > 0:
                    ttt -= (float(data_member[0][2] / 100)) * ttt
                    print(ttt)
                    cursor.execute(
                        "update users set discount=discount+0.5 where mobile_number='"
                        + data_member[0][1]
                        + "'"
                    )
                    ms.commit()
                elif ttt > 500 and ttt <= 1000 and float(data_member[0][2]) > 0:
                    ttt -= (float(data_member[0][2] / 100)) * ttt
                    print(ttt)
                    cursor.execute(
                        "update users set discount=discount+0.2 where mobile_number='"
                        + data_member[0][1]
                        + "'"
                    )
                    ms.commit()
                print(total_p2.cget("text"))
                total_p2.config(text="TOTAL : " + str(ttt))

            ok2.destroy()
            ok3 = tk.Button(
                popup2, text="OK", font=("verdana", 10, "bold"), command=discount_total
            )
            ok3.place(x=215, y=130)

        else:
            print("h", data_member)

            def doublefns():
                popup2.destroy()
                member()

            msg = messagebox.askquestion(
                "Error",
                "please check the username entered or does the cudtomer wants his name to be registered",
            )
            popup2.lift()
            if msg == "yes":
                ok2.destroy()

                def adding():
                    cursor.execute(
                        "insert into users (name,mobile_number,points,discount) values('"
                        + entry_member_name.get()
                        + "','"
                        + entry_member_no.get()
                        + "',0,0)"
                    )
                    ms.commit()
                    msg2 = messagebox.showinfo(" ", "successfully stored")
                    popup2.lift()
                    entry_member_name.delete(0, "end")
                    entry_member_no.delete(0, "end")

                ok4 = tk.Button(
                    popup2, text="OK", font=("calibre", 15, "bold"), command=adding
                )
                ok4.grid(row=5, column=2, sticky="e")

            else:
                entry_member_name.delete(0, "end")
                entry_member_no.delete(0, "end")

    def users():
        global data_member, ttt
        if entry_member_name.get() != "":
            cursor.execute(
                "select* from users where name="
                + "'"
                + entry_member_name.get().lower()
                + "'"
                + ";"
            )
            data_member = cursor.fetchall()
        else:
            cursor.execute(
                "select* from users where mobile_number="
                + "'"
                + entry_member_no.get().lower()
                + "'"
                + ";"
            )
            data_member = cursor.fetchall()

    def doub():
        users()
        checking(data_member)

    # def card_use():
    # print("hey")

    popup2 = tk.Tk()
    popup2.title("BILL")
    popup2.iconbitmap("bucket-clipart-fruit-15.ico")
    popup2_bg = tk.PhotoImage(file="popup2_bg.gif")
    bgggggg = tk.Label(popup2, image=popup2_bg)
    bgggggg.place(x=0, y=0)
    name_m = tk.Label(popup2, text="Name:", font=("verdana"))
    name_m.place(x=15, y=30)

    entry_member_name = tk.Entry(popup2, width=50)
    entry_member_name.place(x=165, y=30)
    entry_member_name.bind("<Return>", users)

    number = tk.Label(popup2, text="Phone Number:", font=("verdana"))
    number.place(x=15, y=80)
    entry_member_no = tk.Entry(popup2, width=30)
    entry_member_no.place(x=165, y=80)
    entry_member_no.bind("<Return>", users)
    ok2 = tk.Button(popup2, text="CHECK", font=("verdana", 10, "bold"), command=doub)
    ok2.place(x=215, y=130)
    total_p2 = tk.Label(
        popup2, text="TOTAL : " + str(total_l.cget("text")[1:]), font=("verdana", 20)
    )
    total_p2.place(x=900, y=400)

    treeview_frame = tk.Frame(popup2)
    treeview_frame.place(x=630, y=70)
    tree_scroll = tk.Scrollbar(treeview_frame)
    tree_scroll.pack(side="right", fill="y")
    sum_bill = ttk.Treeview(treeview_frame, yscrollcommand=tree_scroll.set)
    sum_bill["columns"] = ("one", "two", "three", "four")

    sum_bill.column("#0", anchor="w", width=100)
    sum_bill.column("#1", anchor="w", width=250)
    sum_bill.column("#2", anchor="w", width=100)
    sum_bill.column("#3", anchor="w", width=100)
    sum_bill.column("#4", anchor="w", width=100)

    sum_bill.heading("#0", text="S.No", anchor="w")
    sum_bill.heading("#1", text="Product", anchor="w")
    sum_bill.heading("#2", text="Rate", anchor="w")
    sum_bill.heading("#3", text="Qty", anchor="w")
    sum_bill.heading("#4", text="Price", anchor="w")

    for sum_bill_items in l:
        sum_bill.insert(
            "",
            "end",
            text=sum_bill_items[0],
            values=(
                sum_bill_items[1],
                sum_bill_items[2],
                sum_bill_items[3],
                float(sum_bill_items[3]) * float(sum_bill_items[2]),
            ),
        )
    sum_bill.pack()
    tree_scroll.config(command=sum_bill.yview)

    bill_final = PrettyTable()
    bill_final.field_names = ("PRODUCTS", "RATE", "QUANTITY", "PRICE")
    for bill_items in l:
        bill_items += (float(bill_items[-1]) * float(bill_items[2]),)
        bill_final.add_row(list(bill_items)[1:])

    # prdt = tk.Label(popup2, text=bill_final, font=("courier new", 10))
    # prdt.place(x=700, y=70)

    def card_use():
        global ttt
        ttt = float(total_l.cget("text")[1:])
        phonenumber = input("enter your number")
        usage = int(input("enter amount to be deducted"))
        cursor.execute(
            "select * from members where contact_number='" + phonenumber + "'"
        )
        data_card = cursor.fetchall()
        print(len(data_card))
        amt_acc = data_card[0][4]
        amt_acc -= usage
        cursor.execute(
            "update members set amt=amt-"
            + str(usage)
            + " where contact_number='"
            + phonenumber
            + "';"
        )
        ms.commit()
        ttt -= usage
        total_p2.config(text="TOTAL : " + str(ttt))

    credit_card_img = tk.PhotoImage(file="Images\\credit_card.png")
    credit_card_img = credit_card_img.subsample(2)
    use_card = tk.Button(
        popup2,
        image=credit_card_img,
        command=card_use,
    )
    use_card.place(x=100, y=320)
    heading_bill = tk.Label(popup2, text="BILL", font=("verdana", 30)).place(x=870, y=0)
    """total_p2 = tk.Label(
        popup2, text="TOTAL : " + str(total_l.cget("text")[1:]), font=("verdana", 20)
    )
    total_p2.place(x=900, y=400)"""


member_button = tk.Button(
    main,
    bg="snow",
    height=3,
    width=10,
    text="PAY BILL",
    font=("verdana", 20),
    command=member,
)
member_button.place(x=1140 + 45, y=545 + 39)

# ACCOUNT CARD


def register():
    popup4 = tk.Tk()
    popup4.title("REGISTRATION")
    popup4.geometry("300x170")
    heading = tk.Label(popup4, text="REGISTERATION", font=("verdana", 10, "bold")).grid(
        row=0, column=1, sticky="w"
    )
    username_label = tk.Label(
        popup4, text="First Name         : ", font=("verdana", 10)
    ).grid(row=1, column=0, sticky="w")
    username_entry = tk.Entry(popup4, width=25)
    username_entry.grid(row=1, column=1)
    id_label = tk.Label(popup4, text="Password          : ", font=("verdana", 10)).grid(
        row=2, column=0, sticky="w"
    )
    id_entry = tk.Entry(popup4, show="*", width=25)
    id_entry.grid(row=2, column=1)
    address_label = tk.Label(
        popup4, text="Address            : ", font=("verdana", 10)
    ).grid(row=3, column=0, sticky="w")
    address_entry = tk.Entry(popup4, width=25)
    address_entry.grid(row=3, column=1)
    PHONE_label = tk.Label(popup4, text="Contact Number : ", font=("verdana", 10)).grid(
        row=4, column=0
    )
    PHONE_entry = tk.Entry(popup4, width=25)
    PHONE_entry.grid(row=4, column=1)
    amt_label = tk.Label(popup4, text="Initial amount : ", font=("verdana", 10)).grid(
        row=5, column=0
    )
    amt_entry = tk.Entry(popup4, width=25)
    amt_entry.grid(row=5, column=1)

    def store():
        if (
            len(username_entry.get()) == 0
            or len(id_entry.get()) == 0
            or len(address_entry.get()) == 0
            or len(PHONE_entry.get()) == 0
            or len(amt_entry.get()) == 0
        ):
            messagebox.showerror("Incomplete", "All the data has to be entered")
            popup4.lift()
        else:
            try:
                cursor.execute(
                    "insert into members values('"
                    + id_entry.get()
                    + "','"
                    + username_entry.get()
                    + "','"
                    + address_entry.get()
                    + "','"
                    + PHONE_entry.get()
                    + "',"
                    + amt_entry.get()
                    + ")"
                )
                ms.commit()
                r = messagebox.showinfo("SAVED", "Your account has been saved")
                popup4.destroy()
            except:
                messagebox.showerror("data error", "please enter limited data")
                popup4.lift()
                if len(username_entry.get()) > 30:
                    username_entry.delete(0, "end")
                elif len(id_entry.get()) > 6:
                    id_entry.delete(0, "end")
                elif len(address_entry.get()) > 50:
                    address_entry.delete(0, "end")
                elif len(PHONE_entry.get()) > 10 or (PHONE_entry.get()).isalpha():
                    PHONE_entry.delete(0, "end")

    button_register = tk.Button(popup4, text="Register", bg="snow", command=store).grid(
        row=6, column=1, sticky="ew"
    )


acc_button = tk.Button(
    main,
    text="REGISTER",
    bg="snow",
    height=3,
    width=10,
    font=("verdana", 20),
    command=register,
).place(x=1000, y=545 + 39)


def scanner():
    vid = cv2.VideoCapture(0)
    vid.set(3, 640)
    vid.set(4, 480)
    c = 0

    while True:
        success, img = vid.read()
        for code in decode(img):
            if c == 1:
                break
            else:
                data_req = code
                pts = np.array([code.polygon], np.int32)
                pts = pts.reshape(-1, 1, 2)
                cv2.polylines(img, [pts], True, (255, 0, 255), 5)
                c = 1

        cv2.imshow("Result", img)
        if cv2.waitKey(1) == 27:
            break
        elif c == 1:
            break
    vid.release()
    cv2.destroyAllWindows()


scan = tk.Button(main, text="SCANNER", command=scanner, font=("verdana", 20))
scan.place(x=1000, y=400)


tk.mainloop()
