from tkinter import *
from PIL import Image, ImageTk


def show_error():
    window3 = Toplevel()

    window3.geometry('385x200')
    window3.overrideredirect(True)
    window3.config(bg='white')

    def move_app(e):
        window3.geometry(f'+{e.x_root}+{e.y_root}')

    title_bar = Frame(window3, bg="white", relief="raised", bd=0)
    title_bar.place(x=0, y=0, width=385, height=26)
    title_bar.bind("<B1-Motion>", move_app)

    exitbtn = Button(title_bar, text='X', fg='#242432', borderwidth=0,
                     bg='white', command=window3.destroy,
                     activebackground='red', activeforeground='grey')
    exitbtn.place(x=365, y=2)

    # pop up error window
    img = Image.open('error tab icon.png')
    r_img = img.resize((180, 130), Image.LANCZOS)
    n_img = ImageTk.PhotoImage(r_img)
    error = Label(window3, image=n_img)
    error.place(x=140, y=4,
                width=100, height=100)

    errortext = Label(window3, text='P l e a s e   m a k e   s u r e   t o   f i l l',
                      font=('@Yu Gothic Light', 11), bg='white', fg='black')
    errortext2 = Label(window3, text='o u t   t h e   e n t r y   f i e l d s',
                       font=('@Yu Gothic Light', 11), bg='white', fg='black')

    errortext2.place(x=80, y=110)
    errortext.place(x=67, y=90)

    ok = Button(window3, text='O K', bg='white', fg='black', relief=SOLID,
                borderwidth=1, font=('@Yu Gothic Light', 13),
                command=window3.destroy)
    ok.place(x=170, y=150, width=35, height=23)

    window3.mainloop()
