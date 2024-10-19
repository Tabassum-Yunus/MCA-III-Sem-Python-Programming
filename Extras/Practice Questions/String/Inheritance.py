class Parent:
    def __init__(self, name):
        self.name = name
    def prin(self):
        print('Name:', self.name)

class Child(Parent):
    def __init__(self, name, age, occupation):
        super().__init__(name)
        self.age = age
        self.occupation = occupation

    def prin(self):
        super().prin()
        print(self.age, ' ',self.occupation)

p = Parent('Demo Parent name') 
p.prin()
c = Child('Chils name', 11, 'Student')
c.prin()


    
        
