def total_cost(calls):
    d={}
    for c in calls:
        ca=c.split(' ')
        if ca[0] not in d:
            d[ca[0]]=[]
        d[ca[0]].append(int(ca[2]))
    print(d)
    coins=0
    for i in d.items():
        mins=0
        for s in i[1]:
            mins += ((s//60) + (1 if s%60>0 else 0))
        print(mins)
        coins += (100+ ((mins-100) *2)) if (mins > 100) else mins    
    return coins

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")))

    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"