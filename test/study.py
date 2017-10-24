#Study

class People():
    name = "None"
    surname = "None"
    age = "None"


class Teacher(People):
    def __init__(self, name, surname, age, knowledge, know_type):
        self.name = name
        self.surname = surname
        self.age = int(age)
        self.knowledge = int(knowledge)
        self.know_type = know_type

    def __str__(self):
        return str("Hello, my name is "+self.name+" "+self.surname+". I know "+self.know_type+" this much: "+str(self.knowledge))

    def teach(self, obj, time):
        if(obj.know_type == self.know_type):
            print("I can teach "+obj.name)
            obj.knowledge += self.knowledge/100*int(time)
            self.knowledge -= int(time)/100
        else:
            print("I can't teach "+obj.name)

    def upgrade(self, knowledge):
        self.knowledge += int(knowledge)


class Student(People):
    def __init__(self, name, surname, age, knowledge, know_type):
        self.name = name
        self.surname = surname
        self.age = int(age)
        self.knowledge = int(knowledge)
        self.know_type = know_type

    def __str__(self):
        return str("Hello, my name is "+self.name+" "+self.surname+". I know "+self.know_type+" this much "+str(self.knowledge))

    def take_know(self, obj, time):
        obj.teach(self, time)
        
        
