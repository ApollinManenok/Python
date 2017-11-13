import shelve

class Number():
    def __init__(self, num):
        self.title = str(num)
        self.author = 'author '+str(num)
        self.publisher = 'publisher '+str(num)
        self.amount = int(num)

if __name__ == '__main__':
        
    num_list = list()
    db = shelve.open('database_lib')
    for num in range (0,25):
        db['Num '+str(num)]=Number(num)
        num_list.append('Num '+str(num))
    db['num_list']=num_list
    db.close()
