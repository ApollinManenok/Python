from tkinter import *
 
root = Tk()
 
tx = Text(root,
          width=20,
          height=3,
          font='14')
scr = Scrollbar(root,
                command=tx.xview)
tx.configure(xscrollcommand=scr.set)
 
tx.grid(row=0,column=0)
scr.grid(row=0,column=1)


win = Toplevel(root,
               relief=SUNKEN,
               bd=10,
               bg="lightblue")
win.title("Дочернее окно")
win.minsize(width=400,
            height=200)
win.grid()
win.mainloop()
root.mainloop()
