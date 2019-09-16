def next_feb():
    p1=0
    p2=1
    for i in range(5000):
        yield(p2)
        p1,p2 = p2,p1+p2

def checkio(opacity):
    age = 0
    io = 10000
    i = iter(next_feb())
    feb = next(i)
    feb = next(i)
    if io <= opacity:
        return age
    
    for r in range (1,5000):
        print('AGE  ::', age, opacity)
        if r >= 5000:
            return 5000

        if feb != r:
            io += 1
        else:
            io -= feb
            feb = next(i)
        if( io == opacity):
            return r

    return r

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':


    print(checkio(9990))    
    # assert checkio(10000) == 0, "Newborn"
    # assert checkio(9999) == 1, "1 year"
    # assert checkio(9997) == 2, "2 years"
    # assert checkio(9994) == 3, "3 years"
    # assert checkio(9995) == 4, "4 years"
    #assert checkio(9990) == 5, "5 years"

# For example:
# A newborn ghost -- 10000 units of opacity.
# 1 year -- 10000 - 1 = 9999 (1 is a Fibonacci number).
# 2 year -- 9999 - 2 = 9997 (2 is a Fibonacci number).
# 3 year -- 9997 - 3 = 9994 (3 is a Fibonacci number).
# 4 year -- 9994 + 1 = 9995 (4 is not a Fibonacci number).
# 5 year -- 9995 - 5 = 9990 (5 is a Fibonacci number).
