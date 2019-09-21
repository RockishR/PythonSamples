def is_stressful(subj):
    """
        recoognise stressful subject
    """
    print('-----------')
    print(subj)
    if(subj.endswith('!!!')): 
        return True
    subj=subj.replace('-','')
    subj=subj.replace('!','')
    subj=subj.replace('.','')
    reda=['A','S','P','H','E','L','P','U','R','G','E','N','T']
    redList=['ASAP', 'URGENT','HELP']
    subj=subj.upper()
    for a in reda:
        while True:
            plen = len(subj)
            print(subj,a+a)
            subj=subj.replace(a+a,a)
            print(subj)
            if(plen == len(subj)):
                break
    print(subj)
    return True if (any([subj.find(i)>=0 for i in redList])) else False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("HHHEEELLLPPPP!!!!!") == True, "!!!!!!!"
    #assert is_stressful("HHHEEELLLPPPP") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    is_stressful('HI HOW ARE YOU?')
    print('Done! Go Check it!')



# integers
a = 10
b = 20
c = a


print(id(a))
print(id(b))    
print(id(c))    
print(id(10))    