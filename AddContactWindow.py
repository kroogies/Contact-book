from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import ErrorWindow as s_e
from tkinter import messagebox


def entryfields_window():
    window2 = Toplevel()

    window2.overrideredirect(True)
    window2.config(bg='#0f0f0f')
    window2.geometry('360x565')

    # title bar
    def move_app(e):
        window2.geometry(f'+{e.x_root}+{e.y_root}')

    title_bar = Frame(window2, bg="#242423", relief="raised", bd=0)
    title_bar.place(x=0, y=0, width=400, height=24)
    title_bar.bind("<B1-Motion>", move_app)

    exitbtn = Button(title_bar, text='X', fg='#ffffff', borderwidth=0,
                     bg='#242423', command=window2.destroy,
                     activebackground='red', activeforeground='#ffffff')
    exitbtn.place(x=330, y=2)

    # random line
    line = Frame(window2, bg='#242423')
    line.place(x=0, y=40, width=500, height=2)

    # new contact title bar
    cb = Image.open('new contact tab.jpg')
    resized_img2 = cb.resize((170, 45), Image.LANCZOS)
    new_img2 = ImageTk.PhotoImage(resized_img2)
    tab = Label(title_bar, image=new_img2, borderwidth=0)
    tab.place(x=-5, y=1)

    # first name entry and label
    fname_entry = Entry(window2, font=('@Yu Gothic Light', 18), relief=SOLID, borderwidth=3)
    fname_entry.place(x=30, y=120,
                      width=300, height=30)
    fname_text = Label(window2, text='F I R S T   N A M E', font=('@Yu Gothic Light', 15), fg='#ffffff',
                       bg='#0f0f0f')
    fname_text.place(x=30, y=90)

    # last name entry and label
    lname_entry = Entry(window2, font=('@Yu Gothic Light', 18), relief=SOLID, borderwidth=3)
    lname_entry.place(x=30, y=200,
                      width=300, height=30)
    lname_text = Label(window2, text='L A S T   N A M E', font=('@Yu Gothic Light', 15), fg='#ffffff',
                       bg='#0f0f0f')
    lname_text.place(x=30, y=170)

    # email entry and label
    email = Entry(window2, font=('@Yu Gothic Light', 18), relief=SOLID, borderwidth=3)
    email.place(x=30, y=280,
                width=300, height=30)
    e_label = Label(window2, text='E M A I L   A D D R E S S', font=('@Yu Gothic Light', 15), fg='#ffffff',
                    bg='#0f0f0f')
    e_label.place(x=30, y=250)

    # phone number entry and label

    PNumber = int()
    PNumber = Entry(window2, font=('@Yu Gothic Light', 18), relief=SOLID, borderwidth=3)
    PNumber.place(x=30, y=370,
               width=300, height=30)
    nmbr_label = Label(window2, text='P H O N E   N U M B E R', font=('@Yu Gothic Light', 15), fg='#ffffff',
                       bg='#0f0f0f')
    nmbr_label.place(x=30, y=340)

    def addb():
        fields = [fname_entry.get(), lname_entry.get(), PNumber.get(), email.get()]

        if '' in fields:
            s_e.show_error()

        try:
            fields[2] = int(fields[2])
        except ValueError:
            messagebox.showerror('Error', 'Numbers only please')

        else:
            pathcon = 'contacts1.db'
            con = sqlite3.connect(pathcon)
            c = con.cursor()
            c.execute('INSERT INTO contacts VALUES (:fname_entry, :lname_entry, :PNumber, :email)',
                      {'fname_entry': fields[0],
                       'lname_entry': fields[1],
                       'PNumber': fields[2],
                       'email': fields[3]})

            con.commit()
            con.close()
            fname_entry.delete(0, END)
            lname_entry.delete(0, END)
            PNumber.delete(0, END)
            email.delete(0, END)

    # add btn
    addbtn = Button(window2, text='A D D', font=('@Yu Gothic Light', 16), fg='#000000', bg='#ffffff',
                    relief=SOLID, borderwidth=3, activeforeground='#000000', activebackground='#bdbebf', command=addb)
    addbtn.place(x=115, y=420,
                 width=120, height=45)
    window2.bind("<Return>", lambda event: addb())

    # cancel btn
    cancelbtn = Button(window2, text='C A N C E L', font=('@Yu Gothic Light', 16), fg='#ffffff', bg='#393a3b',
                       relief=SOLID, borderwidth=3, command=window2.destroy)
    cancelbtn.place(x=115, y=470,
                    width=120, height=45)

    window2.mainloop()
