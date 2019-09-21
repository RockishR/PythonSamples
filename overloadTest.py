class Parent:
    def add(self,a):
        print("PARENT:: ",a)
class Child(Parent):
#    def add(self,a):
#        print("CHILD:: ",a)
    def add(self,a,b):
        print("CHILD:: ",a,b)


p = Parent()
p.add(1)

c = Child()
### fails c.add(2)
c.add(5,7)
def f1(a):
    print("f1  ::",a)
def f1(a,b):
    print("f1 a b  ::",a,b)
def f1(a,b,c):
    print("f1 a b c ::",a,b,c)
    
def f1(a):
    print("f1  ::",a)


f1(1)
#f1(2,2,66)
