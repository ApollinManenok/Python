from tkinter import *

root = Tk()
root.title("New Window!")
root.geometry("500x500")

bttn1 = Button(root, text = 'I do nothing!!')
bttn1.grid()

bttn2 = Button(root)
bttn2.grid()
bttn2.configure(text = 'I am too!')

bttn3 = Button(root)
bttn3.grid()
bttn3['text'] = 'And I!'

root.mainloop()
