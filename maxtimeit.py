from functools import reduce
from collections import Counter

l1 = [1,2,3,4,5,6,"ABC","Swamy","Name","zzz",77,8,9]*100000
#1
#print(max([i for i in [1,2,3,4,5,6,'ABC','Swamy','Name','zzz',77,8,9]*100000 if isinstance(i,int)]))

#2
#print(max(i for i in [1,2,3,4,5,6,'ABC','Swamy','Name','zzz',77,8,9]*100000 if isinstance(i,int)))

#3
#print(max(filter(lambda i: isinstance(i,int),[1,2,3,4,5,6,'ABC','Swamy','Name','zzz',77,8,9]*100000)))

#4
#print(reduce(lambda a,b: a if a>b else b,list(filter(lambda i: isinstance(i,int),[1,2,3,4,5,6,'ABC','Swamy','Name','zzz',77,8,9]*100000))))

l=[1,2,3,2,1,3,4,3,2,4,45,45,45,45,45,3,2,98]

print("-----------------------")
print(max(l,key=l.count))

print(Counter(l).most_common(1)[0][0])

print(sorted({k:l.count(k) for k in l}.items(),key=lambda kv: kv[1],reverse=True)[0][0] )


#print( sorted({i:l.count(i) for i in l}.items(), key=lambda a,b: a[1]>b[1]))
#print(memoryview("aaaaaaa"))

a=[(1,2),(22,33),(2,4)]
print(sorted(a,key=lambda x:x[1]))


