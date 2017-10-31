from tkinter import *
 
class But_print(Button):
    def __init__(self, text):
        self.text = text
        self.but = Button(root)
        self.but["text"] = self.text
        self.but["bg"] = "red"
        self.but.bind("<Button-1>",self.printer)
        self.but.pack()
    def printer(self,event):
        print ("Как всегда очередной 'Hello World!'")

#main 
root = Tk()
root.title("Main Window")
root.geometry("250x250")
obj = But_print('Печать')

root.mainloop()
