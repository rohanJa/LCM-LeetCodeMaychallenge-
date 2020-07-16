class BaseClass:
    def fly(self):
        print('base class fly')        
    
    def swim1(self):
        print('base class swim')

class Sub_Class(BaseClass):
    def fly(self):
        print('Sub_Class fly')
    def swim(self):
        print('Sub_Class swim')

obj = BaseClass()
obj1 = Sub_Class()
obj1.fly()
obj1.swim1() #This will call the inherited class method.