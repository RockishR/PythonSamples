def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    if( len(data) > 0):
        
        mi = min(data)
        ma = max(data)
        i  = mi
        t1 = mi
        t2 = mi
        res=[]
        while i < ma+1:
            if i+1 not in data:
                #print('####', i, t1,t2)
                #yield((t1,i))
                res.append(((t1,i)))
                while i+1 not in data and i < ma+1:
                    i=i+1
                t1=i+1
                t2=i+1
            else:
                t2 = i
            i = i+1         
        # your code here
        #yield(t1,t2)
    return None

if __name__ == '__main__':
    print(create_intervals([]))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    #assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')


