def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    l=[i for j,i in enumerate(array) if(j%2==0)]
    print(array)
    print(l)
    print(l[:-1])
    print (array.pop())
    return sum([i for j,i in enumerate(array) if(j%2==0)])* (array[-1] if len(array)>0 else 1)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
