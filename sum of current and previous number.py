previous_num=0
n=int(input("Enter the number of terms: "))
for i in range(1,n+1):
    sum=previous_num+i
    print('Current number: ',i,'Previous number: ',previous_num,'Sum: ',sum)
    previous_num=i