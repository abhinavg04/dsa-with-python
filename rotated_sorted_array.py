
arr = [15, 18, 2, 3, 6, 12]
def rsa(arr,tar):
    st,end=0,len(arr)-1
    while st<end:
        mid = st + (end-st)//2
        if arr[mid] == tar:
            return mid
        if arr[mid] >= arr[0]:
            #left part
            if tar >= arr[0] and tar <= arr[mid]:
                end = mid
            else:
                st = mid + 1
        else:
            if tar >= arr[mid] and tar <= arr[len(arr)-1]:
                st = mid
            else:
                end = mid - 1
    
print(rsa(arr,3))
    