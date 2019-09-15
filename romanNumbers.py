
sd={900:'CM',90:'XC',9:'IX',400:'CD',40:'XL',4:'IV',1:'I',5:'V',
    10:'X',50:'L',100:'C',500:'D',1000:'M',0:''}
print(sd)
def aaa(n):
    res=''
    for i in [1000,500,100,50,10,5,1]:
        if i>n:
            continue
        if n in sd:
            res += sd[n]
            break
        if str(n)[0] in ['9','4']:
            if i in [500,50,5]:
                continue;
            print('nnnnn', n, i)
            x=int(str(n)[0]) * (10**(len(str(n))-1))
            print('XXXXXX:',x)
            res += sd[x]
            print('RES   ',res)
 
        else:
            for j in range(int(n/i)):
                res += sd[i]
        n = n%i

    return res

print(aaa(571))