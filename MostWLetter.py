from collections import Counter
import re
from collections import OrderedDict
import string

def checkio(text: str) -> str:


    # to lower case
    # sort by most common occurance
    # get max occurance count
    # filter the remaining.. and store the items match the max
    # sort by alphabetical order
    # return the value by pop 
    #odict = OrderedDict(Counter(re.findall("[a-z]|[A-Z]", text.lower())).most_common(26))
    #max = next(iter(odict.items()))[1]
    #return dict(sorted(filter(lambda item: item[1] == max,odict.items()) ,key=lambda t: t[0],reverse=True)).popitem()[0][0]
    #text = text.lower()
    return max(string.ascii_lowercase, key=text.lower().count)



if __name__ == '__main__':
    print(max(['a','b','c','d']))
    #print("Example:")
    print(checkio(" bbb aaa cc dd"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")