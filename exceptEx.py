from MySqlTest import mycursor
try:
    a=0/0
    print(a)
except NameError as ne:
    print('Name Error',ne)
except Exception as ex:
    print(ex)
finally:
    print('Finally Block')

print([['!!Welcome!!']]*2)
l = [1,2,3,4,5]
print(l[len(l)-1])
print(l[-0])
i = 10
j = -i
print(i,j)

mycursor.execute("show tables")

for x in mycursor:
  print(x)
