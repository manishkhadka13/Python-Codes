import os
# number=int(input("Enter a number to check armstrong number: "))
number=int(input("Enter a number to check armstrong number: "))
num=str(number)
sum=0
for i in num:
    sum+=int(i)**3
if sum==number:
    print("The number is armstrong number") 
else:
    print("The number is not armstrong number")
# sum=0
# temp=number
# while temp>0:
#     digit=temp%10
#     sum+=digit**3
#     temp//=10
# if number==sum:
#     print(number, "is an armstrong number")
# else:
#     print(number, "is not an armstrong number")
