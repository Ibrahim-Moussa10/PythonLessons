def binarySearch(arr,l,h,key):
    if l > h:
        return False
    mid = (l + h)  //2
    if arr[mid] == key:
        return mid
    elif key > arr[mid]:
        return binarySearch(arr,mid+1,h,key)
    else:
        return binarySearch(arr,l, mid - 1,key)


arr = [1,2,3,4,5,6,7,8,9]
print(binarySearch(arr,0,len(arr)-1,1))