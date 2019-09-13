FIRST_TEN = ["","one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["", "","twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):

    if(number<20):
        return FIRST_TEN[number]
    res=''

    if(number>=100):
        res=FIRST_TEN[abs(int(number/100))]+" "+HUNDRED;
    
    number = number % 100

    if(number in range(11,20)):
        res+=" "+FIRST_TEN[number]
    else:    
        res += " " + OTHER_TENS[abs(int(number/10))]
        res += " " + FIRST_TEN[number%10]
        
    return res.replace("  "," ").strip()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    print(checkio(23))

    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')