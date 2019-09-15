def check_connection(network, first, second):

    data =[['dr101','abc','qqqq']]
    for node in network:
        ar = node.split('-')
        s1 = [s for s in data if ar[0] in s]
        s2 = [s for s in data if ar[1] in s]
        print(s1,s2)
        data.remove(s1[0])
    return True or False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3")
    # == True, "Scout Brotherhood"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "super", "scout2") == True, "Super Scout"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "dr101", "sscout") == False, "I don't know any scouts."