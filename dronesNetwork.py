def check_connection(network, first, second):

    data =[]
    for node in network:
        ar = node.split('-')
        s1 = [s for s in data if ar[0] in s]
        s2 = [s for s in data if ar[1] in s]
        
        print(s1,'###',s2)
        if(len(s1) == 0 and len(s2) ==0):
            data.append([ar[0],ar[1]])
        elif len(s1) == 0 and len(s2) >0:
            s2[0].append(ar[0])
        else:
            s1[0].append(ar[1])
            
        print(data)

        l1 = sum([l for l in data if first in l ],[])
        l2 = sum([l for l in data if second in l],[])
        print(l1)

    return len(set(l1) & set(l2)) > 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2")
    # == True, "Scout Brotherhood"
    print("---------------------------")
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."

    check_connection(("nikola-robin","batman-nwing","mr99-batman",
        "mr99-robin","dr101-out00","out00-nwing",)
        ,"dr101","mr99")
    print("DONE")