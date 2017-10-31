from tkinter import*

# Okno
root = Tk()
root.title("First Task")
root.geometry("500x600")

#tekst
name_pole0 = Label(root,
                   text="Ваш адрес:",
                   font="Consolas 15")
name_pole0.pack()

singl_text = Entry(root, width=30, bd = 5)
singl_text.pack()
#mnogostr tekst
name_pole1 = Label(root,
                   text="Комментарий:",
                   font="Consolas 15")
name_pole1.pack()
multy_text = Text(root,
                  width = 40,#shirina
                  height = 10,#vysota
                  font="Consolas 10",#shrift
                  wrap = CHAR)#perenos
multy_text.pack()
#knopka otpravit'(print)
bttn0 = Button(root,
               text = "Отправить",#text na knopke
               width = 10,
               height = 2,
               bg = 'light blue',#fon
               font = 'Consolas 10')
bttn0.pack()
#radioknop 0-10 11-20 21-30 31-40
name_pole2 = Label(root,
                   text="Сколько штук?",
                   font="Consolas 10")
name_pole2.pack()
rad_var = IntVar()
rad_var.set(0)

rad_but0 = Radiobutton(root, text="0-10", variable=rad_var, value = 0).pack()
rad_but1 = Radiobutton(root, text="11-20", variable=rad_var, value = 1).pack()
rad_but2 = Radiobutton(root, text="21-30", variable=rad_var, value = 2).pack()
rad_but3 = Radiobutton(root, text="31-40", variable=rad_var, value = 3).pack()
#flag cvet krasn, sin, zel, zhelt
name_pole2 = Label(root,
                   text="Какого цвета?",
                   font="Consolas 10")
name_pole2.pack()

fl1 = IntVar()
fl2 = IntVar()
fl3 = IntVar()
fl4 = IntVar()

fl_but = Checkbutton(root, text = "RED", bg = 'RED', variable = fl1, onvalue=1, offvalue=0).pack()
fl_but = Checkbutton(root, text = "BLUE", bg = 'BLUE', variable = fl1, onvalue=1, offvalue=0).pack()
fl_but = Checkbutton(root, text = "GREEN", bg = 'GREEN', variable = fl1, onvalue=1, offvalue=0).pack()
fl_but = Checkbutton(root, text = "YELLOW", bg = 'YELLOW', variable = fl1, onvalue=1, offvalue=0).pack()


root.mainloop()
