# -*- coding: utf-8 -*-
#import collections
#my_dict = collections.OrderedDict()

def varargs(arg1, *args):
    print("Got " +arg1+" and "+" , ".join(args))
varargs("one")
varargs("one","two")
varargs("one","two","three")

def define(apple, tomato, *arg, **kwarg):
    print("This is the first parameter %s " % apple)
    print("This is the second parameter %s " % tomato)
    print(arg)
    print(kwarg)
    #my_dict['name'] =name
    #my_dict['age'] =age
    #print(my_dict)
#define(1,2, name='Jessica', age=12)
define(1,2, name="Jessica", age=20)
