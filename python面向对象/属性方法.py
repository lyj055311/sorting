class Student:
    def __init__(self,name):
        self.name=name
    @property
    def fly(self):
        print(self.name,'is flying...')
s=Student('liu')
s.fly #不需要写fly(),因为fly已经变成属性
