# flaws: no delete button, search box doesn't accept two/three digit ids, and two bugs
# bug one, search btn, if there's no contact found after searching an existing contact,
# the button stays just underneath the label

# bug two, search box and edit fields, if you keep searching and searching and finally decide
# to edit a contact, the button doesn't get destroyed and remains in the window even when transitioning
# to the edit fields page

from tkinter import *
from PIL import Image, ImageTk
import AddContactWindow as acd
import sqlite3
import EditContactWindow as ecd


window = Tk()

# root
window.geometry('495x530')
window.config(bg='#0f0f0f')
window.title('Contact Book - Yeshua')
window.overrideredirect(True)


def move_app(e):
    window.geometry(f'+{e.x_root}+{e.y_root}')


title_bar = Frame(window, bg="#242423", relief="raised", bd=0)
title_bar.place(x=0, y=0, width=495, height=28)
title_bar.bind("<B1-Motion>", move_app)

exitbtn = Button(title_bar, text='X', fg='#ffffff', borderwidth=0,
                 bg='#242423', command=window.destroy,
                 activebackground='red', activeforeground='#ffffff')
exitbtn.place(x=480, y=3)

# line
line = Frame(window, bg='#242423')
line.place(x=0, y=45, width=500, height=1)

# images
cb = Image.open('tab.jpg')
resized_img2 = cb.resize((170, 45), Image.LANCZOS)
new_img2 = ImageTk.PhotoImage(resized_img2)
tab = Label(title_bar, image=new_img2, borderwidth=0)
tab.place(x=20, y=1)

# drop down menu
menu = Button(title_bar, text='☰', bg='#242423', fg='#ffffff',
              activeforeground='#0f0f0f', activebackground='#242423', borderwidth=0)
menu.place(x=4, y=-10, width=30, height=50)

# buttons
btn = Image.open('sureaddbtn.png')
resized_img = btn.resize((60, 60), Image.LANCZOS)
new_img = ImageTk.PhotoImage(resized_img)
addbtn = Button(window, image=new_img, relief=SOLID, borderwidth=0, command=acd.entryfields_window)
addbtn.place(x=410, y=440, width=55, height=55)

habtn = Image.open('edit button.png')
resized_img3 = habtn.resize((47, 47), Image.LANCZOS)
new_img3 = ImageTk.PhotoImage(resized_img3)
editbtn = Button(window, image=new_img3, relief=SOLID, borderwidth=0, command=ecd.editcontacts)
editbtn.place(x=360, y=445, width=47, height=47)

# empty labels
c = StringVar()
c2 = StringVar()
c3 = StringVar()
c4 = StringVar()
c5 = StringVar()
c6 = StringVar()
c7 = StringVar()
c8 = StringVar()
c9 = StringVar()
c0 = StringVar()

# line
Label(text='__________________________________________________________________',
      font=('@Yu Gothic Light', 12), fg='#242432', bg='#0f0f0f').place(x=-2, y=60)

# ID
Label(text='ID', font=('@Yu Gothic Light', 12), fg='white', bg='#0f0f0f').place(x=3, y=50)

# Name
Label(text='Name', font=('@Yu Gothic Light', 12), fg='white', bg='#0f0f0f').place(x=70, y=50)

# Email
Label(text='Email Address', font=('@Yu Gothic Light', 12), fg='white', bg='#0f0f0f').place(x=380, y=50)

# Number
Label(text='Phone Number', font=('@Yu Gothic Light', 12), fg='white', bg='#0f0f0f').place(x=230, y=50)

# query 1


def query1():
    con = sqlite3.connect('contacts1.db')
    cursor = con.cursor()
    cursor.execute("SELECT rowid, * FROM contacts WHERE rowid == 1")
    records = cursor.fetchall()
    con.commit()
    con.close()

    textvar = StringVar()
    no_contacts = Label(window, textvariable=textvar, font=('@Yu Gothic Light', 20),
                        bg='#0f0f0f', fg='#ffffff')
    no_contacts.place(x=85, y=240)

    if len(records) == 0:
        textvar.set('N o t h i n g   t o   s h o w')

    else:
        # for loop to iterate individual contact
        textvar.set('')
        for a1 in records:
            c.set(str(a1[0]) + ' | ' + a1[1] + ' ' + a1[2] + ' | ' + str(a1[3]) + ' | ' + a1[4])


def query2():
    con = sqlite3.connect('contacts1.db')
    cursor = con.cursor()
    cursor.execute("SELECT rowid, * FROM contacts WHERE rowid == 2")
    records = cursor.fetchall()
    con.commit()
    con.close()

    if len(records) == 0:
        pass

    else:
        # for loop to iterate individual contact
        for b1 in records:
            c2.set(str(b1[0]) + ' | ' + b1[1] + ' ' + b1[2] + ' | ' + str(b1[3]) + ' | ' + b1[4])


def query3():
    con = sqlite3.connect('contacts1.db')
    cursor = con.cursor()
    cursor.execute("SELECT rowid, * FROM contacts WHERE rowid == 3")
    records = cursor.fetchall()
    con.commit()
    con.close()

    if len(records) == 0:
        pass

    else:
        # for loop to iterate individual contact
        for ui in records:
            c3.set(str(ui[0]) + ' | ' + ui[1] + ' ' + ui[2] + ' | ' + str(ui[3]) + ' | ' + ui[4])


def query4():
    con = sqlite3.connect('contacts1.db')
    cursor = con.cursor()
    cursor.execute("SELECT rowid, * FROM contacts WHERE rowid == 4")
    records = cursor.fetchall()
    con.commit()
    con.close()

    if len(records) == 0:
        pass

    else:
        # for loop to iterate individual contact
        for hu in records:
            c4.set(str(hu[0]) + ' | ' + hu[1] + ' ' + hu[2] + ' | ' + str(hu[3]) + ' | ' + hu[4])


def query5():
    con = sqlite3.connect('contacts1.db')
    cursor = con.cursor()
    cursor.execute("SELECT rowid, * FROM contacts WHERE rowid == 5")
    records = cursor.fetchall()
    con.commit()
    con.close()

    if len(records) == 0:
        pass

    else:
        # for loop to iterate individual contact
        for oi in records:
            c5.set(str(oi[0]) + ' | ' + oi[1] + ' ' + oi[2] + ' | ' + str(oi[3]) + ' | ' + oi[4])



def query6():
    con = sqlite3.connect('contacts1.db')
    cursor = con.cursor()
    cursor.execute("SELECT rowid, * FROM contacts WHERE rowid == 6")
    records = cursor.fetchall()
    con.commit()
    con.close()

    if len(records) == 0:
        pass

    else:
        # for loop to iterate individual contact
        for ko in records:
            c6.set(str(ko[0]) + ' | ' + ko[1] + ' ' + ko[2] + ' | ' + str(ko[3]) + ' | ' + ko[4])


def query7():
    con = sqlite3.connect('contacts1.db')
    cursor = con.cursor()
    cursor.execute("SELECT rowid, * FROM contacts WHERE rowid == 7")
    records = cursor.fetchall()
    con.commit()
    con.close()

    if len(records) == 0:
        pass

    else:
        # for loop to iterate individual contact
        for qi in records:
            c7.set(str(qi[0]) + ' | ' + qi[1] + ' ' + qi[2] + ' | ' + str(qi[3]) + ' | ' + qi[4])



def query8():
    con = sqlite3.connect('contacts1.db')
    cursor = con.cursor()
    cursor.execute("SELECT rowid, * FROM contacts WHERE rowid == 8")
    records = cursor.fetchall()
    con.commit()
    con.close()

    if len(records) == 0:
        pass

    else:
        # for loop to iterate individual contact
        for qi in records:
            c8.set(str(qi[0]) + ' | ' + qi[1] + ' ' + qi[2] + ' | ' + str(qi[3]) + ' | ' + qi[4])


def query9():
    con = sqlite3.connect('contacts1.db')
    cursor = con.cursor()
    cursor.execute("SELECT rowid, * FROM contacts WHERE rowid == 9")
    records = cursor.fetchall()
    con.commit()
    con.close()

    if len(records) == 0:
        pass

    else:
        # for loop to iterate individual contact
        for qi in records:
            c9.set(str(qi[0]) + ' | ' + qi[1] + ' ' + qi[2] + ' | ' + str(qi[3]) + ' | ' + qi[4])


def query10():
    con = sqlite3.connect('contacts1.db')
    cursor = con.cursor()
    cursor.execute("SELECT rowid, * FROM contacts WHERE rowid == 10")
    records = cursor.fetchall()
    con.commit()
    con.close()

    if len(records) == 0:
        pass

    else:
        # for loop to iterate individual contact
        for qi in records:
            c0.set(str(qi[0]) + ' | ' + qi[1] + ' ' + qi[2] + ' | ' + str(qi[3]) + ' | ' + qi[4])


window.bind('<Enter>', lambda event: query1())
contact1_label = Label(window, textvariable=c, bg='#0f0f0f', fg='white',
                       font=('@Yu Gothic Light', 12))
contact1_label.place(x=4, y=100)


window.bind('<Enter>', lambda event: query2(), add="+")
contact2_label = Label(window, textvariable=c2, bg='#0f0f0f', fg='white',
                       font=('@Yu Gothic Light', 12))
contact2_label.place(x=4, y=130)


window.bind('<Enter>', lambda event: query3(), add="+")
contact3_label = Label(window, textvariable=c3, bg='#0f0f0f', fg='white',
                       font=('@Yu Gothic Light', 12))
contact3_label.place(x=4, y=160)


window.bind('<Enter>', lambda event: query4(), add="+")
contact4_label = Label(window, textvariable=c4, bg='#0f0f0f', fg='white',
                       font=('@Yu Gothic Light', 12))
contact4_label.place(x=4, y=190)


window.bind('<Enter>', lambda event: query5(), add="+")
contact5_label = Label(window, textvariable=c5, bg='#0f0f0f', fg='white',
                       font=('@Yu Gothic Light', 12))
contact5_label.place(x=4, y=220)


window.bind('<Enter>', lambda event: query6(), add="+")
contact6_label = Label(window, textvariable=c6, bg='#0f0f0f', fg='white',
                       font=('@Yu Gothic Light', 12))
contact6_label.place(x=4, y=250)


window.bind('<Enter>', lambda event: query7(), add="+")
contact7_label = Label(window, textvariable=c7, bg='#0f0f0f', fg='white',
                       font=('@Yu Gothic Light', 12))
contact7_label.place(x=4, y=280)


window.bind('<Enter>', lambda event: query8(), add="+")
contact8_label = Label(window, textvariable=c8, bg='#0f0f0f', fg='white',
                       font=('@Yu Gothic Light', 12))
contact8_label.place(x=4, y=310)


window.bind('<Enter>', lambda event: query9(), add="+")
contact9_label = Label(window, textvariable=c9, bg='#0f0f0f', fg='white',
                       font=('@Yu Gothic Light', 12))
contact9_label.place(x=4, y=340)


window.bind('<Enter>', lambda event: query10(), add="+")
contact10_label = Label(window, textvariable=c0, bg='#0f0f0f', fg='white',
                       font=('@Yu Gothic Light', 12))
contact10_label.place(x=4, y=370)

window.mainloop()
