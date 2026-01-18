a=[10,2,44,23,90,99,54,34]
def bubblesort(arr):
    print("Bubble sort")
    n=len(arr)
    for i in range(n):
        flag=0
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=1
        if flag==0:
            break
    return arr
print(bubblesort(a))
def selectionsort(arr):
    print("Selection sort")
    n=len(arr)
    for i in range(n-1):
        mi=i
        for j in range(i+1,n):
            if arr[j]<arr[mi]:
                mi=j
        minv=arr.pop(mi)
        arr.insert(i,minv)
    print(arr)
b=[98,52,10,65,33,489,54,30]
selectionsort(b)
def insertionsort(arr):
    print("Insertion sort")
    n=len(arr)
    for i in range(1,n):
        insert_i=i
        curr_val=arr.pop(i)
        for j in range(i-1,-1,-1):
            if arr[j]>curr_val:
                insert_i=j
        arr.insert(insert_i,curr_val)
    print(arr)
c=[99,68,41,30,25,87,44,12,0,32]
insertionsort(c)
d=[20,21,87,85,500,654,99,32,10,50,44,7]
print("Quick sort:")
def quicksort(array,low=0,high=None):
    if high is None:
        high=len(array)-1
    if low<high:
        pivot_index=partition(array,low,high)
        quicksort(array,low,pivot_index-1)
        quicksort(array,pivot_index+1,high)
    return array
def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i+=1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high]=array[high],array[i+1]
    return i+1
print(quicksort(d))
e=[77,54,20,12,3,98,842,111,547,20]
def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    lefthalf=arr[:mid]
    righthalf=arr[mid:]
    sortl=mergesort(lefthalf)
    sortr=mergesort(righthalf)
    return merge(sortl,sortr)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
print(" Merge sort")
print(mergesort(e))
print("Linear search")
def linearsearch(arr):
    n=len(arr)
    k=int(input("enter the key element "))
    i=flag=0
    while n:
        if arr[i]==k:
            print("key element found")
            flag=1
            break
        else:
            i+=1
        n-=1
    if flag==0:
        print("Key not found")
linearsearch(e)
def binarysearch(arr):
    n=len(arr)
    k=int(input("enter the key element "))
    arr.sort()
    left=fl=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==k:
            print("Key found at index ",mid)
            fl=1
            break
        if arr[mid]>k:
            right=mid-1
        else:
            left=mid+1
    if fl==0:
        print("element not in array")
binarysearch(c)
