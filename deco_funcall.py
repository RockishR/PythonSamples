from deco_my1 import fun_one

def myprint(st):
    with open('abc.log','a') as ff:
        ff.write(st+'\n')
    print(st)

@fun_one
def fun_two():
    myprint("from two")



def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def greet(name):
    myprint(f"Hello {name}")
    return f"Hello {name}"

myprint(greet("Siddhi"))
