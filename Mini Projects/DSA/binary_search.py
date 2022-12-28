def binary_search(start,end,xlist,search):
    if start>end:
        return -1
    else:
        mid=(start+end)//2
        if xlist[mid]==search:
            return mid
        elif xlist[mid]>search:
            return binary_search(start,mid-1,xlist,search)
        else:
            return binary_search(mid+1,end,xlist,search)

length=int(input('Enter the length of the list: '))
xlist=[]
for i in range(length):
    number=int(input('Enter the number: '))
    xlist.append(number)
xlist=sorted(xlist)
print(xlist)
search=int(input('Enter the number to search: '))
location= binary_search(0,length-1,xlist,search)
if location==-1:
    print('The number is not in the list')
else:
    print('The number is at position: '+str(location))
