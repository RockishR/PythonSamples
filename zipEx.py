from itertools import cycle

d1={"abc":111,"abd":222,"abz":333}
d2={"xxx":555,"xx5":666}


print([(z,a) for z,a in zip(d1,d2)])

d = {'a0': [1, 2, 3], 'a1': [4, 5, 6],'z':[7,8,9]}
print([i for i in zip(*d.values())])

l1=[1,1,1,2,3,4,5,6]
l2=['a','b','c','d']
print([i for i in zip(l1,cycle(l2))])


print("ABC".join(l2))
st='This is test mag'
print(''.join(st.split(' ')))
print("--------- REV ----------")
l1.reverse()
print(l1)
l1.remove(2)
del(l1[0])
l1.reverse()
print(l1)
