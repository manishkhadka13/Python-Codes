num=[int(i) for i in input()[1:-1].split(',')]
target=int(input())
def twosum():
    for i in range(0,len(num)-1):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==target:
                return([i,j])
print(twosum())
