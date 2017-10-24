class Avto():
    wheels = 4
    fuel = "petrol"
    doors = 4
    brand = "none"
    
    def __str__(self):
        return str("Brand: "+self.brand+"\nUse "+self.fuel+"\nHas "+str(self.wheels)+" wheels and "+str(self.doors)+ " doors" )
        

class Sedan(Avto):
   
    def __init__(self, klass = "sedan", flap_top = "none", trunk = "yes"):
        self.klass = klass
        self.flap_top = flap_top
        self.trunk = trunk
        
    def __str__(self):
        return str("This is "+self.klass+"\nBrand: "+self.brand+"\nUse "+self.fuel+"\nHas "+str(self.wheels)+" wheels and "+str(self.doors)+ " doors\nFlap top: "+self.flap_top+"\nTrunk: "+self.trunk)

    def ch_klass(self, klass):
        self.klass = klass

        
class Gruz(Avto):
    health = 100
    cargo = 0
    def __init__(self, carrying = 1000, cargo_type = "none", ):
        self.carrying = int(carrying)
        self.cargo_type = cargo_type

    def __str__(self):
        
        return str("This is truck with "+str(self.carrying)+"kg carrying ability\nBrand: "+self.brand+"\nUse "+self.fuel+"\nHas "+str(self.wheels)+" wheels and "+str(self.doors)+ " doors\nCargo type is: "+self.cargo_type+"\nCargo is "+str(self.cargo)+"\nHealth is "+str(self.health))

    def ch_cargo_carry(self, cargo_type, carrying):
        self.carrying = int(carrying)
        self.cargo_type = cargo_type

    def add_cargo(self, cargo):
        self.cargo += int(cargo)
        if(cargo>100):
            self.health -=1

    def rem_cargo(self, cargo):
        self.cargo -= cargo
        if(cargo>100):
            self.health -=2

    

            
class Spectech(Avto):
    go = "stop"
    def __init__(self, spec_type = "tractor", mode = "manual", action = "none"):
        self.mode = mode
        self.action = action

    def __str__(self):
        return str("This is special auto - "+self.spec_type+"\nBrand: "+self.brand+"\nUse "+self.fuel+"\nHas "+str(self.wheels)+" wheels and "+str(self.doors)+ " doors\nAction:"+self.action+"\nMode of operation: "+self.mode+"\nActing at the moment: "+self.go)

    def ch_action(self, action):
        self.action = action

    def do(self, go = "start"):
        self.go = go

     
