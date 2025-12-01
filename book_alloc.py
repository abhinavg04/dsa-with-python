arr = [2,1,3,4]
m = 2

def is_valid(mid):
    stu = 1
    maxAllocatedPage = mid
    pages = 0
    for i in range(len(arr)):
        if arr[i] > maxAllocatedPage:
            return False
        if arr[i]+pages <= maxAllocatedPage:
            pages += arr[i]
        else:
            stu += 1
            pages = arr[i]
    if stu <= m:
        return True
    else:
        return False
        
    

def allocate_books(arr, m):
    n = len(arr)
    st = 0
    end = sum(arr)
    ans = -1
    while(st <= end):
        mid = st + (end - st)//2
        if is_valid(mid):
            ans = mid
            end = mid - 1
        else:
            st = mid + 1
            
    return ans

print(allocate_books(arr, m))