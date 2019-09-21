from functools  import reduce
print("{0:b}".format(1022).count('1'))

n=54670
rn=0
while n>0:
    rn = (rn*10)+n%10
    n=n//10
print(rn)

n=54670
print(int(str(n)[::-1]))
print(int( ''.join(reversed(str(n)))))
print(reduce( lambda x,y: (x*10)+y, [int(i) for i in str(n)][::-1] ))
print(int( ''.join( [i for i in str(n)][::-1])))
print(sum([t[0]*t[1] for t in  zip([int(i) for i in str(n)][::-1],[10000,1000,100,10,1])]))
print(sum([t[0]*t[1] for t in  zip([int(i) for i in str(n)][::-1],[10**i for i in range(len(str(n)))][::-1])]))

print(bin(8))