class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=Person('liu',33)

a=getattr(p,'age')

if not hasattr(p,'sex'):
    setattr(p,'sex','男')

delattr(p,'age')