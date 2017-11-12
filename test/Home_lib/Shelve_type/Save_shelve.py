import shelve
from Objects_lib import *

db = shelve.open('database_lib')
db['author_list'] = author_list
db['auth_obj']=auth_obj
db['publish_list']=publish_list
db['publish_obj']=publish_obj
db['book_list']=book_list
db['book_obj']=book_obj
db.close()
