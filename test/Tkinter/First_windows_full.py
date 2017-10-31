from tkinter import *
 
def printer(event):
    print ("Hi, Peaples!")

#main 
root1 = Tk()

root1.title("Main Window")
root1.geometry("250x250")

but = Button(root1)
but["text"] = "Печать"
but.bind("<Button-1>",printer)
 
but.pack()
root1.mainloop()

