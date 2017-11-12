import shelve
import os
#from Objects_lib import *

#################

class Author():
    def __init__(self, name, comment = 'None'):
        auth_list.append(name)
        self.firstname = name[0:(len(name)-(len(name.split()[-1])+1))]
        self.secondname = name.split()[-1]
        self.comment = comment
        

class Book():
    def __init__(self, title, author = 'None', publish = 'None', comment = 'None'):
        book_list.append(title)
        self.title = title
        self.comment = comment
        if (author!=''):
            if not(author in auth_obj):            
                auth_obj[author] = Author(author)
            self.author = auth_obj[author]
        if(publish==''):
            if not(publish in publish_obj):
                publish_obj[publish] = Publisher(publish)
            self.publish = publish_obj[publish]


class Publisher():
    def __init__(self, publish, comment = 'None'):
        publish_list.append(publish)
        self.publish = publish
        self.comment = comment



#################
#           Proverka vvoda
def checking (var):
    try:
        var=int(var)
    except: TypeError
    return var


#           Proverka otveta da-net
def yes_no(answer):
    while(True):
        if(answer == 'Yes' or answer == 'Да' or answer == 'y' or answer == 'yes' or answer == 'Y'
           or answer == 'Ye' or answer == 'e' or answer == 'Eah' or answer == 'E' or answer == 'Yap'
           or answer == 'Канеш' or answer == 'канеш' or answer == 'угу' or answer == 'ага' or answer == 'ес'
           or answer=='Да!' or answer=='ДА' or answer=='!' or answer=='!!!' or answer=='--' or answer=='+'
           or answer=='ляляля' or answer=='Ляляля' or answer=='start' or answer=='давай' or answer=='Давай'):
            return 1
        elif(answer == 'No' or answer == 'Nea' or answer == 'Net' or answer == 'nea' or answer == 'no'
           or answer == 'net' or answer == 'Нет' or answer == 'нет' or answer == 'Неа' or answer == 'неа'
           or answer == 'неть' or answer == 'Неть' or answer == '-' or answer == 'ни в коем случае'
           or answer == 'уйди противный' or answer == 'Уйди, противный' or answer == 'Бебебе'
           or answer == 'N' or answer == 'n' or answer == '0' or answer=='нетушки' or answer=='н' or answer=='Н'
           or answer=='ненене' or answer=='Ненене' or answer=='НЕТ' or answer=='Надоело' or answer=='надоело'):
            return 0
        else:
            answer = input('Sorry, I don\'t understand. What would be your answer again?(Yes/No) ')

if not(os.path.isfile('database_lib.dir')):
    auth_list = list()
    auth_obj = dict()
    publish_list = list()
    publish_obj = dict()
    book_list = list()
    book_obj = dict()
    db = shelve.open('database_lib')
    db['auth_list'] = auth_list
    db['auth_obj']=auth_obj
    db['publish_list']=publish_list
    db['publish_obj']=publish_obj
    db['book_list']=book_list
    db['book_obj']=book_obj
    db.close()
db = shelve.open('database_lib')
auth_list = db['auth_list']
auth_obj = db['auth_obj']
publish_list = db['publish_list']
publish_obj = db['publish_obj']
book_list = db['book_list']
book_obj = db['book_obj']
db.close()

while(True):
    print('''
This is Home library.

1 - Add book
2 - Add author
3 - Add publisher
4 - Show all books
5 - Show all authors
6 - Show all publishers
0 - Exit
''')
    menu = checking(input('>>> '))
    if (menu == 0):
        db = shelve.open('database_lib')
        db['auth_list'] = auth_list
        db['auth_obj']=auth_obj
        db['publish_list']=publish_list
        db['publish_obj']=publish_obj
        db['book_list']=book_list
        db['book_obj']=book_obj
        db.close()
        print('Good bye!')
        break
    
    elif(menu == 1): #Add book
        title = input('Enter title ')
        author = input('Enter author ')
        publish = input('Enter publisher ')
        comment = 'None'
        if not(title in book_obj):
            book_obj[title]=Book(title,author,publish,comment)
            
    elif(menu == 2): #Add author
        author = input('Enter author ')
        if not(author in auth_obj):
            comment = 'None'
            auth_obj[author] = Author(author, comment)
            
    elif(menu == 3): #Add publisher
        publish = input('Enter publisher ')
        if not(publish in publish_obj):
            comment = input('Enter comment ')
            publish_obj[publish] = Publisher(publish, comment)
            
    elif(menu == 4): #Show all books
        print(book_list)
        
    elif(menu == 5): #Show all authors
        print(auth_list)
        
    elif(menu == 6): #Show all publishers
        print(publish_list)
        
    else:
        print('Wrong command!\n') 
    

