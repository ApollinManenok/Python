from tkinter import *

root = Tk()
root.title("Widjets 1")
#root.geometry("220x900")

#Кнопка
but = Button(root,
             text = 'This is Button',
             width = 30,
             height = 5,
             bg = 'orange',
             fg = 'blue',
             font = 'Arial 10')

but.pack()

#Метка
lab = Label(root,
            text="Это метка! \n Из двух строк.",
            font="Arial 18")
lab.pack()

#Однострочное текстовое поле
ent = Entry(root, width=20, bd=10) #text = "Hi")
ent.pack()

#Многострочное текстовое поле
tex = Text(root, width=20, height = 5,
          font="Verdana 12",
          wrap=CHAR)
tex.pack()

#Радиокнопки
var = IntVar()
var.set(2)
rad0 = Radiobutton(root, text="Первая",
                   variable=var, value=0).pack()
rad1 = Radiobutton(root, text="Вторая",
                   variable=var, value=1)
rad2 = Radiobutton(root, text="Третья",
                   variable=var, value=2)
rad1.pack()
rad2.pack()

#Флажки
c1 = IntVar()
c2 = IntVar()
che1 = Checkbutton(root, text="Первый флажок",
                   variable=c1, onvalue=1, offvalue=0).pack()
che2 = Checkbutton(root,text="Второй флажок",
                   variable=c2, onvalue=1, offvalue=0)
che2.pack()

#Списки
r = ['Linux', 'Python', 'Tk', 'Tkinter','Igor']
lis = Listbox(root, selectmode=MULTIPLE, height=4)
for i in r:
     lis.insert(END,i)
lis.pack()


root.mainloop()
