### Содержит объекты Book (Книга), Author (Автор) и Publisher (Издательство).

class Author():
    def __init__(self, name, comment = None):
        author_list.append(name)
        self.firstname = name[0:(len(name)-(len(name.split()[-1])+1))]
        self.secondname = name.split()[-1]
        self.comment = comment
        

class Book():
    def __init__(self, title, series, author, publisher, pages, comment):
        self.title = title
        self.series = series
        self.comment = comment
        self.author = author
        self.publisher = publisher
        if not(pages == ''):
            self.pages = int(pages)
        else:
            self.pages = 0


class Publisher():
    def __init__(self, publish, comment = None):
        publish_list.append(publish)
        self.publish = publish
        self.comment = comment
