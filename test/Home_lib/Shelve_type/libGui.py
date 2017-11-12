############################################################
#                         IMPORT
############################################################

from tkinter import *
from tkinter.messagebox import showerror
import shelve
import os

from Objects_lib import *
from Numbers import Number

#shelvename = 'class-shelve'
book_field = ('#0', 'Title', 'Author', 'Publisher', 'Comment')

############################################################
#                       FUNCTIONS
############################################################


def mainWind():
    global entries #diction with Entries
    master = Tk()
    master.title('HOME Lib')
    table = Frame(master, bg = 'white')
    table.pack() #Table of books
    entries = dict()
    rown = 1 #row number
    for (num, label) in enumerate(book_field):# Shapka tablicy
        lab0 = Label(table, justify = CENTER, text=label)
        lab0.grid(row=0, column=num)
    for key in db['num_list']:# vyvod znachenij postrochnyj
        lab1 = Label(table, justify = CENTER, text=str(rown)) #Numeracija strok
        txt0 = Text(table, width=10, height = 1, wrap=WORD)
        txt1 = Text(table, width=10, height = 1, wrap=WORD)
        txt2 = Text(table, width=10, height = 1, wrap=WORD)
        txt3 = Text(table, width=10, height = 1, wrap=WORD)
        txt0.insert(END, db[key].title)
        txt1.insert(END, db[key].author)
        txt2.insert(END, db[key].publisher)
        txt3.insert(END, db[key].amount)
        txt0.config(state = DISABLED)
        txt1.config(state = DISABLED)
        txt2.config(state = DISABLED)
        txt3.config(state = DISABLED)
        lab1.grid(row = rown, column = 0)
        txt0.grid(row = rown, column = 1)
        txt1.grid(row = rown, column = 2)
        txt2.grid(row = rown, column = 3)
        txt3.grid(row = rown, column = 4)
        lab_tab = (txt0, txt1, txt2, txt3)
        entries[key] = lab_tab
        rown+=1
    lab2 = Label(table, text = 'Total: '+str(len(db['num_list'])))
    lab2.grid(row = rown, column = 4)
    
    bttn_tab0 = Button(master, text='ADD Book')
    bttn_tab0.bind('<Button-1>', addBook)
    bttn_tab0.pack(side = LEFT)
    bttn_tab1 = Button(master, text='Change')
    #bttn_tab1.bind('<Button-1>', changeBook)
    bttn_tab1.pack(side = LEFT)
    bttn_tab2 = Button(master, text='DELETE')
    #bttn_tab2.bind('<Button-1>', delBook)
    bttn_tab2.pack(side = LEFT)
    bttn_tab3 = Button(master, text='QUIT')
    #bttn_tab3.bind('<Button-1>', quitProg)
    bttn_tab3.pack(side = RIGHT)
    return master

def addBook(event):
    add_book_field = ('Title','Author','Publisher','Comment')
    add_wind = Toplevel()
    add_wind.title('New book')
    fram0 = Frame(add_wind)
    fram0.pack()
    entries_add = {}
    for (num, label) in enumerate(add_book_field):
        lab = Label(fram0, text=label)
        ent = Entry(fram0)
        ent.bind('<Return>', )
        lab.grid(row=num, column=0)
        ent.grid(row=num, column=1)
        entries_add[label] = ent
    bttn_add_wind0 = Button(add_wind, text='OK')
    #bttn_add_wind0.bind('<Button-1>', ok_addBook)
    bttn_add_wind0.pack(side=RIGHT)
    bttn_add_wind1 = Button(add_wind, text='Cancel')
    bttn_add_wind1.bind('<Button-1>', canc_addBook(event, add_wind))
    bttn_add_wind1.pack(side=LEFT)
    bttn_add_wind2 = Button(add_wind, text='Next')
    #bttn_add_wind2.bind('<Button-1>', next_addBook)
    bttn_add_wind2.pack(side=RIGHT)
    add_wind.mainloop()

#def ok_addBook(event): #change?
    #

def canc_addBook(event, window): #change?
    window.destroy()

#def next_addBook(event):
    #

#def changeBook(event): #There is no such book
    #

#def delBook(event): #There is no such book
    #

#def ok_delBook(event): 
    #

#def canc_delBook(event): 
    #

#def quitProg(event):
    #
    
############################################################
#                      MAIN - GUI
############################################################

db = shelve.open('database_lib')
master = mainWind()
master.mainloop()

##### END PROGRAMM
db.close()
