from collections import Counter
from itertools import chain,groupby
#from iteration_utilities import deepflatten
import string 
from functools import reduce

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for a1,b1 in zip(a,b):
    print(a1,b1,end='#')


print(a[0:])
print(a[190:-200])
print("#######")
print(list(set(a)))
print([item for item in {i:a1 for i,a1 in enumerate(a)  if a1 not in a[:i] }.values()])
print([a1 for i,a1 in enumerate(a)  if a1 not in a[:i]])

print(a)
print(b)
print([a1 for a1 in set(a) if(b.__contains__(a1))] )

lz = [1,2,3,[4,5,6],7,8]
print(lz)
print(isinstance(lz,list))
print([l1 for l1 in lz  if(isinstance(l1,list) == False)  ])

print("------------")
#print([ [ l2 for l2 in l1 if isinstance(l1,list)==True ]  for l1 in lz ])

a = [[1, 2, 0], [5, 6, 0], [0, 3, 5]]
final = [[ "zero" if(k==0) else "odd" if (k %2 != 0 and k != 0) else "even" for k in j] for j in a ]

print(final)

#print([l1 for l in lz  for l1 in enumerate(l) ])
print("#######")
l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]

print([l2 for l1 in l  for l2 in l1 if (isinstance(l1,list)==True)  ] )


lll =[k**k for i in range(1,10) if i%2 == 0   for k in range(i)]

print(lll)

final=[1,2,3,4,5,6,7,8,9]
print(final)
print ([["odd","even"][i%2!=1] for i in final])


dup = [1,2,1,2,3,6,4,4,4,4]
cntr = Counter(dup)
print([ k1  for k1 in dup  if cntr[k1]>1 ] )

fq= [4, 6, 2, 2, 6, 4, 4, 4]
print(fq)
print([k for k,v in Counter(fq).most_common() for i in range(v)])


def flat(li,out):
    #print("Flat -- ",li)
    if isinstance(li,list) == True:
        for i in li:
            flat(i,out)
    else:
        out.append(li)
        
nfl=[1,1,1,[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]
#print(list(chain.from_iterable(nfl)))
#print(list(deepflatten(nfl)))
out=[]
flat(nfl,out)
print(nfl)
print(out)

st='sdsffffsehhhhjkkkk'

for k, g in groupby(st):
    print(k,''.join(g))

print(len(max([''.join(g) for k,g in groupby(st)],key= lambda l: len(l))))

print("#######")
ll=[[1,2,3,5,5],8]
print(-1 if len(ll[0])<ll[1] else pow(ll[0][ll[1]],ll[1]) )
print("########")
ar = "07:30".split(':')
print( "Error" if (int(ar[0])>=18 or int(ar[0])<=6) else  str(( (int(ar[0])-6)*60 + int(ar[1]))*(15/60)).rstrip('0').rstrip('.') )

x = "Error" if (int(ar[0])>=18 or int(ar[0])<=6) else  str( ((int(ar[0])-6)*60 + int(ar[1]))*(15/60)).rstrip('0').rstrip('.') 

if x.find("rror")>0:
    x=x
elif x.find('.')>0:
    x=float(x) 
else:
    x=int(x)

print(type(x))
#assert x == 15
print(x)

bird = "hoooowe yyyooouuu duoooiiine"
bird = "sooooso aaaaaaaaa"

gg = groupby(bird)
out=[]
vo=['a','e','i','o','u','y']
prevC = False
for k,v in gg:
    #print(k,"".join(v))
    if(k ==' '):
        print("SPACE")
        out.append(k)
        prevC=False
        continue
    print('NOTSPACE')
    if(k not in vo):
        #Consonant
        out.append(k)
        prevC = True
    else:
        #Vowels flow
        st = "".join(v)
        print("VOWELS FLOW:",k,st)
        if(prevC):
            #discard one vowel
            print(prevC,st,"####*")
            st=st[1:]
            print(st)
        prevC=False
        if(len(st)>1):
            #out.append(st[0])
            out.extend([st[0] for i in range(int(len(st)/3)) ])
            print("LEN::",len(st))    
print(bird)   
print(''.join(out))

board=[[0 for i in range(8)]*8]
print(board)

n=123405
print(reduce((lambda x,y: x*y), [int(c) for c in str(n) if c != '0' ]))


ll = ["abc","pqr","xyz"]
print(ll)
gen_upp_rev=(name[::-1] for name in (name.upper() for name in ll))
print(gen_upp_rev)
print(list(gen_upp_rev))
gen_upp_rev2=(name2.upper()[::-1] for name2 in ll  )
print(list(gen_upp_rev2))


# Fibonacci using generator exp.

def gen_fib(n):
    p1=0
    p2=1
    for i in range(n):
        print(p1,p2)
        yield(p2)
        p1,p2=p2,p1+p2

print(list(gen_fib(10)))        