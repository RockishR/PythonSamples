def flat(parentkey,d):
    res = {}
    for i in d.items():
        if isinstance(i[1],str):
            res[parentkey+i[0]]=i[1]
        elif len(i[1]) == 0:
            res[parentkey+i[0]]=''
        else:
            res = {**res, **flat(parentkey+i[0]+'/',i[1])}

    return res

def flatten(dictionary):
    # your code here
    res = flat("",dictionary)
    #print(dictionary)
    #print(res)
    return res

if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')