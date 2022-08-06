a=int(input('Enter a sequence of number to check pallindrome: '))
temp=a
reverse=0
while temp!=0:
    reverse=reverse*10
    reverse=reverse+temp%10
    temp=temp//10
if reverse==a:
    print('Pallindrome')    
else:  
    print('Not pallindrome')