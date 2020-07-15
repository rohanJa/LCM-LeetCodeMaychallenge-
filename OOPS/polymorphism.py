class BaseClass:
    def fly(self):
        print('base class fly')        
    
    def swim(self):
        print('base class swim')

class Sub_Class(BaseClass):
    def fly(self):
        super()
        print('Sub_Class fly')
    def swim(self):
        print('Sub_Class swim')

obj = BaseClass()
obj1 = Sub_Class()
obj1.fly()