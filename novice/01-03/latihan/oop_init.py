class Person:
    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print('Hai Gan, nama saya', self.name)


p = Person('Azizkyaaa')
p.say_hi()
#The previous 2 lines can also be written as 
#person('Swaroop').say_hi()