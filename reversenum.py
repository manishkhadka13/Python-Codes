n=int(input('Enter the number tor reverse: '))
print('The number before reversing: ',n)
reverse=0
while n!=0:
    reverse=reverse*10
    reverse=reverse+n%10
    n=n//10 
print('The number after reversing: ',reverse)