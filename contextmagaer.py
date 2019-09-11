from contextlib import contextmanager

@contextmanager
def cont_ex(obj):

    try:
        obj.prop += 2
        yield
    finally:
        obj.prop -= 2

class somec():
    def __init__(self):
        self.prop=33

obj=somec()
print("**********")
print(obj.prop)
with cont_ex(obj):
        print(obj.prop)
        print(obj.prop)
print(obj.prop)
        