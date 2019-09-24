def fun_one(fun):
    def wrapper():
        print("BEFORE  Call")
        fun()
        print("AFTER Call")
    return wrapper
    


@fun_one
def fun_two():
    print("from two")


