from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import ErrorWindow as s_e
from tkinter import messagebox


def editcontacts():
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
    cb = Image.open('edit contact tab.png')
    resized_img2 = cb.resize((170, 45), Image.LANCZOS)
    new_img2 = ImageTk.PhotoImage(resized_img2)
    tab = Label(title_bar, image=new_img2, borderwidth=0)
    tab.place(x=-5, y=1)

    # id search entry, search btn, and btn function
    id_entry = Entry(window2, font=('@Yu Gothic Light', 18), relief=SOLID, borderwidth=3)
    id_entry.place(x=21, y=90,
                   width=300, height=30)
    id_text = Label(window2, text="S E A R C H   C O N T A C T", font=('@Yu Gothic Light', 15), fg='#ffffff',
                    bg='#0f0f0f')
    id_text.place(x=21, y=60)

    textvar = StringVar()
    textvar2 = StringVar()

    def getdata():
        get_input = id_entry.get()  # not accepting two digits/three digits id's

        if get_input != '':
            con = sqlite3.connect('contacts1.db')
            c = con.cursor()
            c.execute("SELECT * FROM contacts WHERE rowid = :id_entry", get_input)
            data = c.fetchall()

            def show_fields():
                store_contact_id = id_entry.get()

                searchbtn.destroy()
                id_entry.destroy()
                id_text.destroy()
                searched_contact.destroy()

                # first name entry and label
                fnamevar = StringVar()
                fname_entry = Entry(window2, font=('@Yu Gothic Light', 18), relief=SOLID, borderwidth=3,
                                    textvariable=fnamevar)
                fname_entry.place(x=30, y=80,
                                  width=300, height=30)
                fname_text = Label(window2, text='F I R S T   N A M E', font=('@Yu Gothic Light', 15),
                                   fg='#ffffff',
                                   bg='#0f0f0f')
                fname_text.place(x=30, y=50)

                # last name entry and label
                lnamevar = StringVar()
                lname_entry = Entry(window2, font=('@Yu Gothic Light', 18), relief=SOLID, borderwidth=3,
                                    textvariable=lnamevar)
                lname_entry.place(x=30, y=150,
                                  width=300, height=30)
                lname_text = Label(window2, text='L A S T   N A M E', font=('@Yu Gothic Light', 15), fg='#ffffff',
                                   bg='#0f0f0f')
                lname_text.place(x=30, y=120)

                # email entry and label
                emailvar = StringVar()
                email = Entry(window2, font=('@Yu Gothic Light', 18), relief=SOLID, borderwidth=3,
                              textvariable=emailvar)
                email.place(x=30, y=230,
                            width=300, height=30)
                e_label = Label(window2, text='E M A I L   A D D R E S S', font=('@Yu Gothic Light', 15),
                                fg='#ffffff',
                                bg='#0f0f0f')
                e_label.place(x=30, y=200)

                # phone number entry and label
                nmbrvar = StringVar()
                nmbr = Entry(window2, font=('@Yu Gothic Light', 18), relief=SOLID, borderwidth=3,
                             textvariable=nmbrvar)
                nmbr.place(x=30, y=310,
                           width=300, height=30)
                nmbr_label = Label(window2, text='P H O N E   N U M B E R', font=('@Yu Gothic Light', 15),
                                   fg='#ffffff',
                                   bg='#0f0f0f')
                nmbr_label.place(x=30, y=280)

                for i in data:
                    fnamevar.set(i[0])
                    lnamevar.set(i[1])
                    nmbrvar.set(str(i[2]))
                    emailvar.set(i[3])

                # edit contact btn function
                def eddb():
                    fields = [fname_entry.get(), lname_entry.get(), nmbr.get(), email.get(), store_contact_id]

                    if '' in fields:
                        s_e.show_error()

                    try:
                        fields[2] == str(int(fields[2]))
                    except ValueError:
                        messagebox.showerror('Error', 'Numbers only please')

                    else:
                        con = sqlite3.connect('contacts1.db')
                        cursor = con.cursor()
                        cursor.execute("UPDATE contacts SET Fname = :fname_entry, Lname = :lname_entry, PNumber = :nmbr, Email = :email WHERE rowid = :store_contact_id", fields)

                        con.commit()
                        con.close()

                        fname_entry.delete(0, END)
                        lname_entry.delete(0, END)
                        nmbr.delete(0, END)
                        email.delete(0, END)
                        window2.destroy()

                # edit contact btn
                editbtn = Button(window2, text='U P D A T E', font=('@Yu Gothic Light', 16), fg='#000000', bg='#ffffff',
                                relief=SOLID, borderwidth=3, activeforeground='#000000', activebackground='#bdbebf',
                                command=eddb)  # added command, might bug out tho
                editbtn.place(x=115, y=370,
                             width=120, height=45)

                # cancel edit btn
                cancelbtn = Button(window2, text='C A N C E L', font=('@Yu Gothic Light', 16), fg='#ffffff',
                                   bg='#393a3b',
                                   relief=SOLID, borderwidth=3, command=window2.destroy)
                cancelbtn.place(x=115, y=420,
                                width=120, height=45)

            notfoundmsg = Label(window2, textvariable=textvar2, fg='#ffffff', font=('@Yu Gothic Light', 20),
                                bg='#0f0f0f')

            searched_contact = Button(window2, textvariable=textvar, fg='#ffffff',
                                      font=('@Yu Gothic Light', 20), bg='#0f0f0f', relief=FLAT,
                                      command=show_fields)

            if len(data) == 0:
                textvar.set('')
                searched_contact.config(state=DISABLED)

                notfoundmsg.place(x=80, y=170)
                textvar2.set('No contact found')

            if len(data) == 1:
                searched_contact.place(x=130, y=190)

                for records in data:
                    textvar.set(records[0])

                textvar2.set('')

    img3 = Image.open('final search button.png')
    resized_img3 = img3.resize((24, 24), Image.LANCZOS)
    new_img3 = ImageTk.PhotoImage(resized_img3)
    searchbtn = Button(window2, image=new_img3, command=getdata, borderwidth=0)
    searchbtn.place(x=318, y=93, width=24, height=24)

    window2.mainloop()