# Main window

from tkinter import *
import shelve
from Numbers import Number
book_field = ['#0','Title', 'Author', 'Publisher','Comment']


def mainWind():
    global entries
    master = Tk()
    master.title('HOME Lib')
    table = Frame(master, bg = 'white')
    table.pack()#grid(row = 0, column = 0, columnspan = 5)
    entries = dict()
    rown = 1
    for (num, label) in enumerate(book_field):
        lab = Label(table, justify = CENTER, text=label)
        lab.grid(row=0, column=num)
    for key in db['num_list']:
        lab1 = Label(table, justify = CENTER, text=str(rown))
        ent0 = Entry(table)
        ent0.insert(0, db[key].title)
        ent1 = Entry(table)
        ent1.insert(0, db[key].author)
        ent2 = Entry(table)
        ent2.insert(0, db[key].publisher)
        ent3 = Entry(table)
        ent3.insert(0, db[key].amount)
        lab1.grid(row = rown, column = 0)
        ent0.grid(row = rown, column = 1)
        ent1.grid(row = rown, column = 2)
        ent2.grid(row = rown, column = 3)
        ent3.grid(row = rown, column = 4)
        coll = (ent0, ent1, ent2, ent3)
        entries[key] = coll
        rown+=1

    
    lab2 = Label(table, text = 'Total: '+str(len(db['num_list'])))
    lab2.grid(row = rown, column = 4)
    Button(master, text='ADD Book').pack(side = LEFT)#grid(row=2, column = 0)
    Button(master, text='Change').pack(side = LEFT)#grid(row=2, column = 1)
    Button(master, text='DELETE').pack(side = LEFT)#grid(row=2, column = 2)
    Button(master, text='QUIT').pack(side = RIGHT)#grid(row=2, column = 4)
    return master


db = shelve.open('database_lib')

master = mainWind()

entries['Num 5'][2].insert(END, 'Check')

master.mainloop()
db.close()
