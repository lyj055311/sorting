class Document:
    def __init__(self,name):
        self.name=name
    def show(self):
        raise NotImplementedError("Subclasss must implement abstract method")
        #子类调用的时候直接报错，子类必须重新写
class Pdf(Document):
    pass
    def show(self):
        return "Show pdf contents!"
class Word(Document):
    def show(self):
        return "Show word contents!"
a=Pdf('联系方式.pdf')
b=Word('护士.docx')
for o in [a,b]:
    print(o.show())