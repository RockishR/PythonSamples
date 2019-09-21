import functools
import itertools
import collections

class base:
    def __init__(self,obj):
        self.__obj=obj
    def print_obj(self):
        print(self.__obj)


b = base(123)
b.print_obj()
b.__obj = "OUT123"
print(b.__obj)
b.print_obj()

print(dir(functools))
print("-------------------------")
print(dir(itertools))
print("-------------------------")
print(dir(collections))
print("-------------------------")