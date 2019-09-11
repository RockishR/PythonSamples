from collections import Counter
import re
from collections import OrderedDict
def abc():
    pass

def main():
    print("in Function main()...")

    str = "ABCDE"
    print(abc)
    print(abc())

    print(str)

    elements = [1,2,3,4,56,88]
    for x, y in zip(elements, elements[1:]):
        print(x,y)
    print("##########")

    s1 = "laABCD abc aaaaa b l l l l lll"
    #print(re.findall("[a-z]|[A-Z]", s1.lower()))
    #cdict1 = Counter(re.findall("[a-z]|[A-Z]", s1.lower()))
    #print(cdict1)
    #odict = OrderedDict(Counter(re.findall("[a-z]|[A-Z]", s1.lower())).most_common(26))
    #print(odict)
    #print("********", list(odict.values())[0]);
    #print("********", next(iter(odict.items()))[1]);

    #print(next(iter(odict)))
    #print(dict(map(lambda t: t==,odict))) 
    #print(odict)

    #zd = dict(filter(lambda item: item[1] == 8,odict.items()))
    #print("ZD:: ", zd)
    #  working --- print(dict(sorted(zd.items(),key=lambda t: t[0],reverse=True)).popitem()[0][0])
"""

Random Review (?)

import collections
import operator

def checkio(text: str) -> str:
    newText = ''.join(e for e in text if e.isalpha())
    newText = sorted(list(newText.lower()))
    newText = collections.Counter(newText)
    return max(newText.items(), key=operator.itemgetter(1))[0]

"""
    # to lower case
    # sort by most common occurance
    # get max occurance count
    # filter the remaining.. and store the items match the max
    # sort by alphabetical order
    # return the value by pop 
    odict = OrderedDict(Counter(re.findall("[a-z]|[A-Z]", s1.lower())).most_common(26))
    max = next(iter(odict.items()))[1]
    print(dict(sorted(filter(lambda item: item[1] == max,odict.items()) ,key=lambda t: t[0],reverse=True)).popitem()[0][0])
   
    #print(OrderedDict(sorted(Counter(re.findall("[a-z]|[A-Z]", s1.lower())).most_common(26),key = lambda t: t[0],reverse=True)).popitem()[0][0])


    result = [item for items, c in Counter(ini_list).most_common()  for item in [items] * c]

if __name__=="__main__":
    main();