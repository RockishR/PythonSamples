
ranks=[(1,10),(2,20),(3,30),(4,3)]
first,*rest = 1,2,3,4,5,6
print(first)
print(rest)

print(max(ranks,key=lambda t:t[1]))

print( "aaabcdef".count('a'))

print(max("abcedf",key="aaabbbcdef".count))

#TODO sdsds 
print("..............")
for i in range(5,10):
    print(i)

print("..............")

name="1122345"
ll = [(i,name.count(i)) for i in "0123456789"]
for i in ll:
    print(i[0],i[1])

p=0
l=[ sum([k for k in range(0,i)]) for i in range(1,5) ]
print(l)


print("-----------------")
l=[1,2,3,4,5,6,7,8,9,10]
#l="abcdefghij"
print(l[1::1])
print(l[1::-1])

print(l[5::-1])
print(l[5::-2])

print("********")

print(l)
print(l[0:5])
print(l[0:5:1])
print(l[0:5:2])

print(l[::-1]) # end to begin becasue order is reverse, increment is 1 
print(l[::-2]) # end to begin becasue order is reverse, increment is 2
print(l[10:0:-1])




