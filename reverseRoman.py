sd={'CM':900,'XC':90,'IX':9,'CD':400,'XL':40,'IV':4,'I':1,'V':5,
    'X':10,'L':50,'C':100,'D':500,'M':1000}
print(sd)

def reverse_roman(roman_string):
    '''
    Test method.. 1234
    123456
    zxzxzxzx
    '''
    
    #replace this for solution
    print(dir(list))
    num=0;
    while len(roman_string)>0:
        cs = roman_string[0:2] if len(roman_string)>1 else roman_string[0]
        cs1= roman_string[0]
        if cs in sd:
            num +=sd[cs]
            roman_string=roman_string[len(cs):]
        else:
            num +=sd[cs1]
            roman_string=roman_string[len(cs1):]         

    return num

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    print(reverse_roman.__doc__)

    print(reverse_roman('DLXXI'))
    assert reverse_roman('VI') == 6, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');