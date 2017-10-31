from tkinter import*

# Okno
root = Tk()
root.title("Third Task")
#root.geometry("700x400")


#scale in frame
u_frame0 = Frame(root,
                 bg = "light green",
                 bd = 15)
u_frame0.pack()

horiz_scale = Scale(u_frame0,
                    orient = HORIZONTAL,
                    length = 250,
                    from_ = 0,
                    to = 100,
                    tickinterval = 10,
                    resolution = 5)
horiz_scale.pack()

# text_pole in frame
u_frame1 = Frame(root,                 
                 bg = "green",
                 bd = 25)
u_frame1.pack()

singl_text = Entry(u_frame1, width=20, bd = 0)
singl_text.pack()

#mnogostr tekst
 
tx = Text(root,
          width=20,
          height=3,
          font='14')
scr = Scrollbar(tx,
                command=tx.yview)
tx.configure(yscrollcommand=scr.set)
 
tx.pack()#(row=0,column=0)
scr.pack(side = RIGHT, fill=Y)#grid(row=0,column=1)



root.mainloop()
