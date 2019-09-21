MORSE = {'a': '.-',    'b': '-...',  'c': '-.-.',
         'd': '-..',   'e': '.',     'f': '..-.',
         'g': '--.',   'h': '....',  'i': '..',
         'j': '.---',  'k': '-.-',   'l': '.-..',
         'm': '--',    'n': '-.',    'o': '---',
         'p': '.--.',  'q': '--.-',  'r': '.-.',
         's': '...',   't': '-',     'u': '..-',
         'v': '...-',  'w': '.--',   'x': '-..-',
         'y': '-.--',  'z': '--..',  '0': '-----',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.'
        }

def morse_encoder(text):
    #replace this for solution
    return  ''.join([ MORSE[ch]+' ' if ch!=' ' else '  ' for ch in text.lower()]).strip()
    #list1 = ['foo', 'bar']
    #list2 = ['-ness', '-ity']
    #return ([str1+str2 for str1 in list1 for str2 in str1])
if __name__ == '__main__':
    print("Example:")
    print(morse_encoder('some text'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_encoder("some text") == "... --- -- .   - . -..- -"
    assert morse_encoder("2018") == "..--- ----- .---- ---.."
    assert morse_encoder("It was a good day") == ".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"
    print("Coding complete? Click 'Check' to earn cool rewards!")
