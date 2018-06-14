class MathDojo(object):
    def __init__(self):
        self.value = 0
    def add(self, *arg):
        a = sum(arg)
        self.value +=a
        return self
    def subtract(self, *arg):
        a = sum(arg)
        self.value -= a
        return self
    def result(self):
        return self.value

md = MathDojo()
print(md.add(2).add(2,5).subtract(3,2).result())


class MathDojo2(object):
    def __init__(self):
        self.value = 0

    def add(self, *arg):
        a = 0
        for i in arg:
            if type(i) is int:
                a += i
            elif type(i) is list or tuple:
                a += sum(i)
        print(a)
        self.value += a
        return self

    def subtract(self, *arg):
        a = 0
        for i in arg:
            if type(i) is int:
                a -= i
            elif type(i) is list or tuple:
                a -= sum(i)
        print(a)
        self.value -= a
        return self

    def result(self):
        return self.value

md2 = MathDojo2()
print(md2.add([1], 3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).result())
