def peak_index(arr):
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i+1] and arr[i] > arr[i-1]: #O(n) linear search
            return arr[i]
arr = [0,3,8,9,5,2,1]

print(peak_index(arr))

def peak_index_binary(arr):
    st, end = 1, len(arr)-2
    while st < end:
        mid = st + (end - st)//2
        if arr[mid] > arr[mid-1] and arr[mid] > arr [mid+1]:
            return arr[mid]
        if arr[mid-1] < arr[mid+1]:
            st = mid + 1
        else:
            end = mid-1
    return arr[st]