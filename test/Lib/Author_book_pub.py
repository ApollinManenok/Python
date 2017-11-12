class Author():
    id_author = 0
    def __init__(self, firstname, secondname, birth = None, death = None, comment = None):
        self.id_author+=1
        self.firstname = firstname
        self.secondname = secondname
        self.birth = birth
        self.death = death
        self.comment = comment
        
    def __str__(self):
        return('Author '+self.firstname+' '+self.secondname)

    


class Book():
    id_book = 0
    def __init__(self, title, author = None, date = None, publisher = None, comment = None):
        self.id_book+=1
        self.title = title
        self.author = author
        self.date = date
        self.publisher = publisher
        self.comment = comment

    def __str__(self):
        return('Book title "'+self.title+'". '+str(self.author)+'.')


class Publisher():
    id_publisher = 0
    def __init__(self, name, adress = None):
        self.id_publisher += 1
        self.name = name
        self.adress = adress



    
