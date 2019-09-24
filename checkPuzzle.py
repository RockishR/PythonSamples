import time
from copy import deepcopy
def wall_keeper(on_panels):
    wall = [ 0 for i in range(26)]
    for i in on_panels:
        wall[i] = 1
    data={1:[2,6], 2:[1,3,7], 3:[2,4,8], 4:[3,5,9], 5:[4,10],
            6:[1,7,11], 7:[2,6,8,12], 8:[3,7,9,13], 9:[4,8,10,14], 10:[5,9,15],
            11:[6,12,16], 12:[7,11,13,17], 13:[8,12,14,18], 14:[9,13,15,19], 15:[10,14,20],
            16:[11,17,21], 17:[12,16,18,22], 18:[13,17,19,23], 19:[14,18,20,24], 20:[15,19,25],
            21:[16,12], 22:[17,21,23], 23:[18,22,24], 24:[19,23,25], 25:[20,24]           
            }
    out=[]

    #print(wall)
    #print(data)
    states={i:[] for i in range(26)}
    
    while sum(wall) >0:
        for t in data.items():

            if(any(wall[v]==1 for v in t[1])):
                if wall not in states[t[0]]:
                    states[t[0]].append(deepcopy(wall))
                    #print('@!@!@!  ',sum(wall))
                        
                    out.append(t[0])
                    wall[t[0]] = abs(1-wall[t[0]])
                    for z in t[1]:
                        wall[z] = abs(1-wall[z])
                    # print(wall,t)
                    # print("#########  ", sum(wall), out)
                    # if sum(wall) < 3:
                    #     print("******* :: ", sum(wall))
                    #     time.sleep(0.1)
                #else:
                    # l = states[t[0]]
                    # l.remove(wall)
                    # print("Ecountered the previous state.. skipping..",t)
                    # print( sum([len(states[i]) for i in states] ))
                    # time.sleep(0.1)
                #time.sleep(0.2)
    print('INPUT ::', on_panels )
    print('WALL  ::', wall)
    print('OUTPUT len ', len(out))
        
    return out

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    from itertools import chain


    def checker(solution, on_panels):
        answer = solution(on_panels)
        wk_p = list((0, 1)[n in on_panels] for n in range(1, 26))
        p = list(wk_p[n: n+5] for n in range(0, 25, 5))
        for a in answer:
            r, c = (a-1) // 5, (a-1) % 5
            p[r][c] = 1 - p[r][c]
            if r+1 < 5:
                p[r+1][c] = 1 - p[r+1][c]
            if r-1 > -1:
                p[r-1][c] = 1 - p[r-1][c]
            if c+1 < len(p[0]):
                p[r][c+1] = 1 - p[r][c+1]
            if c-1 > -1:
                p[r][c-1] = 1 - p[r][c-1]

        print('SUM  :',sum(chain(*p)) )
        print('P :: ', p, len(answer))
        return sum(chain(*p)) == 0

    assert checker(wall_keeper, [1,2, 6 ]), 'basic'
    assert checker(wall_keeper, [5, 7, 13, 14, 18]), 'basic 222'
    assert checker(wall_keeper, list(range(1, 26))), 'all_lights'
    print('---   DONE   ---')
