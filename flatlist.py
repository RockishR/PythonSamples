print("#######")
l = [[1, 2, 3], [4, 5, 6], [7], [8, 9],11,22,33,44]

print(sum([l1 if (isinstance(l1,list)==True)  else [l1] for l1 in l],[]) )

l = [(1, 2, 3), 'abc',(4, 5, 6), 7,44]

print(sum([l1 if (isinstance(l1,tuple)==True)  else (l1,) for l1 in l],() ))



# print(sum([[l1 if (isinstance(l1,list)==True) else l1] for l1 in l],[])  )

# print(sum(l,[]))
