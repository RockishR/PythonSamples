def count_consecutive_summers(num):
    # your code here

    print("============")
    cnt=0
    for i in range(1,int(num/2+2)):
        sum=0
        for j in range(i,int(num/2+2)):
            sum+=j
            #print(j,end=" ")
            if(sum==num):
                cnt+=1
                print("****",i,j,sum)
                break
            if(sum>num):
                break
    return cnt+1;

if __name__ == '__main__':
    print("Example:")
    l=[1,2,34]
    print(count_consecutive_summers(99))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert count_consecutive_summers(42) == 4
    #assert count_consecutive_summers(99) == 6
    #assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
