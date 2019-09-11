from functools import reduce

l=["abc","def","ghi","jkl","mno","pqrs"]
l1=["abc","xyz"]
print(any(item in l for item in l1))
print(all(item in l for item in l1))
print(set(l)-set(l1))
print(l+l1) # - operation is not supported in list

#  ^ XOR on set only
print(set(l)^set(l1))


