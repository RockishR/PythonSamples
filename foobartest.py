def foo(arg=[]):
    # if(len(arg)==0):
    #     arg=[]
    arg.append(1)
    return arg
print(foo([7,8,9]))
print(foo())
print(foo())
print(foo([7,8,9]))
print(dir(foo))
print(foo.__getattribute__)

print(foo.__dict__)
# print(foo.__get__(arg))

class Te:
    cv=[]
    def __init__(self,ov):
        self.ov=ov
    def prin(self):
        print(" CV :",self.cv)
        print(" OV :",self.ov)
        print('--------------',__name__)

t1 =Te(44)
t2 =Te(55)

t1.prin()
t2.prin()

# t1.cv.append(1)
# t1.cv.append(2)
# t1.cv.append(3)

t1.cv=[1,2,3]

t1.prin()
t2.prin()

