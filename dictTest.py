from collections import OrderedDict
from itertools import chain

dictOfName = {
   7 : 'sam',
   8: 'john',
   9: 'mathew',
   10: 'riti',
   11 : 'aadi',
   12 : 'sachin'
}
dictOfNames = OrderedDict(dictOfName)
# Filter dictionary by keeping elements whose values are string of length 6
newDict = dict(filter(lambda elem: len(elem[1]) == 6,dictOfNames.items()))
print('Filtered Dictionary : ')
print(newDict)

d2 = { "d222":222, "d2222":2222}
d3 = { "d333":333, "d3333":3333}

print({**d2,**d3,**newDict})
print({ i:j for i,j in chain(d2.items(),d3.items(),newDict.items())})


