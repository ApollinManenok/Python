############################################################
#                         IMPORT
############################################################

from tkinter import *
from tkinter.messagebox import showerror
import shelve
import os

from Objects_lib import Book

table_field = [[4, '#0'], [20, 'Название'], [18, 'Серия'], [18, 'Автор'], [18, 'Издательство'], [7, 'Стр.'], [25, 'Комментарий']]
add_book_field = ['Название','Серия', 'Автор', 'Издательство', 'Стр.', 'Комментарий']

############################################################
#                       FUNCTIONS
############################################################

#### Zapis'

def print_record(key, last_row):
    lab1 = Label(table, justify = RIGHT, width = 4, text=str(last_row), font = 'Consolas 12', bg = 'white') #Numeracija strok
    lab1.grid(row = last_row, column = 0, sticky = NW)
    book_data = [[20, db[key].title], [18, db[key].series], [18, db[key].author], [18, db[key].publisher], [7, db[key].pages], [25, db[key].comment]]
    coll = 1
    lab_tab = list()
    lab_tab.append(lab1)
    for data in book_data:
        txt = Text(table, width=data[0], height = 2, font = 'Consolas 12', wrap=WORD)
        txt.insert(END, data[1])
        txt.config(state = DISABLED)
        txt.grid(row = last_row, column = coll, sticky = NW)
        lab_tab.append(txt)
        coll+=1
    texties[key] = lab_tab
        

#### Dobavlenie knig

def addBook(event):
    global entries_add
    global add_wind
    add_wind = Toplevel()
    add_wind.title('Новая книга')
    fram1 = Frame(add_wind)
    fram1.pack()
    entries_add = dict()
    for (num, label) in enumerate(add_book_field):
        lab = Label(fram1, text=label)
        ent = Entry(fram1)
        lab.grid(row=num, column=0)
        ent.grid(row=num, column=1)
        entries_add[label] = ent
    bttn_add_wind0 = Button(add_wind, text='OK')
    bttn_add_wind0.bind('<Button-1>', ok_addBook)
    bttn_add_wind0.pack(side=RIGHT)
    bttn_add_wind1 = Button(add_wind, text='Отмена', command = add_wind.destroy)
    bttn_add_wind1.pack(side=LEFT)
    bttn_add_wind2 = Button(add_wind, text='Следующая')
    bttn_add_wind2.bind('<Button-1>', next_addBook)
    bttn_add_wind2.pack(side=RIGHT)

def ok_addBook(event):
    title = entries_add[add_book_field[0]].get()
    series = entries_add[add_book_field[1]].get()
    author = entries_add[add_book_field[2]].get()
    publisher = entries_add[add_book_field[3]].get()
    pages = entries_add[add_book_field[4]].get()
    comment = entries_add[add_book_field[5]].get()
    if (title in db['book_list']):
        title = title+' (авт. '+author.split()[-1]+')'
        no = 0
        title_cop = title+' (копия '+str(no)+')'
        while (title_cop in db['book_list']):
            no+=1
            title_cop = title+' (копия '+str(no)+')'
        title = title_cop
            
    db[title]=Book(title, series, author, publisher, pages, comment)
    book_list = db['book_list']
    book_list.append(title)
    db['book_list']=book_list
    add_wind.destroy()
    last_row = len(book_list)
    key = book_list[last_row-1]
    print_record(key,last_row)
    canva.config(scrollregion=(0,0,1,last_row*42))
    lab2.config(text = 'Всего книг: '+str(last_row))
            
    
def next_addBook(event):
    title = entries_add[add_book_field[0]].get()
    series = entries_add[add_book_field[1]].get()
    author = entries_add[add_book_field[2]].get()
    publisher = entries_add[add_book_field[3]].get()
    pages = entries_add[add_book_field[4]].get()
    comment = entries_add[add_book_field[5]].get()
    if (title in db['book_list']):
        title = title+' (авт. '+author.split()[-1]+')'
        no = 0
        title_cop = title+' (копия '+str(no)+')'
        while (title_cop in db['book_list']):
            no+=1
            title_cop = title+' (копия '+str(no)+')'
        title = title_cop
            
    db[title]=Book(title, series, author, publisher, pages, comment)
    book_list = db['book_list']
    book_list.append(title)
    db['book_list']=book_list
    last_row = len(book_list)
    key = book_list[last_row-1]
    print_record(key,last_row)
    canva.config(scrollregion=(0,0,1,last_row*42))
    lab2.config(text = 'Всего книг: '+str(last_row))
    entries_add[add_book_field[0]].delete(0,END)

############################################################


# Izmenenie knigi

#def changeBook(event): #There is no such book
    #

#def ok_changeBook(event): #change?
    #
    '''
    texties['Num 5'][1].config(state = NORMAL)
    texties['Num 5'][1].insert(END, str(num))
    texties['Num 5'][1].config(state = DISABLED)
    texties['Num 5'][3].config(state = NORMAL)
    texties['Num 5'][3].insert(END, 'Len of obj '+ str(len(db['num_list'])))
    texties['Num 5'][3].config(state = DISABLED)
    
    '''

#def next_changeBook(event):
    #

############################################################


# Udalenie knigi

def delBook(event): #There is no such book
    global del_wind
    del_wind = Toplevel()
    del_wind.geometry('320x135')
    del_wind.title('Удаление книги')
    del_lab = Label(del_wind, width=35, justify = CENTER, text='Введите название удаляемой книги, затем подтвердите удаление', font = 'Consolas 13', wraplength = 300)
    del_lab.pack()
    global del_txt
    del_txt = Text(del_wind, bd = 5, width=25, height = 2, font = 'Consolas 12', wrap=WORD)
    del_txt.pack()
    bttn_del0 = Button(del_wind, text='OK')
    bttn_del0.bind('<Button-1>', ok_delBook)
    bttn_del0.pack(side=RIGHT)
    bttn_del1 = Button(del_wind, text='Отмена', command = del_wind.destroy)
    bttn_del1.pack(side=LEFT)

def ok_delBook(event):
    title = del_txt.get('1.0', 'end-1c')
    if(title in db['book_list']):
        book_list = db['book_list']
        book_list.remove(title)
        db['book_list'] = book_list
        del db[title]
        del_wind.destroy()
        for wid in texties[title]:
            wid.destroy()
        del texties[title]

        for key in db['book_list']:
            for txt in texties[key]:
                txt.grid_forget()

        rown = 1 #row number
        for key in db['book_list']:# vyvod znachenij postrochnyj
            print_record(key, rown)
            rown+=1
        canva.config(scrollregion=(0,0,1,(rown-1)*42))
        lab2.config(text = 'Всего книг: '+str(rown-1))

############################################################
#                      MAIN - GUI
############################################################

if not(os.path.isfile('database_lib.dir')):# sozdanie
    db = shelve.open('database_lib')
    book_list = list()
    db['book_list'] = book_list
    db.close()

db = shelve.open('database_lib')
global texties #diction with Texts
texties = dict()
master = Tk()
master.title('HOME LIBerty')
fram0 = Frame(master, bg = 'white')
fram0.pack()
    
for (num, label) in enumerate(table_field):# Shapka tablicy
    lab0 = Label(fram0, width = label[0], justify = CENTER, text=label[1], font = 'Consolas 11', bg = 'white')
    lab0.grid(row=0, column=num, sticky = W)

############## CANVAS
canva = Canvas(fram0, bg = 'light grey')
table = Frame(canva, bg = 'white')

### inside of the table
rown = 1 #row number
for key in db['book_list']:# vyvod znachenij postrochnyj
    print_record(key, rown)
    rown+=1
###end of table
rown-=1
canva.create_window(0, 0, anchor = NW, window = table)    
yscroll = Scrollbar(fram0, orient = VERTICAL)
yscroll.grid(row = 1, column = 7, sticky = 'nsw')
yscroll.config(command = canva.yview)
canva.config(width=1022, height = 350,)
canva.config(yscrollcommand = yscroll.set)
canva.grid(row = 1, column=0, columnspan = 7, sticky = 'news')
canva.config(scrollregion=(0,0,1,rown*42))
    
############### END CANVAS
    
lab2 = Label(fram0, text = 'Total: '+str(rown), bg = 'white')
lab2.grid(row = 2, column = 0)
bttn_tab0 = Button(master, text='ADD Book')
bttn_tab0.bind('<Button-1>', addBook)
bttn_tab0.pack(side = LEFT)
bttn_tab1 = Button(master, text='Change')
#bttn_tab1.bind('<Button-1>', changeBook)
bttn_tab1.pack(side = LEFT)
bttn_tab2 = Button(master, text='DELETE')
bttn_tab2.bind('<Button-1>', delBook)
bttn_tab2.pack(side = LEFT)
bttn_tab3 = Button(master, text='QUIT', command = master.destroy)
bttn_tab3.pack(side = RIGHT)


master.mainloop()
##### END PROGRAMM
db.close()
