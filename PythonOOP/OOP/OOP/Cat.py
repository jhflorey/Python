class Cat(object):
    def __init__(self, name, color , type, age ):
        self.name = name
        self.color = color
        self.type = type
        self.age = age

    def display(self):
        print(("The cat name:  %s\n It's color: %s\n Belong to type: %s\n Age: %s\n ") % (self.name, self.color, self.type, self.age))
    def update_name(self, new_name):
        self.name = new_name
        return self

class myCAT(object):
    def __init__(self, names):
        self.names = names
        self.AllCat = []
    def add(self, cat):
        self.AllCat.append(cat)
        return self
    def display(self):
        for cat in self.AllCat:
            cat.display()
    def remove(self, cat_name):
        copy_cat = self.AllCat[:]
        self.AllCat.remove(cat_name)
        return self

# 4/28 gdhjfg

abc = Cat('Tottoro', 'brownlight', 'bigxu', 2)
#abc = Cat ('Hugo', 'Brow', 'Longxu', 3), ('Tottoro', 'brownlight', 'bigxu', 2)]
cat2 = Cat('Hugo', 'Brow', 'Longxu', 3)
mycat1 = myCAT('Hermes')
mycat1.add(abc)
mycat1.add(cat2)
mycat1.display()
#mycat1.remove(abc)
print("____")
#mycat1.display()
#mycat1.display()
#abc.name = 'Totto'
abc.update_name('Totto')
mycat1.display()