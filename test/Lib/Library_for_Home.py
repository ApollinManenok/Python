#########################################################
#                       IMPORT
#########################################################

from tkinter import *


#########################################################
#                     FUNCTIONS
#########################################################

def output_b(event):
    txt1.insert(END, b)

def output_a(event):
    txt0.insert(END, a)

def get_a(event):
    a = txt1.get(1.0, END)
    
def get_b(event):
    b = txt0.get(1.0, END)

def insert_a(event):
    a = txt1.get(1.0, END)
    
def insert_b(event):
    b = txt0.get(1.0, END)


#########################################################
#                       BODY
#########################################################


root = Tk()

root.title("Library for HOME")
root.geometry("500x500")


bttn0 = Button(root,
               text = "x",
               font = "Consolas 12",
               fg = "Black",
               bg = "red",
               command=root.destroy)
bttn0.grid(row = 0, column = 0, rowspan = 1, columnspan = 1, sticky = 'w')

txt0 = Text(root,
            height = 10,
            width = 25,
            bg = "white",
            fg = "black",
            font = "Consolas 12",
            wrap = WORD)
txt0.grid(row = 1, column = 0, rowspan = 3, columnspan = 3)


txt1 = Text(root,
            height = 10,
            width = 25,
            bg = "white",
            fg = "black",
            font = "Consolas 12",
            wrap = WORD)
txt1.grid(row = 1, column = 5, rowspan = 3, columnspan = 3)

a=''
b=''

bttn1 = Button(root,
               text = "Copy from 1 to 2",
               font = "Consolas 12",
               fg = "black",
               bg = "pink")
bttn1.grid(row = 5, column = 0)
bttn1.bind("<Button-1>", output_b)
bttn1.bind("<Button-2>", output_a)

bttn2 = Button(root,
               text = "Copy from 2",
               font = "Consolas 12",
               fg = "black",
               bg = "pink",
               command=txt0.get('1.0', END))
bttn2.grid(row = 5, column = 1)
bttn2.bind("<Button-1>", get)
bttn2.bind("<Button-2>", b = txt0.get(1.0, END))

bttn3 = Button(root,
               text = "Delete",
               font = "Consolas 12",
               fg = "black",
               bg = "pink",
               command=txt0.delete('1.0', END))
bttn3.grid(row = 5, column = 2)
bttn3.bind("<Button-1>", txt1.delete(1.0, END))
bttn3.bind("<Button-2>", txt0.delete(1.0, END))

root.mainloop()

