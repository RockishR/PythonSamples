from itertools import permutations
from itertools import product
print(list(permutations([1,2,3,4,5,6], 2)).__len__())
print(list(product([1,2,3,4,5,6], repeat=2)))