class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__life_val=100 #私有变量 私有属性
    def get_life_val(self):
        print('生命值还有%s'%self.__life_val)
        return self.__life_val
    def __breath(self):
        print('%s is breathing...'%self.name)
    def got_attack(self):
        self.__life_val-=20
        print('被攻击了，生命值减了20')
        self.__breath()
        return self.__life_val

a=Person('刘一骏',22)
a.got_attack()
a.get_life_val()