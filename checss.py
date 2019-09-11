import string
alph="zabcdefghi"
data={"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
#data={"b4", "c4", "d4", "e4", "f4", "g4", "e5"}
print( sum( [ 1 for i in data if( chr(ord(i[0])-1)+str(int(i[1])-1)  in data or chr(ord(i[0])+1)+str(int(i[1])-1) in data) ]  ) )

print(chr(ord('b')-1))

#print(alph[alph.find('b')-1])
print ('b')


data = [   "X.O",
    "XX.",
    "XOO"]
data=["OO.",
        "XOX",
        "XOX"] 
print(data)
mat =[]
mat.append((data[0][0],data[0][1],data[0][2]))
mat.append((data[1][0],data[1][1],data[1][2]))
mat.append((data[2][0],data[2][1],data[2][2]))
mat.append((data[0][0],data[1][0],data[2][0]))
mat.append((data[0][1],data[1][1],data[2][1]))
mat.append((data[0][2],data[1][2],data[2][2]))
mat.append((data[0][0],data[1][1],data[2][2]))
mat.append((data[0][2],data[1][1],data[2][0]))

print(mat)
if(('X','X','X') in mat):
    print('X')
elif(('O','O','O') in mat):
    print('O')
else:
    print('.')

print(list(zip(*data)))

print(list(map(''.join, zip(*data))))

print("******************")
game_result = data
sample = "".join(game_result)
print(type(sample[1:19:3]))
data = game_result + [sample[i:9:3] for i in range(3)] + [sample[0:9:4], sample[2:8:2]]
print(data)
print(string.ascii_uppercase[1:2:3])
