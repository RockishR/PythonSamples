from itertools import cycle

def decode_amsco(message, key):
    kd = {}
    maind = {}
    max = len(str(key))
    kc = cycle(int(i)  for i in str(key))
    vc = cycle([1,2])
    
    f = 1
    ch = 0
    while ch < len(message):
        k = next(kc)
        v = next(vc)
        if ch+1 ==len(message):
            v = 1
        if k in kd:
            kd[k].append(v)
        else:
            kd[k]=[v]
        if f==max and max%2==0:
            f=0
            next(vc)
        f  += 1
        ch += v

    print(kd)
    mi = iter(message)
    for i in range (max):
        j = i+1
        for k in kd[j]:
            if k == 1:
                vl = [ next(mi) ]
            else:
                vl = [ next(mi)+next(mi) ]
            #print("#######",vl,j,k)
            if j in maind:
                maind[j].extend(vl)
            else:
                maind[j]= vl
    print(maind)

    for k in maind:
        maind[k] = maind[k][::-1]
    print(maind)

    kc = cycle(int(i)  for i in str(key))
    out = ''

    while(len(out)<len(message)):
        out += maind[next(kc)].pop()

    return out

if __name__ == '__main__':
    print(decode_amsco("oruoreemdstmioitlpslam", 4123))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco('hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"
