class Dog:
    def sound(self):
        print('汪汪汪。。。。')
class Cat:
    def sound(self):
        print('喵喵喵。。。。')
def make_sound(obj):
    '''统一调用接口'''
    obj.sound()
d=Dog()
c=Cat()
make_sound(d)
make_sound(c)