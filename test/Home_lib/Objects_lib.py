### Содержит объекты Book (Книга), Author (Автор) и Publisher (Издательство).
from Libert import author_list, auth_obj, publish_list, publish_obj, book_list, book_obj


class Author():
    def __init__(self, name, comment = None):
        author_list.append(name)
        self.firstname = name[0:(len(name)-(len(name.split()[-1])+1))]
        self.secondname = name.split()[-1]
        self.comment = comment
        

class Book():
    def __init__(self, title, author = None, publish = None, comment = None):
        book_list.append(title)
        self.title = title
        self.comment = comment
        if not(author in author_list):            
            auth_obj[author] = Author(author)
        self.author = auth_obj[author]
        if not(publish in publish_list):
            publish_obj[publish] = Publisher(publish)
        self.publish = publish_obj[publish]


class Publisher():
    def __init__(self, publish, comment = None):
        publish_list.append(publish)
        self.publish = publish
        self.comment = comment
