from itertools import product
def probability(dice_number, sides, target):

    numa=0
    denom=pow(sides,dice_number)
    l=[]
    for i in range(1,sides+1):
        l.append(i)
    print(l)
    print("--------")
    #print(list(product(l, repeat=dice_number)))
    for i in product(l, repeat=dice_number):
        if(sum(i)==target):
            numa+=1
            #print(i)
    print(denom)
    print(numa)
    return float("{0:.4f}".format(numa/denom)) 

if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
    print(probability(10, 10, 50))    
    # assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    # assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    # assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    # assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    # assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    # assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    # assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"