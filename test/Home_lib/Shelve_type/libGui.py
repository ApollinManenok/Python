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


#### Osnovnoe okno s tablicej

def mainWind():
    global entries #diction with Entries
    master = Tk()
    master.title('HOME Lib')
    fram0 = Frame(master, bg = 'white')
    fram0.grid_rowconfigure(0, weight = 1)
    fram0.grid_columnconfigure(0, weight = 1)
    fram0.pack()
    
    for (num, label) in enumerate(book_field):# Shapka tablicy
        lab0 = Label(fram0, justify = CENTER, text=label, bg = 'grey')
        lab0.grid(row=0, column=num, sticky = W)
##############
    canva = Canvas(fram0, scrollregion=(0,0,300,300))
    #table = Frame(canva, bg = 'white', width = 300, height = 300)
    #canva.create_window(0,0, anchor = NW, width = 300, height = 300, window = table)

    #canva.config(width = 300, height = 300)
    
    canva.grid(row = 1, column=1, columnspan = 5, sticky = 'news')
    #yscroll = Scrollbar(canva, orient = VERTICAL)
    #yscroll.grid(row = 0, column = 5, sticky = 'nsw')
    #yscroll.config(command = canva.yview)
    #canva.config(yscrollcommand = yscroll.set)
    #xscroll = Scrollbar(fram0, orient = HORIZONTAL)
    #xscroll.grid(row = 1, column = 6, sticky = E+W)
    #table.grid_columnconfigure(0,weight = 1)
    #table.grid_columnconfigure(1,weight = 2)
    #table.grid_columnconfigure(2,weight = 2)
    #table.grid_columnconfigure(3,weight = 2)
    #table.grid_columnconfigure(4,weight = 3)
    #table.grid_rowconfigure(1,weight = 1)
    #table.grid(row = 1, column = 0, columnspan = 5) #Table of books
###############
    entries = dict()
    rown = 1 #row number
    
    for key in db['num_list']:# vyvod znachenij postrochnyj
        lab1 = Label(table, justify = CENTER, text=str(rown), bg = 'white') #Numeracija strok
        txt0 = Text(table, width=15, height = 2, wrap=WORD)
        txt1 = Text(table, width=10, height = 2, wrap=WORD)
        txt2 = Text(table, width=10, height = 2, wrap=WORD)
        txt3 = Text(table, width=15, height = 2, wrap=WORD)
        txt0.insert(END, db[key].title)
        txt1.insert(END, db[key].author)
        txt2.insert(END, db[key].publisher)
        txt3.insert(END, db[key].amount)
        txt0.config(state = DISABLED)
        txt1.config(state = DISABLED)
        txt2.config(state = DISABLED)
        txt3.config(state = DISABLED)
        lab1.grid(row = rown, column = 0, sticky = NW)
        txt0.grid(row = rown, column = 1, sticky = NW)
        txt1.grid(row = rown, column = 2, sticky = NW)
        txt2.grid(row = rown, column = 3, sticky = NW)
        txt3.grid(row = rown, column = 4, sticky = NW)
        lab_tab = (txt0, txt1, txt2, txt3)
        entries[key] = lab_tab
        rown+=1
        
    
    lab2 = Label(fram0, text = 'Total: '+str(len(db['num_list'])), bg = 'white')
    lab2.grid(row = 2, column = 0)
    
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
####################################################################


#### Dobavlenie knig

def addBook(event):
    add_book_field = ('Title','Author','Publisher','Comment')
    add_wind = Toplevel()
    add_wind.title('New book')
    fram1 = Frame(add_wind)
    fram1.pack()
    entries_add = {}
    for (num, label) in enumerate(add_book_field):
        lab = Label(fram1, text=label)
        ent = Entry(fram1)
        ent.bind('<Return>', )
        lab.grid(row=num, column=0)
        ent.grid(row=num, column=1)
        entries_add[label] = ent
    bttn_add_wind0 = Button(add_wind, text='OK')
    #bttn_add_wind0.bind('<Button-1>', ok_addBook)
    bttn_add_wind0.pack(side=RIGHT)
    bttn_add_wind1 = Button(add_wind, text='Cancel', command = add_wind.destroy)
    #bttn_add_wind1.bind('<Button-1>', add_wind.destroy)
    bttn_add_wind1.pack(side=LEFT)
    bttn_add_wind2 = Button(add_wind, text='Next')
    #bttn_add_wind2.bind('<Button-1>', next_addBook)
    bttn_add_wind2.pack(side=RIGHT)
    return add_wind

#def ok_addBook(event): #change?
    #

#def next_addBook(event):
    #

############################################################


# Izmenenie knigi

#def changeBook(event): #There is no such book
    #

#def ok_changeBook(event): #change?
    #

#def next_chengeBook(event):
    #

############################################################


# Udalenie knigi

#def delBook(event): #There is no such book
    #

#def ok_delBook(event): 
    #

#def canc_delBook(event): 
    #

############################################################
#                      MAIN - GUI
############################################################

db = shelve.open('database_lib')
master = mainWind()
master.mainloop()

##### END PROGRAMM
db.close()
