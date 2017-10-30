# FOOD and DRINK characteristics
healthy = ['fish','soup','carrot','green','nuts','apple','berries','grass','grits','liver']
junk = ['sausage','pork','cheese','cream','sweet','chips','preserves','jam','noodles','bacon']
callories = {'fish':5, 'beef':7, 'chicken':6, 'soup':7, 'carrot':3, 'sausage':6, 'cream':4, 'cheese':3, 'pork':6, 'green':4, 'egg':5, 'sweet':8, 'nuts':5, 'apple':3, 'berries':2, 'grass':3, 'grits':6, 'liver':6, 'chips':3, 'preserves':7, 'jam':5, 'puree':5, 'noodles':6, 'bacon':10}
drinks = {'water':7, 'milk':5, 'juice':5, 'kefir':6, 'soda':7, 'honey':10}

# DO_lists

do_feed = ['feed','Feed','give food','Give food','','','','','','']
do_drink = ['drink','Drink','give drink','Give drink','water','Water','','','','']
do_play = ['play','Play','joy','Joy','','','','','','']
do_clean = ['wash','Wash','clean','Clean','','','','','','']
do_sleep = ['give it some rest','rest','Rest','sleep','Sleep','let sleep','Let sleep','','','']
do_heal = ['heal','Heal','treat','Treat','cure','Cure','vet','Vet','','']

# Check functions

def check_max(val, num, max_val=100):
    if(val+num > max_val):
        val = max_val
    else:
        val +=num
    return val

def check_min(val, num, min_val = 0):
    if(val-num<min_val):
        val = min_val
    else:
        val-=num
    return val

# Obshie parametry v classe Critter

class Critter():
    age = 0
    name = 'none'
    health = 100
    joy = 50
    fullness = 50
    thirst = 50
    fatigue = 0
    cleanliness = 100

# Osoboe vzaimodejstvie dl'a kota

class Cat(Critter):
    __time = 0
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str("cat "+self.name)

    def feed(self, food):
        self.__time+=10
        self.fullness=check_max(self.fullness, callories[food])
        self.cleanliness=check_min(self.cleanliness, 5)
        self.fatigue=check_max(self.fatigue, 3)
        self.thirst = check_max(self.thirst,1)
        self.health = check_max(self.health,1)
        if(food in healthy):
            self.health = check_max(self.health,3)
            self.joy=check_min(self.joy,3)
        if(food in junk):
            self.health=check_min(self.health,3)
            self.thirst = check_max(self.thirst,2)
            self.joy = check_max(self.joy,5)

    def drinking(self, drink):
        self.__time+=5
        self.thirst = check_min(self.thirst,drinks[drink])
        self.fullness=check_max(self.fullness, 2)
        self.cleanliness=check_min(self.cleanliness, 3)
        self.fatigue=check_max(self.fatigue, 2)
        
    def play(self, game, win):
        self.__time+=20*game
        self.joy += game*10 + win*5
        self.fatigue = check_max(self.fatigue, game*10)
        self.cleanliness = check_min(self.cleanliness,game*5)
        self.fullness=check_min(self.fullness,game*7)
        self.thirst=check_max(self.thirst,game*4)
        if(self.joy>100):
            self.health =check_min(self.health,(self.joy-100)//2)
            self.fatigue = check_max(self.fatigue, (self.joy-100)//2)
            self.joy = 100
        
    def sleep(self, hours):
        self.__time+=60*hours
        self.fatigue = check_min(self.fatigue,hours*10)
        self.fullness = check_min(self.fullness,hours*7)
        self.thirst=check_max(self.thirst,hours*4)
        self.health=check_max(self.health,hours)
        self.joy=check_min(self.joy,hours*3)

    def clean(self,val):
        self.__time+=30
        self.cleanliness = check_max(self.cleanliness,val)
        self.joy=check_min(self.joy,10)
        self.fatigue = check_max(self.fatigue,10)
        self.health = check_max(self.health,4)

    def heal(self,val):
        self.__time+=60
        self.health = check_max(self.health,val)
        self.fatigue = check_max(self.fatigue,10)
        self.thirst=check_max(self.thirst,5)
        self.joy=check_min(self.joy,10)

    def timer(self):
        print('\n', end = ' ')
        if(self.__time//720 > 0):
            print('Days:', self.__time//720, end = ' ')
        print('Hours:',self.__time//60,"Minutes:",self.__time%60)
    
    def status(self):
        print('health: ', self.health,'joy: ',self.joy,'fatigue: ',self.fatigue,'\ncleanliness: ',self.cleanliness,'fullness: ',self.fullness,'thirst',self.thirst)

# Osoboe povedenie dl'a sobaki        
#class Dog(Critter):
    
    
    


