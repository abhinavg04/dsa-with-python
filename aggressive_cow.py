n = 5
arr = [1,2,8,4,9]
c=3

def is_possible(arr, n, c, mid):
    last_position = arr[0]
    count = 1
    
    for i in range(1, n):
        if arr[i] - last_position >= mid:
            count += 1
            last_position = arr[i]
            
        if count == c:
            return True
            
    return False
def aggressive_cows(arr, n, c):
    arr.sort()

    start = 0
    end = arr[-1] - arr[0]
    ans = -1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if is_possible(arr, n, c, mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
            
    return ans