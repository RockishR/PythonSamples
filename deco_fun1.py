
def one_fun():
    print("Line 1")
    print("line 2")
    return 100

def two_fun(fun):
    # business 1
    # business 2
    return fun()


fobj = one_fun

print(fobj, one_fun)

print(two_fun(fobj))
