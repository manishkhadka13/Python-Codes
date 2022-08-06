import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
def swap(A, i, j):
    A[i], A[j] = A[j], A[i]
    return A
def merge_sort(array,l,r):
    if(r<=l):
        return
    elif(l<r):
        mid=(l+r)//2
        yield from merge_sort(array,l,mid)
        yield from merge_sort(array,mid+1,r)
        yield from merge(array,l,mid,r)
        yield array
def merge(array,l,mid,r):
    new=[]
    i=l
    j=mid+1
    while(i<=mid and j<=r):
        if(array[i]<array[j]):
            new.append(array[i])
            i+=1
        else:
            new.append(array[j])
            j+=1
    if(i>mid):
            while(j<=r):
                new.append(array[j])
                j+=1
    else:
            while(i<=mid):
                new.append(array[i])
                i+=1
    for i,val in enumerate(new):
            array[l+i]=val
            yield array
def bubble_sort(array):
    if(len(array)==1):
        return
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if(array[j]>array[j+1]):
                array=swap(array,j,j+1)
                yield array
    yield array   
def selection_sort(array):
    if(len(array)==1):
        return
    for i in range(len(array)-1):
        min_index=i
        for j in range(i+1,len(array)):
            if(array[j]<array[min_index]):
                min_index=j
                yield array
        if(min_index!=i):
            array=swap(array,i,min_index)
            yield array
def insertion_sort(array):
    if(len(array)==1):
        return
    for i in range(1,len(array)):
        j=i
        while(j>0 and array[j]<array[j-1]):
            array=swap(array,j,j-1)
            j-=1
            yield array
n=int(input('Enter the number of elements: '))
choose=int(input('Select the sorting algorithm to use: \n1. Bubble Sort\n2. Selection Sort\n3. Insertion Sort\n4. Merge Sort\n'))
array=[i+1 for i in range(n)]
random.shuffle(array)
if(choose==1):
    title=('Bubble Sort')
    algorithm=bubble_sort(array)
elif(choose==2):
    title=('Selection Sort')
    algorithm=selection_sort(array)
elif(choose==3):
    title=('Insertion Sort')
    algorithm=insertion_sort(array)
elif(choose==4):
    title=('Merge Sort')
    algorithm=merge_sort(array,0,n-1)
fig,ax=plt.subplots()
ax.set_title('title')
bar_rec=ax.bar(range(len(array)),array,align='edge')
ax.set_xlim(0,n)
ax.set_ylim(0,int(n*1.1))
text=ax.text(0.02,0.95,'',transform=ax.transAxes)
epochs=[0]
def update_plot(array,rec,epochs):
    for rect,val in zip(rec,array):
        rect.set_height(val)
    epochs[0]+=1
    text.set_text('Epoch: '+str(epochs[0]))
anima=anim.FuncAnimation(fig,func=update_plot,fargs=(bar_rec,epochs),frames=algorithm,interval=1,repeat=False)
plt.show()