def mostCommonOrder(l):
    return [ sl[0] for sl in  sorted( [(i,l.count(i)) for i in set(l)], key = lambda t:t[1], reverse=True )]

print(mostCommonOrder([11,11,11,2,33,33,33,33,2,1,5,6]))
