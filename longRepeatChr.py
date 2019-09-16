def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    # your code here
    ulist = []
    st = ''
    for c in line:
        if c not in st:
            st += c
        else:
            ulist.append(st)
            st = st[st.find(c)+1:]+c
            #print("###",st,c, ulist)
    else:
        ulist.append(st)
    #print(line)
    #print(ulist)
    return sorted(ulist,key= lambda i: len(i), reverse=True)[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')