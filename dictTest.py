from collections import OrderedDict

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
